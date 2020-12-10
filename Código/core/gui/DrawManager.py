import turtle, json


"""
Clase encargada de los controles de los dibujos
@authors eglopezl@unah.hn lemartinezm@unah.hn
@source Data Structures and Algorithms with Python 2nd, 2015, Kent D. Lee, Steve Hubbard
"""
class GoToCommand:
    def __init__(self,x,y,width=1,color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        

    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x,self.y)
        

    def __str__(self):
        return '''				"GoTo" : 
				{begin}
					"x": "{x}",
					"y": "{y}",
					"width": "{width}",
					"color": "{color}"
				{end}'''.format(
						begin = "{",
						end="}",
						x=str(self.x),
						y=str(self.y),
						width=str(self.width),
						color=self.color
					)
 
#
# Esta clase se encarga de dibujar un circulo
#
class CircleCommand:
    def __init__(self,radius, width=1,color="black"):
        self.radius = radius
        self.width = width
        self.color = color
        
    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)
        
    def __str__(self):
        return '''				"Circle" : 
				{begin}
					"radius": "{radius}",
					"width": "{width}",
					"color": "{color}"
				{end}'''.format(
						begin = "{",
						end="}",
						radius=str(self.radius),
						width=self.width,
						color=self.color
					)

#
# Esta clase inicia el rellenado del dibujo
#
class BeginFillCommand:
    def __init__(self,color):
        self.color = color
        
    def draw(self,turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        
    def __str__(self):
        return '''				"BeginFill" : 
				{begin}
					"color": "{color}"
				{end}'''.format(
						begin = "{",
						end="}",
						color=self.color
					)
#
# Esta clase termina el rellenado del dibujo
#
class EndFillCommand:
    def __init__(self):
        pass
    
    # end_fill se usa para rellenar la forma dibujada despues del begin
    def draw(self,turtle):
        turtle.end_fill()
        
    def __str__(self):
        return '''				"EndFill" : {begin}{end}'''.format(begin = "{", end = "}")	
       
#
# Esta levanta el lapiz
#
class PenUpCommand:
    def __init__(self):
        pass
    
    def draw(self,turtle):
        turtle.penup()
        
    def __str__(self):
        return '''				"PenUp" : {begin}{end}'''.format(begin = "{", end = "}")	
       
#
# Esta baja el lapiz
# 
class PenDownCommand:
    def __init__(self):
        pass
    
    def draw(self,turtle):
        turtle.pendown()
        
    def __str__(self):
        return '''				"PenDown" : {begin}{end}'''.format(begin = "{", end = "}")

