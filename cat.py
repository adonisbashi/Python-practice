## While loops

'''
i = 0
while i < 3:
    print("meow")
    i += 1
'''

## For loops

## A single _ variable = unnecessary name, only for the function
'''
for _ in range(3):
    print("meow")
'''

## Infinite 'while True' loops
'''
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
'''

'''
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
'''