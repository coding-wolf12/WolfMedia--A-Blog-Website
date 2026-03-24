import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app )
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert'
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'codingwolf12@gmail.com'
app.config['DEBUG'] = os.getenv("DEBUG", "False") == "True"
mail =Mail(app)


from wolfmedia import routes
