
#First iteration of the slope field idea
import matplotlib.pyplot as plt
import turtle
import random
import numpy as np

wn=turtle.Screen() 
wn.bgcolor("grey")
wn.title("SlopeField") #sets title of the screen, doesnt seem to do anythin
wn.tracer(0)

flakes=[]
Colors=["grey"]
num_flakes = 100

#set up array of vectors to use as slope field
vectors= [  ] 
N = 35
Spacer = 10 
#number of pixels between gridpoints of vectorfield
for i in range(2*N):
    vectors.append([])
    #print(i)
    for j in range(2*N):
        #vectors[i].append( ((i) , (j)) ) 
        #vectors[i].append( ((j) , (-i)) ) 
        vectors[i].append( (np.sin(i) , np.cos(j)) ) 

        #vectors[i].append( (0,1) ) 
            #vectors[i].append( ((50) , (50)) ) 
        #print(j)
#print(vectors) 

Rad = 1 / (8 ) 

for i in range(num_flakes):
    flakes.append(turtle.Turtle())
    flake = flakes[i]
    #flake.shape("circle")
    flake.shape("circle")
    flake.shapesize(Rad,Rad)
    flake.shapesize(outline=Rad)

    flake_color =  "white"
    flake.color(flake_color)

    flake.speed(20)
    x=random.randint(-N*Spacer,N*Spacer)
    y=random.randint(-N*Spacer,N*Spacer)

    flake.penup()   
    flake.goto(x,y)                      #sets position of flake on screen
    flake.pendown()   

    S = 1 / (10)  #speed paramdeter
    S = 1  

    x_ind =  ( round( (x) /Spacer) -1 ) + N
    y_ind = ( round( (y) /Spacer) -1 ) + N

    flake.dx= S * vectors[x_ind][y_ind][0]
    flake.dy= S * vectors[x_ind][y_ind][1]

while True:  
    wn.update()
    #for flake in flakes:
    for i in range(num_flakes):
        flake =  flakes[i] 
        x = flake.xcor()
        y = flake.ycor()

        #flake.forward( flake.dx )
        #flake.left( flake.dy )
        flake.sety(y+flake.dy)
        flake.setx(x+flake.dx)

    #    x_ind = round( abs(x) /10 ) -1
    #    y_ind = round( abs(y) /10 ) -1
        x_ind =  ( round( (x) /Spacer) -1 ) + N
        y_ind = ( round( (y) /Spacer) -1 ) + N

        flake.dx = S * vectors[x_ind][y_ind][0]
        flake.dy = S * vectors[x_ind][y_ind][1]

        #checks for boundary wall collision
        if flake.xcor()>300 or flake.xcor()<-300:
            flake.dx*=-1
            flake.penup()
            flake.setx(random.randint(-N*Spacer,N*Spacer))
            flake.pendown()
        if flake.ycor()<-270 or flake.ycor()>270:
            flake.dy*=-1
            flake.penup()
            flake.sety(random.randint(-N*Spacer,N*Spacer))
            flake.pendown()
    
wn.mainloop()



