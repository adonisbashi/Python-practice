''' 
def number_squared(number):
    print(number**2)

x = int(input("What number would you like to square? "))

number_squared(x)
'''

'''
def number_squared_cust(number, power):
    print(number**power)

number = float(input("What number would you like to add a power to? "))
power = float(input("What power would you like to set it to? "))
number_squared_cust(number, power)
'''

'''
args_tuple = (5,6,1,2,8)

def number_args(*number):
    print(number[0]*number[1])

number_args(*args_tuple)
'''

'''
def number_kwarg(**number):
    print("My number is: " + number["interger"] + " My other number is: " + number["interger2"])

number_kwarg(interger = "2309", interger2 = "349")
''' 

x = int(input("Whats x? "))
y = int(input("Whats y? "))

if x < y:
    print("x is less than y")
elif x == y: print("x is equal to y")
else: print("x is greater than y")
