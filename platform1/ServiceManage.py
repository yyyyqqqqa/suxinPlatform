from tools.Dao import BaseService
import platform1.sqlMapperPlatform as sqlMapper
import json

class ServiceManagement(BaseService):
    def __init__(self,  request):
        # 调用父类中的初始化 在子类写一下, 能让大家知道有这件事情 andy
        self.init_param( request)

    def pfsm0001(self):
        if not self.param['error'] == '0':
            return self.param

        '''查询服务 , 可以按照系统 或模块 或 服务ID查询'''
        sql = sqlMapper.get_service_by_id_or_module_sys
        a = self.select(sql=sql, param=self.param)
        if not len(a) > 0:
            self.param['error'] = '没有查询到服务'
            return self.param
        self.param['list'] = a

    def pfsm0002(self):
        # '''新增服务'''
        # '''验证该模块是否存在'''
        a = {}  # 临时一个变量
        a['id'] = self.param['sys_id'] + self.param['module_id']
        sql = sqlMapper.get_module_by_id
        b = self.select(sql=sql, param=a)
        if not len(b) == 1:
            self.param['error'] = '模块或系统不存在!!!'
            return self.param

        # '''取该模块最大的服务号'''
        sql = sqlMapper.get_maxid_in_a_module
        b = self.select(sql=sql, param=self.param)
        if len(b) == 0:
            self.param['new_service_id'] = '0001'
        elif len(b) == 1:
            # 如果该模块已经有了 , 那就加 1
            a = int(b[0][0]) + 1
            a = '0000' + str(a)
            self.param['new_service_id'] = a[len(a) - 4:]
        # '''插入服务信息'''
        sql = sqlMapper.insert_service_infos
        self.insert(sql=sql, param=self.param)
        # if a.rowcount() == 1:
        #     self.param['error'] = '服务错误!!'
        self.commit_or_rollback()




