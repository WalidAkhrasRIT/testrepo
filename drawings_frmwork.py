import turtle

PIXEL_SIZE = 30 # This is the size of the pixel
ROWS = 20 # The size of the rows
COLUMNS = 20 # The size of the columns



def Initialization():
    """This function initializes the turtle state where it begins to draw."""
    turtle.up()
    turtle.speed(0)
    turtle.pensize(1)
    turtle.goto(-300,300)
    turtle.pencolor('black')
    turtle.fillcolor('white')

def draw_black_pixel(): 
    """This function creates a single black pixel.""" 
    turtle.fillcolor("black")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)


def draw_white_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("white")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)


def draw_red_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("red")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def draw_yellow_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def draw_orange_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("orange")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def draw_green_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("green")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill() 
    turtle.forward(PIXEL_SIZE)

def draw_yellowgreen_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("yellowgreen")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def draw_sienna_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("sienna")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def draw_tan_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("tan")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def draw_gray_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("gray")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)


def draw_darkgray_pixel():
    """This function creates a single black pixel.""" 
    turtle.fillcolor("darkgray")
    turtle.begin_fill()
    for y in range(4): #The loop used to make the square
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)


def draw_Color(col):
    """This Function was creared for question number 4 in which is creates a string of color pixel by 
    pixel depending on the string variable given."""
    for c in col: # Creates a loop to draw a certain amount of pixels
        if c=="0":
            draw_black_pixel()
        elif c=="1":
            draw_white_pixel()
        elif c=="2":
            draw_red_pixel()
        elif c=="3":
            draw_yellow_pixel()
        elif c=="4":
            draw_orange_pixel()
        elif c=="5":
            draw_green_pixel()
        elif c=="6":
            draw_yellowgreen_pixel()
        elif c=="7":
            draw_sienna_pixel()
        elif c=="8":
            draw_tan_pixel()
        elif c=="9":
            draw_gray_pixel()
        elif c=="A":
            draw_darkgray_pixel()
        else:
            print("Invalid color")
            break



def input_color():
    """This function is created for question number 5 using the previous function in number 4, it prompts the user to enter the
    sring of color that will be generated pixel by pixel."""
    Initialization()
    while (True): # This loop is used to continously prompt the user to draw strings of colored pixels
        color= input('Enter color strings using numbers between 1-9 and "A": ') # The input variable that is given by the user
        draw_Color(color) # previous function
        turtle.up()
        turtle.goto(-300,turtle.ycor()-PIXEL_SIZE) #Used to start drawing in a new line
        turtle.down()
    
def square_row():
    turtle.down()
    for j in range(ROWS):
        for x in range(COLUMNS):
            for y in range(4):
                turtle.forward(PIXEL_SIZE)
                turtle.right(90)
            turtle.forward(PIXEL_SIZE)
        turtle.up()
        turtle.goto(-300,turtle.ycor()-PIXEL_SIZE) 
        turtle.down()

def Pixart():
    """This function is used to draw pixart from other files. The function opens a file that is given by the user,
    the file contains the data/text that will be ran by this code to create such drawings."""
    Initialization()
    file= input("Enter the file you want to draw: ")
    with open(file) as my_file: # The function used to open other files in a computer
        for l in my_file:
            for c in l:
                if c=="0":
                    draw_black_pixel()
                elif c=="1":
                    draw_white_pixel()
                elif c=="2":
                    draw_red_pixel()
                elif c=="3":
                    draw_yellow_pixel()
                elif c=="4":
                    draw_orange_pixel()
                elif c=="5":
                    draw_green_pixel()
                elif c=="6":
                    draw_yellowgreen_pixel()
                elif c=="7":
                    draw_sienna_pixel()
                elif c=="8":
                    draw_tan_pixel()
                elif c=="9":
                    draw_gray_pixel()
                elif c=="A":
                    draw_darkgray_pixel()
                else:
                    print("Invalid color")
                    break
            turtle.up()
            turtle.goto(-300,turtle.ycor()-PIXEL_SIZE) #Used to start drawing in a new line
            turtle.down()


Pixart()
turtle.done()