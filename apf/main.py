from pago import Pago, Pension, ConceptoPago, ConceptoPagado
from utils import read_file_to_reader, reader_to_list_dict
from config import pathpc
#from utils import ispt

# abrir archivo de empleados
# abrir archivo de conceptos y pensiones
# actualizar conceptos y pensiones por empleado
# hacer lista de

if __name__ == '__main__':
  #grav = 10000.0
  #print ispt(grav)
 
  
  
  c1={'id':413249,
      'tipocpto':'D',
      'cpto':'82',
      'monto':0,
      'porcentaje':10.0,
      'fechaincidencia':'22/01/2014',
      'qnaini':200717,
      'qnafin':209901,
      'qnasaplicadas':61,
      'qnasadescontar':2193,
      'montoadeudo':0,
      'qnasadeudo':0
     }
  c2={'id':204246,
      'tipocpto':'D',
      'cpto':'51',
      'monto':275.13,
      'porcentaje':0,
      'fechaincidencia':'28/07/2010',
      'qnaini':201015,
      'qnafin':0,
      'qnasaplicadas':145,
      'qnasadescontar':0,
      'montoadeudo':0,
      'qnasadeudo':0
     }
  c3={'id':238051,
      'tipocpto':'P',
      'cpto':'A1',
      'monto':275.13,
      'porcentaje':0,
      'fechaincidencia':'24/07/2007',
      'qnaini':200713,
      'qnafin':209901,
      'qnasaplicadas':217,
      'qnasadescontar':0,
      'montoadeudo':0,
      'qnasadeudo':0
     }
  c4={'id':1484401,
      'tipocpto':'D',
      'cpto':'03',
      'monto':518.2,
      'porcentaje':0,
      'fechaincidencia':'08/09/2015',
      'qnaini':201518,
      'qnafin':201705,
      'qnasaplicadas':23,
      'qnasadescontar':36,
      'montoadeudo':0,
      'qnasadeudo':0
     }
  
  '''objp = Pago(p)
  cptospago = []

  cp1 = ConceptoPago(c1)
  cptospago.append(cp1.toDbCol())
  cp2 = ConceptoPago(c2)
  cptospago.append(cp2.toDbCol())
  cp3 = ConceptoPago(c3)
  cptospago.append(cp3.toDbCol())
  cp4 = ConceptoPago(c4)
  cptospago.append(cp4.toDbCol())

  objp.setconceptospago(cptospago) 
  objp.calcula()

  print objp.conceptospago'''

rdatos = read_file_to_reader(pathpc + "empleado.csv")

if rdatos != None:
  empleados = reader_to_list_dict(rdatos, None, None)

  for e in empleados:
     #print e
     oPago=Pago(e)
     rcptos=read_file_to_reader(pathpc + "conceptos.csv")
     lcptos=reader_to_list_dict(rcptos, None, None)
     oPago.setconceptospago(lcptos)
     #print oPago.toDbCol()
     #cptospago = []
     #cp1 = ConceptoPago(c1)
     #cptospago.append(cp1.toDbCol())
     #oPago.setconceptospago(cptospago)
     print oPago.toDbCol()
  
  

