__author__ = 'daniel_cruz'

import requests

objetopago = { "rfc": "CUCD6308017Y1",
               "plaza": 902,
               "conceptospago": [
                  {"tipocpto": "D", "cpto": "51", "monto": 275.13,  "porcentaje": 0.0 },
                  {"tipocpto": "P", "cpto": "A1", "monto": 50.0,    "porcentaje": 0.0 },
                  {"tipocpto": "D", "cpto": "82", "monto": 2394.55, "porcentaje": 10.0},
                  {"tipocpto": "D", "cpto": "03", "monto": 518.2,   "porcentaje": 0.0 },
                  {"tipocpto": "D", "cpto": "94", "monto": 1223.72, "porcentaje": 0.0 }
                  ],
              "nivel": "N33",
              "jerarquia": "MANDO MEDIO",
              "nombramiento": "CONFIANZA",
              "grupo": "ESTRUCTURA",
              "ultimomovimiento": "520",
              "unidad": "711",
              "sobresueldo": 0.0,
              "compensacion": 40970.45,
              "sueldo": 8357.21,
              "pensiones": "",
              "conceptospagados": "",
             }

objetopag = { "rfc": "CUCD6308017Y1",
               "plaza": 902,
               "conceptospago": "..",
              "nivel": "N33",
              "jerarquia": "mando medio",
              "nombramiento": "confianza",
              "grupo": "presupuestal",
              "ultimomovimiento": "520",
              "unidad": "711",
              "sobresueldo": 0.0,
              "compensacion": 40970.45,
              "sueldo": 8357.21,
              "pensiones": "..",
              "conceptospagados": "..",
             }


resp = requests.post('http://calcapf-danycruzmx.rhcloud.com/calculo/', json=objetopag)

if resp.status_code != 201:
    print 'POST /calculo/ {}'.format(resp.status_code)

print resp.json()

