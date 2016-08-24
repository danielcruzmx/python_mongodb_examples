from pago import Pago, Pension, ConceptoPago, ConceptoPagado
from utils import read_file_to_reader, reader_to_list_dict
from utils import ispt

# abrir archivo de empleados
# abrir archivo de conceptos y pensiones
# actualizar conceptos y pensiones por empleado
# hacer lista de

if __name__ == '__main__':
  #grav = 10000.0
  #print ispt(grav)
  p = {
  'rfc':'CUCD6308017Y1',
  'plaza':902,
  'unidad':'711',
  'grupo':'ESTRUCTURA',
  'nivel':'N33',
  'nombramiento':'CONFIANZA',
  'jerarquia': 'MANDO MEDIO',
  'sueldo': 8000.0,
  'compensacion': 39000.0,
  'sobresueldo': 0.0,
  'ultimomovimiento': '502',
  'qnaproceso':201617,
  'fechaultimomovimiento':'01/01/2011',
  'conceptospago':[],
  'conceptospagados':[],
  'pensiones':[]
  }
  
  cptos = [
     {},
     {},
     {}
  ]

  objp = Pago(p)
  print objp.rfc
  
  

