
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

	def setconceptospago(self, conceptospago):
		self.conceptospago = conceptospago		
		
	def toDbCol(self):
		return {
            "rfc": self.rfc,
            "plaza": self.plaza,
            "unidad": self.unidad,
            "grupo": self.grupo,
            "nivel": self.nivel,
            "nombramiento": self.nombramiento,
            "jerarquia": self.jerarquia,
            "sueldo": self.sueldo,
            "compensacion": self.compensacion,
            "sobresueldo": self.sobresueldo,
            "ultimomovimiento": self.ultimomovimiento,
            "qnaproceso": self.qnaproceso,
            "fechaultimomovimiento": self.fechaultimomovimiento,
            "conceptospago": self.conceptospago,
            "conceptospagados": self.conceptospagados,
            "pensiones": self.pensiones
      	}		

	def calcula(self):
		pass

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

	def toDbCol(self):
		return {
            "id": self.id,
            "tipocpto": self.tipocpto,
            "cpto": self.cpto,
            "monto": self.monto,
            "porcentaje": self.porcentaje,
            "fechaincidencia": self.fechaincidencia,
            "qnaini": self.qnaini,
            "qnafin": self.qnafin,
            "qnasaplicadas": self.qnasaplicadas,
            "qnasadescontar": self.qnasadescontar,
            "montoadeudo": self.montoadeudo,
            "qnasadeudo": self.qnasadeudo
      	}		

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

