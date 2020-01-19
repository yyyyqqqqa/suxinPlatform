from tools.Dao import BaseService
import platform1.sqlMapperPlatform as sqlMapper

class SystemUser(BaseService):
    def __init__(self,request):
        # 调用父类中的初始化
        self.init_param(request)

    def pfus0001(self):
        # 获取初始化的参数
        param = self.param
        if not param['error'] == '0':
            return param

        sql = sqlMapper.check_sys_users_password
        temp = self.select(sql=sql, param=param)

        if not len(temp) == 1:
            param['error'] = '用户名或密码错误!!!'
            return param
        param['user_id'] = temp[0][0]
        '''记录到登录日志中去'''
        param['login_id'] = self.get_uuid()

        sql = sqlMapper.insert_user_login_log
        a = self.insert(sql=sql, param=param)

        self.commit_or_rollback()


    def pfus0002(self):
        '''新增用户'''
        # 获取初始化的参数
        param = self.param
        if not param['error'] == '0':
            return param
        '''用户登录'''

        '''验证用户名和密码'''
        sql = sqlMapper.check_sys_user_phone_exist
        temp = self.select(sql=sql, param=param)
        if temp[0][0] == 1:
            param['error'] = '手机号码不能重复!!'
            return param

        param['user_id'] = self.get_uuid()

        sql = sqlMapper.insert_sys_user
        self.insert(sql=sql, param=param)

        self.commit_or_rollback()

