

# ============================系统用户模块
'''验证用户名和密码'''
check_sys_users_password = '''select a.id from sys_users a where a.phone = :phone and a.password = :password'''
'''插入用户登录信息'''
insert_user_login_log = '''insert into login_log(id,user_id,last_date)values(:login_id,:user_id,sysdate)'''
'''检查用户手机号是否已经存在 , 手机号作为登录使用'''
check_sys_user_phone_exist = '''select count(1) from sys_users a where a.phone = :phone'''
'''新增系统用户'''
insert_sys_user = '''insert into sys_users(id, name, birthday, sex, phone, email, account, password ) 
              values( :user_id, :name, to_date(:birthday,'yyyy-mm-dd'), :sex, :phone, :email, :account, :password )'''
'''验证用户login_id是否还在有效期'''
check_loginid_period_time = '''select count(1) from login_log a where a.id = :login_id and a.create_date > sysdate - 0.5 and a.last_date > sysdate - 0.02'''



# ============================平台的服务模块
'''通过服务ID获取服务系统'''
get_service_by_id = '''select a.name,a.in_param,a.out_param,a.note from SERVICE_TAB a where a.id = :service_id'''
'''查询服务 , 可以按照系统 或模块 或 服务ID查询'''
get_service_by_id_or_module_sys = '''select a.id,a.name,a.in_param,a.out_param,a.note from SERVICE_TAB a 
          where (a.sys_id = :id or a.module_id = :id or a.service_id = :id or a.id = :id)'''
'''取该模块最大的服务号'''
get_maxid_in_a_module = '''select max(a.service_id) from service_tab a 
          where a.sys_id = :sys_id and a.module_id = :module_id'''
'''插入服务信息'''
insert_service_infos = '''insert into service_tab(sys_id,module_id,service_id,name,in_param,out_param,note)
          values (:sys_id,:module_id,:new_service_id,:name,:in_param,:out_param,:note)'''



#=============================模块
'''通过ID获取模块系统'''
get_module_by_id = '''select a.id,a.name,a.note from MODULE_TAB a where a.id = :id'''


