from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pathpc='D:\\SITES_OPEN\\CODIGO_GITHUB\\temp\\exemplospython\\apf\\'
pathdbmo='sqlite:////storage/emulated/0/com.hipipal.qpyplus/projects/apf/nominaAPF.db3'
pathdbpc='sqlite:///D:\\SITES_OPEN\\CODIGO_GITHUB\\temp\\exemplospython\\apf\\nominaAPF.db3'
pathmo='/storage/emulated/0/com.hipipal.qpyplus/projects/apf/'

pathdb = pathdbpc
path = pathpc

engine = create_engine(pathdb)
Session = sessionmaker(bind=engine)
sesion = Session()
fecfinal = '01/01/2099'

