from .DrawManager import *
import json

"""
Clase encargada de los comandos
@authors eglopezl@unah.hn lemartinezm@unah.hn
@source Data Structures and Algorithms with Python 2nd, 2015, Kent D. Lee, Steve Hubbard
"""
class PyList:
	def __init__(self):
		self.gcList = []

	# Este metodo agrega un nuevo comando a la lista.
	def append(self,item):
		self.gcList = self.gcList + [item]

	# Este metodo elimina el ultimo objeto
	def removeLast(self):
		self.gcList = self.gcList[:-1]

 	# Este metodo es llamado cuando trabajamos con un iterados como en una sentencia for
	def __iter__(self):
		for c in self.gcList:
			yield c
    
	# Esta metodo es el que se llama cuando usan len        
	def __len__(self):
		return len(self.gcList)
        

	# Este comando es el encargado de escribir un archivo json al guardar
	def create(self,filename, content): 
		# filename contiene la ruta del archivo donde guardaremos el json
		# json_content contiene los comandos json 
		file = open(filename,"w")

		# ingresamos los primeros 2 objetos del json {"GraphicsCommands":{"Command":{}}}
		json_content = '{\n\t"GraphicsCommands":\n\t{\n'
		json_content += '%s"Command":\n%s[\n' % ("\t"*2,"\t"*2)

		for cmd in self:
			json_content +='%s{\n%s\n%s},\n' % ("\t"*3,str(cmd),"\t"*3)

		# json_content[:-2] limpiar una coma extra en el json y agregamos un espacio
		json_content = json_content[:-2] + "\n"
		json_content += '%s]\n' % ("\t"*2)
		json_content += '\t}\n}'
		file.write(json_content)
		file.close()
		
		return json_content


	# Este comando es el encargado de escribir un archivo json al guardar
	def write(self): 
		# filename contiene la ruta del archivo donde guardaremos el json
		# json_content contiene los comandos json 
		#file = open(filename,"w")

		# ingresamos los primeros 2 objetos del json {"GraphicsCommands":{"Command":{}}}
		json_content = '{\n\t"GraphicsCommands":\n\t{\n'
		json_content += '%s"Command":\n%s[\n' % ("\t"*2,"\t"*2)

		for cmd in self:
			json_content +='%s{\n%s\n%s},\n' % ("\t"*3,str(cmd),"\t"*3)

		# json_content[:-2] limpiar una coma extra en el json y agregamos un espacio
		json_content = json_content[:-2] + "\n"
		json_content += '%s]\n' % ("\t"*2)
		json_content += '\t}\n}'
		#file.write(json_content)
		#file.close()
		
		return json_content

    # Este metodo es el encargado de leer un archivo json
	# y tambien creara la lista de comandos a dibujar
	def parse(self,filename):    
		
		js = filename#json.loads(filename)
		Commands = js["GraphicsCommands"]["Command"]
	
		for jsonCommand in Commands:
			for command,atributtes in jsonCommand.items():				
				if command == "GoTo":
					x = float(atributtes["x"])
					y = float(atributtes["y"])
					width = float(atributtes["width"])
					color = atributtes["color"]
					cmd = GoToCommand(x,y,width,color)
				elif command == "Circle":
					radius = float(atributtes["radius"])
					width = int(float(atributtes["width"]))
					color = atributtes["color"]
					cmd = CircleCommand(radius,width,color)
				elif command == "BeginFill":
					color = atributtes["color"]
					cmd = BeginFillCommand(color)
				elif command == "EndFill":
					cmd = EndFillCommand()
				elif command == "PenUp":
					cmd = PenUpCommand()
				elif command == "PenDown":
					cmd = PenDownCommand()
				else:
					raise RuntimeError("Comando Desconocido: " + command) 


				self.append(cmd)