# Asad Bhatti
# Ms. Pais
# ICS 4U
# February 11, 2019

def areatriangle (unit,base,height):
    
    area1 = int(base)*int(height)
# Calculates the total area by converting base and height into an integer and multiply them by each other and store into variable "area1"

    area2 = area1/2
# Calculates the final area of the triangle by dividing area1 by 2 and store into variable "area2"

    return print('The area of the triangle is ' + str(area2) + ' ' + unit + '^2.')
# Output message and convert area2 into a string then return value

run = 1

while(run == 1):
    unit = input('What is the unit of measurement you would like to use?: ')
# User inputs a unit of measurement and is stored as a string in the variable "unit"

    base = input('What is the length of the base: ')
# User inputs the base length of the triangle and is stored as a string in the variable "base"

    height = input('What is the hight of the triangle: ')
# User inputs the hight of the triangle and is stored as a string in the variable "height"
    areatriangle(unit,base,height)
# We use the function to calculate the area of a triangle

    leave = input('Would you like to calculate the area of another triangle? Yes or No (Case Sensitive): ')
#Prompt displays messaage and askes if user would like to quit
    if leave == 'No':
        run = 0
# Program ends if user inputs "Yes"
