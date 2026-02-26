def main():
    operator = input("Choose the operators (+, -, *, /): ")
    
    match operator:
        case '+':
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            sum(a, b)
        
        case '-':
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number "))
            sub(a, b)
            
        case '*':
            a = int(input("Enter the first number "))
            b = int(input("Enter the second number "))
            mul(a, b)
            
        case '/':
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            div(a, b)
            
        case _:
            print("Invalid operator sign!")
             
             
def sum(a, b):
    x = a + b
    print("Sum : ", x)
    
    
def sub(a, b):
    x = a - b
    print("Subtraction : ", x)
    
def mul(a, b):
    x = a * b
    print(f"multiplication of {a} and {b} is {x}")
    
def div(a, b):
        x = a / b
        print("division : ", x)

main()