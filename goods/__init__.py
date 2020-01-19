from flask import Blueprint


goods_blue = Blueprint('goods',__name__)

#在创建蓝图之后导入views

from goods import views