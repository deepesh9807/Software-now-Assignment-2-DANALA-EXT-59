import turtle 

# Function to draw a single edge of the fractal edge
def draw_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else: 
        length_third = length / 3 # divide length into three parts

        draw_edge(t, length_third, depth - 1) # draw the first third
        t.right(60) # turn right 60 degrees to move upward
        draw_edge(t, length_third, depth - 1)
        t.left(120) # turn left 120 degrees to go downward
        draw_edge(t, length_third, depth - 1)
        t.right(60) # turn right 60 degrees to realign direction
        draw_edge(t, length_third, depth - 1) # draw the fourth third (straight)

# Function to draw the complete fractal edge
def draw_polygon(t, sides, side_length, depth): 
    angle = 360 / sides # Calculate the turning angle for the edges 
    for _ in range(sides): 
        draw_edge(t, side_length, depth)
        t.right(angle) #turn right to position for the next side

def main():
    sides = int(input("please Enter the number of sides: ")) 
    side_length = int(input("please Enter the side length: ")) 
    depth = int(input("please Enter the recursion depth: ")) 

    screen = turtle.Screen() 
    screen.bgcolor("white") # Set background color to white
    t = turtle.Turtle() 
    t.speed(0) # Set the turtle speed to maximum
    t.penup() # Lift the pen to move without drawing
    t.goto(-side_length/2, side_length/2) # Move turtle to starting position
    t.pendown() # Put the pen down to start drawing

    draw_polygon(t, sides, side_length, depth)

    t.hideturtle() # Hide the turtle after drawing
    turtle.done() # Finish the drawing and wait for user action
# Run the main function
main()