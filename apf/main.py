from pago import Pago
from utils import read_file_to_reader, reader_to_list_dict
from config import path
from calc import calc

if __name__ == '__main__':

  # LEE EMPLEADOS
  rdatos = read_file_to_reader(path + "empleados.txt")

  # LEE REGLAS
  rreglas = read_file_to_reader(path + "reglas.csv")
  reglas = reader_to_list_dict(rreglas, None, None)
  lstreglas = []
  for r in reglas:
    lstreglas.append(r)

  if rdatos != None:
    empleados = reader_to_list_dict(rdatos, None, None)

    emp = raw_input(" Empleado -> ")
    print emp

    for e in empleados:
      oPago=Pago(e)
      rfc = oPago.rfc
      if rfc == emp:
          rcptos=read_file_to_reader(path + "conceptos.txt")
          lcptos=reader_to_list_dict(rcptos, "rfc", rfc)
          oPago.setconceptospago(lcptos)
          oPago.setconceptospagados(calc(oPago, lstreglas))
          for c,v in oPago.conceptospagados.items():
            if v['Valor'] > 0 :
                print '%s %s -> %s' % (v['Concepto'],v['Descripcion'],v['Valor'])



