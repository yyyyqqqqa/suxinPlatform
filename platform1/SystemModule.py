
from tools.Dao import BaseService

class SystemModule(BaseService):
    '''模块管理包括系统管理'''
    def __init__(self,request):
        # 调用父类中的初始化
        self.init_param(request)
