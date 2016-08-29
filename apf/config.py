from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pathmo='/storage/emulated/0/com.hipipal.qpyplus/projects/apf/'
pathdbmo='sqlite:////storage/emulated/0/com.hipipal.qpyplus/projects/apf/nominaAPF.db3'
pathpc='D:\\SITES_OPEN\\CODIGO_GITHUB\\temp\\exemplospython\\apf\\'
pathdbpc='sqlite:///D:\\SITES_OPEN\\CODIGO_GITHUB\\temp\\exemplospython\\apf\\nominaAPF.db3'
pathpcc='C:\\PROYECTOS\\python_mongodb_examples\\apf\\'
pathdbpcc='sqlite:///C:\\PROYECTOS\\python_mongodb_examples\\apf\\nominaAPF.db3'

pathdb = pathdbpcc
path = pathpcc

engine = create_engine(pathdb)
Session = sessionmaker(bind=engine)
sesion = Session()
fecfinal = '01/01/2099'

