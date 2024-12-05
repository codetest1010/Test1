

import turtle 


t = turtle.Turtle() 

# for background 
screen = turtle.Screen() 
screen.bgcolor("yellow") 

#color and speed 
# of turtle 
# creating the house 

#t.shape("turtle") 
t.speed(5) 

# for creating base of 
# the house 
t.fillcolor('red') 
t.begin_fill() 
t.right(90) 
t.forward(150) 
t.left(90) 
t.forward(180) 
t.left(90) 
t.forward(150) 
t.left(90) 
t.forward(180) 

t.end_fill() 

# for top of 
# the house 
t.fillcolor('black') 
t.begin_fill() 
t.right(135) 
t.forward(127) 
t.right(90) 
t.forward(127) 

t.end_fill() 

turtle.done()