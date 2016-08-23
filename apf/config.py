from flask import Flask, abort, request
from os import environ
#
UPLOAD_FOLDER = '/storage/emulated/0/com.hipipal.qpyplus/projects/calculoBatch/'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])
app = Flask(__name__)
#
#	PARAMETROS DE CONFIGURACION
#
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////storage/emulated/0/com.hipipal.qpyplus/projects3/NApf/nominaAPF.db3'
#app.config['SQLALCHEMY_DATABASE_URI'] = environ['OPENSHIFT_MYSQL_DB_URL'] + environ['OPENSHIFT_APP_NAME']
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
#
#   VARIABLE GLOBAL
#
#fecfinal = '2099-01-01'
fecfinal = '01/01/2099'
plazas = []
fileplazas = 'plazas_711.txt'

#import os
#from flask import Flask, request, redirect, url_for
#from werkzeug import secure_filename
#app = Flask(__name__)
