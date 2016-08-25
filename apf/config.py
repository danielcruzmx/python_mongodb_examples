from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pathpc='D:\\SITES_OPEN\\CODIGO_GITHUB\\temp\\exemplospython\\apf\\'
pathdb='sqlite:////storage/emulated/0/com.hipipal.qpyplus/projects3/NApf/nominaAPF.db3'
pathdbpc='sqlite:///D:\\SITES_OPEN\\CODIGO_GITHUB\\python_mongodb_examples\\apf\\nominaAPF.db3'

engine = create_engine(pathdbpc)
Session = sessionmaker(bind=engine)
sesion = Session()
fecfinal = '01/01/2099'

