from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

path='C:\\proyectos_open_shift_daniel\\python_mongodb_examples\\'
pathdb='sqlite:////storage/emulated/0/com.hipipal.qpyplus/projects3/NApf/nominaAPF.db3'
pathdbpc='sqlite:///D:\\SITES_OPEN\\CODIGO_GITHUB\\python_mongodb_examples\\apf\\nominaAPF.db3'

engine = create_engine(pathdb)
Session = sessionmaker(bind=engine)
sesion = Session()
fecfinal = '01/01/2099'

