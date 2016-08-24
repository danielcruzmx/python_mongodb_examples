
class Pago(object):

	def __init__(self, datadict):
		if datadict != None:
		   self.rfc=datadict['rfc']
		   self.plaza=datadict['plaza']
      self.unidad=datadict['unidad']
      self.grupo=datadict['grupo']
      self.nivel=datadict['nivel']
      self.nombramiento=datadict['nombramiento']
      self.jerarquia=datadict['jerarquia']
      self.sueldo=datadict['sueldo']
      self.compensacion=datadict['compensacion']
      self.sobresueldo=datadict['sobresueldo']
      self.ultimomovimiento=datadict['ultimomovimiento']
      self.qnaproceso=datadict['qnaproceso']
      self.fechaultimomovimiento=datadict['fechaultimomovimiento']
      self.conceptospago=datadict['conceptospago']
      self.conceptospagados=datadict['conceptospagados']
      self.pensiones=datadict['pensiones']

class ConceptoPagado(object):

	def __init__(self, datadict):
		if datadict != None: 
			self.id=datadict['id']
			self.tipocpto=datadict['tipocpto']
			self.cpto=datadict['cpto']
			self.monto=datadict['monto']

class ConceptoPago(object):

	def __init__(self, datadict):
		if datadict != None: 
			self.id=datadict['id']
			self.tipocpto=datadict['tipocpto']
			self.cpto=datadict['cpto']
			self.monto=datadict['monto']
			self.porcentaje=datadict['porcentaje']
			self.fechaincidencia=datadict['fechaincidencia']
			self.qnaini=datadict['qnaini']
			self.qnafin=datadict['qnafin']
			self.qnasaplicadas=datadict['qnasaplicadas']
			self.qnasadescontar=datadict['qnasadescontar']
			self.montoadeudo=datadict['montoadeudo']
			self.qnasadeudo=datadict['qnasadeudo']

class Pension(object):

	def __init__(self, datadict):
		if datadict != None: 
			self.num_pension=datadict['num_pension']
			self.beneficiario=datadict['beneficiario']
			self.monto=datadict['monto']
			self.porcentaje=datadict['porcentaje']
			self.montoadeudo=datadict['montoadeudo']
			self.qnaaplicacadeudo=datadict['qnaaplicacadeudo']
			self.qnadescadeudo=datadict['qnadescadeudo']
			self.cptosporcentaje=datadict['cptosporcentaje']

