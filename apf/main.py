from pago import Pago, Pension, ConceptoPago, ConceptoPagado
from utils import read_file_to_reader, reader_to_list_dict
from config import path
from calc import ispt, calcula

if __name__ == '__main__':

  rdatos = read_file_to_reader(path + "empleado.csv")
  
  if rdatos != None:
    empleados = reader_to_list_dict(rdatos, None, None)

    for e in empleados:
      oPago=Pago(e)
      print '\n'
      rfc = oPago.rfc
      print rfc
      rcptos=read_file_to_reader(path + "conceptos.csv")
      lcptos=reader_to_list_dict(rcptos, "rfc", rfc)
      oPago.setconceptospago(lcptos)
      oPago.setconceptospagados(calcula(oPago))
      for c,v in oPago.conceptospagados.items():
        if v['Valor'] > 0 :
          print '%s %s -> %s' % (v['Concepto'],v['Descripcion'],v['Valor'])
  
  

