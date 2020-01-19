from platform1 import *

#做为服务的路由功能
def invoke(request):
    # 根据服务的前两位找到对应的服务类 , 并该返回服务对应的类
    servaice_class = eval(request.service_id[0:2] + '_invoke(request)')

    if servaice_class is None:
        param = {}
        param['error'] = '没有找到该服务ID'
    else:
        # 根据服务ID调用服务处理数据
        eval('servaice_class.'+request.service_id+'()')
        # 服务完成后获取返回的参数
        param = servaice_class.return_param()
    return param

#平台系统
def pf_invoke(request):
    service_id = request.service_id
    if service_id[0:4] == 'pfus':
        job = SystemUser(request)
        # 平台服务管理
    elif service_id[0:4] == 'pfsm':
        job = ServiceManagement(request)
        # 平台模块&系统管理
    elif service_id[0:4] == 'pfso':
        job = SystemModule(request)
        # 平台系统菜单管理
    elif service_id[0:4] == 'pfsu':
        job = SystemMuen(request)
    else:
        job = None
    return job

#教程内容管理系统couse
def cs_invoke(request):
    service_id = request.service_id
    if service_id[0:4] == 'csuu':
        job = SystemUser(request)
    else:
        job = None
    return job

#人力资源管理系统
def hr_invoke(request):
    service_id = request.service_id
    if service_id[0:4] == 'hruu':
        job = SystemUser(request)
    else:
        job = None
    return job