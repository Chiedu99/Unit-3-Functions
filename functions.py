# Chiedu Nduka-Eze unit 3 9/26/16
#this program asks the user for side length, petal color, and center color to create a flower using octogons

import turtle

def getPetalColor():
    """this functions gets the petal color"""
    return input(" WHat do you want the color of the petals to be?")

def getCenterColor():
    """this function gets the center color"""
    return input("What do you want the color of the center to be?")

def getSideLength():
    """this function gets the side lengths of the octogon"""
    side = float(input("What do you want the side length to be?"))
    return side

def drawPetal(size, color):
    """this function defines what the turtle does for drawing petals"""
    turtle.color(color)
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(size)
        turtle.left(60)
    turtle.end_fill()

def drawHexagon(size, centerColor, petalColor):
    """this function makes the turtle draw the whole flower"""
    turtle.color(centerColor)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(60)
    for x in range (5):
        drawPetal(size,petalColor)
        turtle.left(120) # this is so the trutle faces the right direction
        turtle.forward(size)
        turtle.right(60)
    drawPetal(size, petalColor)
    turtle.left(120)
    drawPetal(size, centerColor)
    turtle.end_fill()

def main():
    """this is the main function that fully draws your flower"""
    turtle.speed(3)
    sideLength= getSideLength()
    centerColor= getCenterColor()
    petalColor= getPetalColor()
    drawHexagon(sideLength, centerColor, petalColor)
    turtle.done()

main()
