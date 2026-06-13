a = int(input("a: "))
b = int(input("b: "))

soma = a + b
sub = a - b
mult = a * b
if(b != 0):
    div = a / b  
    divInt = a // b
    resto = a % b
else:
    div = 0
    divInt = 0
    resto = 0
pot = a ** b    
print("----------------------")
print("Soma........:", soma)
print("Subtração....:", sub)    
print("Multiplicação:", mult)
print("Divisão......:", div)    
print("Divisão Int..:", divInt)
print("Resto........:", resto)
print("Potenciação..:", pot)
print("----------------------")
print(f"{a} + {b} = {soma} ")
print(f"{a} - {b} = {sub} ")
print(f"{a} * {b} = {mult} ")
print(f"{a} / {b} = {div:.2f} divisão real ")
print(f"{a} // {b} = {divInt} divisão inteira")
print(f"{a} % {b} = {resto} resto da divisão ")
print(f"{a} ** {b} = {pot} ")



