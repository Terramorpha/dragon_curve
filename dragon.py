#!/bin/python
from sys import argv
import  turtle

iter = argv[1]
print iter, "iter"
striter = str(iter)
#print striter[::-1]
def reverse(x):
    return x[::-1]
def inverse(x):
    product = ""
    for i in x:
        
        if i == "1":
            product = product + "0"
        elif i == "0":
            product = product + "1"
        else:
            return "dafuq man", i
    return product


#print inverse("110")

#x = reverse(striter)
#print inverse(x)

#######
"""
jusq'ici j'ai la fonction reverse et inverse

"""
#######

def nextiter(x):
    return x + "1" + str(inverse(reverse(x)))

#print nextiter(striter)
x = 0
rol = "1"
for i in range(int(iter)):
    print x
    rol = nextiter(rol)
    x += 1
print rol
new = rol
#print nextiter("1110110110010011101100100100")
printans=raw_input('Display r/l form?(y/n):')
#if yes, print the iteration
if printans=='y':
    print(new)
r = '0'
l = '1'
#prepare to display the graphics
#do not show the turtle icon when drawing
pencolor = "black"
bgcolor = "white"
length = int(argv[2])
turtle.ht()
#set drawing speed to fastest(no animation)
turtle.speed("fastest")
#set pen color as requested
turtle.color(pencolor)
#set background color as requested
turtle.bgcolor(bgcolor)

#display segment of desired length to build off of
turtle.forward(length)

#cycling through all the characters in the iteration
for char in range(0,len(new)):
    #if the character is a right:
    if new[char] == (r):
        #turn right at a right angle 
        turtle.right(90)
        #go forward desired length
        turtle.forward(length)
    #otherwise, if the character is a left:
    elif new[char] == (l):
        #turn left at a right angle
        turtle.left(90)
        #go forward desired length
        turtle.forward(length)
i = raw_input("quit ?")
