import turtle

radio = 20

turtle.fillcolor('red')

turtle.begin_fill()
while radio <= 80:
    radio += 10
    turtle.circle(radio)

turtle.end_fill()