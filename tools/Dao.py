import configparser,uuid,json,tools.GlobalTools as gt
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import create_engine
from datetime import date
import platform1.sqlMapperPlatform as sqlMapper

class DaoPool(object):
    __isinstance = False  # 设置一个私有变量，默认没有被实例化

    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:  # 如果被实例化了
            cls.__isinstance = object.__new__(cls)  # 否则实例化
        return cls.__isinstance  # 返回实例化的对象

    def __init__(self, host=None, port=None, sid=None, user=None, password=None):
        '''
        初始化数据库的链接类 , 如果为空 , 则取config.ini 中默认参数
        :param host:
        :param port:
        :param sid:
        :param user:
        :param password:
        '''
        self.db_log_print = False
        if host and port and sid and user and password:
            pass
        else:
            conf = configparser.ConfigParser()
            conf.read('config.ini', encoding='utf-8')
            if not host:
                host = conf.get('database', 'host')
            if not port:
                port = conf.get('database', 'port')
            if not sid:
                sid = conf.get('database', 'sid')
            if not user:
                user = conf.get('database', 'user')
            if not password:
                password = conf.get('database', 'password')
            if conf.get('sys', 'db_log_print') == '1':
                self.db_log_print = True
        engine = create_engine(
            "oracle+cx_oracle://{user}:{password}@{host}:{port}/{sid}".format(user=user, password=password, host=host,
                                                                              port=port, sid=sid),
            max_overflow=30,  # 超过连接池大小外最多创建的连接
            pool_size=5,  # 连接池大小
            pool_timeout=10,  # 池中没有线程最多等待的时间，否则报错
            pool_recycle=-1,  # 多少秒之后对线程池中的线程进行一次连接的回收（重置）
            echo=self.db_log_print
        )
        self.SessionFactory = sessionmaker(bind=engine)

        pass
    def get_sesson(self):
        return scoped_session(self.SessionFactory)

class Dao(object):
    '''
    封装oracle数据库操作类
    '''

    def __init__(self):
        self.pool = DaoPool()
        self.sesson = self.pool.get_sesson()
        self.result = None
        pass

    def __del__(self):
        self.colse_db(self)
        pass

    def execute(self, sql, param=None):
        '''
        执行数据库语句 ,
        :param sql:
        :param param:
        :return:
        '''
        # self.sql_log(self, sql, param)
        self.result = self.sesson.execute(sql, param)
        return self.result

    def select(self, sql=None, param=None, rownum=100):
        '''
        :param sql: 数据库语句 , 如果不为None ,则视为第一次调用, 如果不是则直接返回行数 , 一直到空
        :param param: sql语句的绑定参数
        :param rownum: 默认每次返回10行
        :return:
        '''
        if sql:
            self.execute(sql, param)
        return self.result.fetchmany(rownum)

    def insert(self, sql, param=None):
        return self.execute(sql, param)

    def update(self, sql, param=None):
        return self.execute(sql, param)

    def delete(self, sql, param=None):
        return self.execute(sql, param)

    def commit_or_rollback(self, YN=True):
        if self.sesson is None:
            return
        if YN:
            self.sesson.commit()
        else:
            self.sesson.rollback()
        return

    def colse_db(self):
        if self.sesson:
            self.sesson.remove()
        return
    def sql_log(self,sql,param):
        log_sesson = self.pool.get_sesson()

        self.result = self.sesson.execute(sql, param)
        log_sesson.remove()



class BaseService(object):

    def __init__(self, request):
        '''
        初始化任务, 并检查参数合理 , 记录 本次访问
        :param request:  获取本次请求对象
        '''
        self.init_param( request)
        pass

    def __del__(self):
        if self.dao:
            self.dao.colse_db()

    def invoke(self):
        print('要在之类中实现,controller中一定会调用')
        pass

    def init_param(self,request):
        param = request.get_json()
        param['service_id'] = request.service_id
        param['error'] = '0'
        self.param = param
        self.dao = Dao()

        self.check_param()

        '''用户权限检查 privilege
        以后添加吧        '''

        '''用户登录检查'''
        return self.param
        if not self.param['service_id'] == 'pfus0001':
            if self.param['login_id'] is None:
                self.param['error'] = '用户没有登录!!!'
                return '跳转到登录页面'
            sql = sqlMapper.check_loginid_period_time
            a = self.select(sql=sql, param=self.param)
            if not a[0][0] == 1:
                self.param['error'] = '服务ID错误!!!'
                return self.param

    def check_param(self):
        '''服务检查 , 同时把服务保存下来'''
        if not self.param['service_id']:
            self.param['error'] = '服务ID不能为空'
            return self.param
        sql = sqlMapper.get_service_by_id
        a = self.select(sql=sql, param=self.param)
        if not len(a) == 1:
            self.param['error'] = '服务ID错误!!!'
            return self.param
        self.service = {}
        self.service['service_id'] = self.param['service_id']
        self.service['name'] = a[0][0]
        self.service['in_param'] = json.loads(a[0][1])
        self.service['out_param'] = json.loads(a[0][2])
        self.service['note'] = a[0][3]

        for k,v in self.service['in_param'].items():
            # 第一判断是否必须 , 长度是否够
            if self.param.get(k) is None:
                self.param[k] = ''
            if v[0] == '==0':
                pass
            else:
                if not eval(str(len(self.param[k])) + v[0]):
                    self.param['error'] = '参数:{}长度不符合'.format(k)
                    return self.param

            # 判断类型 int , str , date
            if v[1] == 'int':
                if not gt.is_number(self.param[k]):
                    self.param['error'] = '参数:{1}必须是数字'.format(k)
                    return self.param
            elif v[1] == 'str':
                pass
            elif v[1][0:4] == 'date':
                # 以后有时间在写对日期的判断吧
                pass
            else:
                pass

    # 返回该服务指定的参数
    def return_param(self):
        # 必须要深copy 不然参数会跟着变
        keys = gt.deep_copy(list(self.param.keys()))
        for key in keys:
            # 如果不在返回的参数中 那就删除 , 如果报错了 ,那就只返回报错信息
            if key=='error': continue
            if key not in self.service['out_param'].keys() or not self.param['error']=='0':
                self.param.pop(key)
        return self.param

    def job_execute_log(self):
        self.param['param0'] = str(self.param)
        if self.param['job_id']:
            sql = r'update job_execute_log a set a.end_date = sysdate,a.out_param = :param0 where a.id = :job_id'
            a = self.update(sql=sql, param=self.param)
            del self.param['param0']
        else:
            self.param['job_id'] = self.get_uuid()
            self.param['param0'] = str(self.param)
            sql = r'insert into job_execute_log(id,service_id,login_id,in_param)values(:job_id,:service_id,:login_id,:param0)'
            a = self.insert(sql=sql, param=self.param)
        del self.param['param0']
        self.commit_or_rollback()
        return self.param

    def get_uuid(self):
        '''获取一个32位随机主键 前面6位是年月日yymmdd , 基本上不会重复'''
        id = date.strftime(date.today(),'%y%m%d') + uuid.uuid4().__str__()[10:36]
        return id

    # 数据库访问 比较方便了 , 调用自己生成的dao 去访问数据库
    def select(self, sql=None, param=None, rownum=None):
        a = self.dao.select(sql=sql, param=param, rownum=rownum)
        i = 0
        while i < len(a):
            a[i] = list(a[i])
            i += 1
        return a
    def insert(self, sql, param=None):
        return self.dao.insert(sql=sql,param=param)
    def update(self, sql, param=None):
        return self.dao.update(sql=sql,param=param)
    def delete(self, sql, param=None):
        return self.dao.delete(sql=sql,param=param)
    def commit_or_rollback(self, YN=True):
        return self.dao.commit_or_rollback(YN=YN)
    def colse_db(self):
        return self.dao.colse_db()