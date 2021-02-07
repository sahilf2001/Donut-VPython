from vpython import *
canvas(background = color.purple)
donut = ring(radius =  0.5,thickness=0.25,color = vector(400,100,1))
chocolate = ring(radius =  0.55,thickness=0.25,color = vector(0.4,0.2,0))
radian = 0
while True:
    rate(8)
    donut.pos = vector(3*cos(radian),sin(radian),2)#static
    chocolate.pos = vector(3*cos(radian),sin(radian),2)
    #donut.rotate(angle=radian,axis=vector(0,1,0))#vector(x-rotation,y-rotation,z-rotation)
    #chocolate.rotate(angle=radian,axis=vector(0,1,0))#vector(x-rotation,y-rotation,z-rotation)
    radian += 0.05