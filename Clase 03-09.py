operación = input("Ingresar el tipo de operación que deseas ejecutar:(+ - * /)")
num1 = int(input("Ingresa tu primer número:"))
num2 = int(input("Ingresa tu segundo número:"))

if operación == "+":
    print("num1 + num2") 
elif operación == "-":
    print("num1 - num2")
elif operación == "*":
    print("num1*num2")
elif operación == "/":
    print("num1/num2")
else:
    print("La operación es inválida")
