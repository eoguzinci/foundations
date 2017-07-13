import turtle

def draw_square():
	
	brad = turtle.Turtle()
	brad.shape('circle')
	brad.color('yellow')
	brad.speed(2)

	for x in range(4):
		brad.forward(100)
		brad.right(90)
		
def draw_circle():
	angie = turtle.Turtle()
	angie.shape('arrow')
	angie.color('green')
	angie.circle(50)

def draw_triangle():
	ahmet = turtle.Turtle()
	ahmet.shape("classic")
	ahmet.color("red")

	ahmet.right(120)
	for x in range(3):
		ahmet.forward(100)
		ahmet.right(120)


window = turtle.Screen()
window.bgcolor('blue')
draw_square()
draw_circle()
draw_triangle()

window.exitonclick()