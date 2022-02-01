num1 = 42 #Declaring a Variable, Assigning a Number to a variable
num2 = 2.3 #Declaring a Variable, Assigning an integer to a variable
boolean = True #Setting a Primitive Data Type Disc as a variable, Assigning a boolean to a variable
string = 'Hello World' #Setting Primitive Data Type Desc. as Variable, Assigning a string of data to that variable
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {
    'name': 'John', #Variable assigned to index, value assigned to variable.
    'location': 'Salt Lake', 
    'age': 37, 
    'is_balding': False #value is boolean
    }
fruit = ('blueberry', 'strawberry', 'banana') #Variable Declared, Values assigned to tuple index. 
"""
Above code:
Declares three variables, assigns
Line 5 is a Composite Data Type: Normal 'List' values assigned to variable
Line 7-10 is a Composite Data Type: Dictionary assigned to a variable
Line 12 is a tuple, values within this list cannot be changed. 
"""
print(type(fruit)) #calling function with function argument assigned, Object for Data Type in question referenced
print(pizza_toppings[1]) #calling function, refers to data object regular list class.
pizza_toppings.append('Mushrooms') #calling add value function referencing list class data type, argument assigned to function
print(person['name']) #calling function, dictionary data class called with argument assigned for specificity within its index
person['name'] = 'George' #dictionary variable referenced, assigned a new string value to that variable within dictionary index
person['eye_color'] = 'blue' #dictionary variable referenced, assigned a new string value to that variable within dictionary index
print(fruit[2]) #call function in reference to index 2 of tuple data object.
if num1 > 45: #First conditional value references variable, if greater than value run code on the next line.
    print("It's greater") #calling function, argument for function
else: #conditional, run the next line of code if preceding conditions are false.
    print("It's lower") #calls a function and assigns an argument to base output on. 
if len(string) < 5: #conditional, function of primitive data type references first value, if less than will run next line.  
    print("It's a short word!") #call function and assigns argument to base output on. 
elif len(string) > 15: #conditional, function of primitive data type references first value, if greater than will run next line.
    print("It's a long word!") #call function and assigns argument to  base output on. 
else: #conditional, run the next line of code if preceding conditions are false.
    print("Just right!") #Call Function, Parameter is a primitive data type: String
for x in range(5): #for loop start, call function, set stop for functions
    print(x) #function, parameter is variable with list of numbers assigned to its index per parameter from range function, loop till end
for x in range(2,5): #for loop start, function called, set start and end for functions
    print(x) #function called, paramter is variable assigned per previous line of code, loop till end
for x in range(2,10,3): #for loop start, function called, start, stop and step parameters set for function.
    print(x) #Function, parameter is varible assigned per previous line, loop till end. 
x = 0 #call existing varaible, set to primitive number.
while(x < 5): #While loop start, parameters set: Variable, Comparative Operative, primitive number limit
    print(x) #function parameter value based on value of variable per previous lines of code
    x += 1 #variable increases (Operative)

pizza_toppings.pop() #variable called (Composite Data Type: regular list), function, parameter is last index value.
pizza_toppings.pop(1) #variable called (Composite Data Type: regular list), function, parameter is value in index per primititve number

print(person) #function, list value from dictionary variable. 
person.pop('eye_color') #dictionary variable, function, parameter for function is string object assigned to index of dictionary.  
print(person) #function, parameter is dictionary variable. 

print(pizza_toppings)
for topping in pizza_toppings: #for loop start, assigns variable to values from list in eaches. 
    if topping == 'Pepperoni': #conditional, variable, operative (equal to) string parameter
        continue #conditional, if previous line is true...
    print('After 1st if statement') #function, parameter set to function is a primitive string
    if topping == 'Olives': #conditional, variable, operative (equal to) string parameter
        break #for loop conditional for end. 

def print_hello_ten_times(): #python keyword for creating a function, function
    for num in range(10): #for loop start, variable, function and parameter end for function. 
        print('Hello') #function, parameter is primitive string object
#lines 64-65 assigned to function 
print_hello_ten_times() #function called.

def print_hello_x_times(x): #create a function, function set
    for num in range(x): #for loop start, variable, function for variable with variable end.
        print('Hello') #function, parameter is a primitive string object

print_hello_x_times(4) #function is called, paramater per line 70 function parameter (for range)

def print_hello_x_or_ten_times(x = 10): #create a function,
    for num in range(x): #for loop start, variable created, function set to variable with variable parameter
        print('Hello') #function, primitive string object parameter

print_hello_x_or_ten_times() #function called.
print_hello_x_or_ten_times(4) #function is called, paramater per line 76 function parameter (for range)
