import xlwt
#from datetime import datetime
wb = xlwt.Workbook()
ws = wb.add_sheet('hola')
ws.write(0,0,'test')
wb.save('/storage/emulated/0/com.hipipal.qpyplus/scripts/example.xls')
