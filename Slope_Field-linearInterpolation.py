
#slope field mark 2 with
#linear interpolation of the acceleartion vector
#between gridpoints
import matplotlib.pyplot as plt
import turtle
import random
import numpy as np

def interp_vecs(x,y):
    x_flr = ( np.floor( (x) /Spacer) -1 ) + N
    y_flr = ( np.floor( (y) /Spacer) -1 ) + N

#the edge cases shouldn't be reachable
    x_ind = round(x_flr)
    y_ind = round(y_flr)

    a_1 = x/Spacer - np.floor(x/Spacer)
    a_2 = 1-a_1
    b_1 = y/Spacer -np.floor(y/Spacer)
    b_2 = 1-b_1

    f_1 = S * vectors[x_ind][y_ind][0]
    f_2 = S * vectors[x_ind+1][y_ind][0]
    f_3 = S * vectors[x_ind][y_ind+1][0]
    f_4 = S * vectors[x_ind+1][y_ind+1][0]

    dx = f_1*a_2*b_2 + f_2*a_1*b_2 + f_3*a_2*b_1 + f_4*a_1*b_1 

    f_1 = S * vectors[x_ind][y_ind][1]
    f_2 = S * vectors[x_ind+1][y_ind][1]
    f_3 = S * vectors[x_ind][y_ind+1][1]
    f_4 = S * vectors[x_ind+1][y_ind+1][1]

    dy = f_1*a_2*b_2+ f_2*a_1*b_2 + f_3*a_2*b_1 + f_4*a_1*b_1 
    return [dx,dy]


wn=turtle.Screen() 
wn.bgcolor("grey")
wn.tracer(0)

flakes=[]
Colors=["grey"]
num_flakes = 100
vectors= [ ]    #set up array of vectors to use as slope field
N = 35 # number of points in grid
Spacer = 10     #number of pixels between gridpoints of vectorfield

for i in range(2*N):
    vectors.append([])
    for j in range(2*N):
        #vectors[i].append( ((i) , (j)) ) 
        vectors[i].append( ((j) , (-i)) ) 
#        vectors[i].append( (np.sin(i) , np.cos(j)) ) 

Rad = 1 / (8 ) 

for i in range(num_flakes):
    flakes.append(turtle.Turtle())
    flake = flakes[i]
    flake.shape("circle")
    flake.shapesize(Rad,Rad)
    flake.shapesize(outline=Rad)
    flake.color("white")
    flake.speed(20)

    x=random.randint(-(N-1)*Spacer,(N-1)*Spacer)
    y=random.randint(-(N-1)*Spacer,(N-1)*Spacer)

    flake.penup()   
    flake.goto(x,y)                      #sets position of flake on screen
    flake.pendown()   

    S = 1 / (100)  #speed paramdeter
    #S = 1  

    [flake.dx , flake.dy] = interp_vecs(x,y)

while True:  
    wn.update()
    for i in range(num_flakes): #for flake in flakes:
        flake =  flakes[i] 
        x = flake.xcor()
        y = flake.ycor()
        flake.sety(y+flake.dy)
        flake.setx(x+flake.dx)
        [flake.dx , flake.dy] = interp_vecs(x,y)

        #checks for boundary wall collision
        if flake.xcor()>(N-1)*Spacer or flake.xcor()<-(N-1)*Spacer:
            flake.dx*=-1
            flake.penup()
            flake.setx(random.randint(-(N-1)*Spacer,(N-1)*Spacer))
            flake.pendown()
        if flake.ycor()>(N-1)*Spacer or flake.ycor()<-(N-1)*Spacer:
            flake.dy*=-1
            flake.penup()
            flake.sety(random.randint(-(N-1)*Spacer,(N-1)*Spacer))
            flake.pendown()
        if flake.dx==0 and flake.dy==0: #not moving, hop out
            flake.penup()
            flake.setx(random.randint(-N*Spacer,N*Spacer))
            flake.sety(random.randint(-N*Spacer,N*Spacer))
            [flake.dx , flake.dy] = interp_vecs(x,y)
            flake.pendown()
    
wn.mainloop()





