#Maru Puran
#September 28, 2023
#predict what will happen when mathematical expressions are used in code alongside variables


# Add comments to this code to predict what it will do.
print(8 + 2) #it'll print the result of 10 on the screen from 8 plus 2

print( 8 - 2) #it'll print the result of 6 on the screen from 8 minus 2

print(8 * 2) #it'll print the result of 16 on the screen from 8 times 2

print(10 / 4) #it'll print the result of 2.5 on the screen from 10 divided by 4
 
print(10 // 4) #it'll print the result of 2 on the screen from 10 divided by 4 w/o the decimal

# This code uses variables in place of numbers in the calculation.  Add comments to explain how it works.

num1 = 20 #assign the value of 20 to num1 variable created
num2 = 5 #assign the value of 5 to num2 variable created

result = num1 * num2 #multiples 20 and 5, the values assigned to the variables num1 and num2(it calls the variables, therefore the numbers), assigning the value to the created variable result (100)

print(result) #prints the result variable, which is 100

# This code uses input to assign data into a variable.  Add comments to explain how it works.
print("Enter a number") #prints the words "enter a number" for the viewer on the output screen
num1 = int(input()) #lets user input a number, changes it from a string (default) to a number (integer) and assigns to a variable num1, erasing the previous value of 20
num2 = 2 #assigns value 2 to num2, erasing the previous value of 5

result = num1 // num2 #result, integer from when the number user inputs is divided by 2 (num2) because it puts 2.5 however it only prints the integer, 2

print(result) #prints the result on screen for user to see, 2 