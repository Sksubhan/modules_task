from basic_math import addition,subtract,multiply,divide

a,b=map(int,input("Enter the digits a and b :").split())
print(addition(a,b))
print(subtract(a,b))
print(multiply(a,b))
print(f'{divide(a,b):.2f}')