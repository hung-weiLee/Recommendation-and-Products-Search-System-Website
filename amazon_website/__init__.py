from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '40c76ea5a74e4fe38e7f1138b0464a2f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Bigdata@415@ec2-34-221-148-154.us-west-2.compute.amazonaws.com:3306/amazon'
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:china666@localhost:3306/amazon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SCHEDULER_API_ENABLED '] = True

db = SQLAlchemy(app)


from amazon_website import routes
