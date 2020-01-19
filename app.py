from flask import Flask, request, render_template, jsonify
from goods.views import  goods_blue
# from flasgger import Swagger
# from platform1 import pf_blue

app = Flask(__name__)


# platform_blue = Blueprint('platform1',__name__)

app.register_blueprint(goods_blue,url_prefix='/gd')
# app.register_blueprint(platform_blue,url_prefix='/pf')
#
# '''对外提供微服务执行的代码'''
# @app.route('/<service_id>.do' ,methods=['GET', 'POST'])
# def to_service(service_id):
#     # 平台系统的调用platform
#     # request.service_id = service_id
#     # out_param = pf.invoke(request)
#
#     # return jsonify(out_param)
#     pass
#
@app.route('/')
def index():
    return render_template("index.html")
#
# @app.errorhandler(404)
# def err_404_handler(err):
#     #err 错误的信息
#     return render_template("index.html")
#
# @app.errorhandler(500)
# def err_500_handler(err):
#     #err 错误的信息
#     return '这是一个的500错误页面,%s' %err

# swag = Swagger(app)

if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host='192.168.98.15', port=80, debug=True)
    # app.run(debug=True)