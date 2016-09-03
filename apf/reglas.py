from utils import read_file_to_reader, reader_to_list_dict
from config import path

CONSTANTES_CALC = {
    'SAL_MIN' :    73.04,
    'AYU_DESP':    565.0,
    'PREV_SOC':    465.0,
    'AYU_SERV':    435.0,
    'APO_DES_CAP': 1400.0,
    'AYU_TRANS':   400,
    'ISSSTE_TOPE': 21912.0,
    'QUIN_A1':     100.0,
    'QUIN_A2':     125.0,
    'QUIN_A3':     175.0,
    'QUIN_A4':     200.0,
    'QUIN_A5':     225.0,
    'DIAS_PRI_EXCE': 7.5,
    'ISSSTE_PATRON': 0.0997,
    'PORC_SIND':   0.015,
    'ISSSTE_42A':  0.0275,
    'ISSSTE_42B':  0.00625,
    'ISSSTE_199':  0.005,
    'ISSSTE_102':  0.06125,
    'ISSSTE_140':  0.00625,
    'PRI_SEG_COL': 14.55,
    'FONAC_AP_TRAB': 205.0
}


#var_s = {}
#var_s.update(CONSTANTES_CALC)
#
#rreglas = read_file_to_reader(path + "reglas.csv")
#reglas = reader_to_list_dict(rreglas, None, None)

#lstReglas = []

#for r in reglas:
#    if r['orden'] != -1:
#        clave = r['variable']
#        ex = r['formula'].format(**var_s)
#        valor = eval(ex)
#        #valor = 0
#        print ex
#        print clave, valor
#        var_s.update({clave:valor})
