from pago import Pago, Pension, ConceptoPago, ConceptoPagado
from utils import read_file_to_reader, reader_to_list_dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Ispt

path='C:\\proyectos_open_shift_daniel\\python_mongodb_examples\\'
pathdb='sqlite:////storage/emulated/0/com.hipipal.qpyplus/projects3/NApf/nominaAPF.db3'
pathdbpc='sqlite:///D:\\SITES_OPEN\\CODIGO_GITHUB\\python_mongodb_examples\\apf\\nominaAPF.db3'

# abrir archivo de empleados
# abrir archivo de conceptos y pensiones
# actualizar conceptos y pensiones por empleado
# hacer lista de pagos
# hacer cpnexion con Alchemy para las tablas ispt y reglas

if __name__ == '__main__':
  engine = create_engine(pathdbpc)
  #connection = engine.connect()
  Session = sessionmaker(bind=engine)
  #result = connection.execute("select * from ispt")
  #for row in result:
  #  print row
  #connection.close()
  sesion = Session()
  res = sesion.query(Ispt).filter_by(tipo='ispt').all()
  for r in res:
    print r.fecha_ini
	

