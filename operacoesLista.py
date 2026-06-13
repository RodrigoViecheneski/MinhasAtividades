a = [int(item) for item in input().split(" ")]
print()
item = int(input("Item a ser procurado: "))

print()

print(a)
print("Soma =", sum(a))
print("Média =", sum(a) / len(a))
print("Menor =", min(a))
print("Maior =", max(a))

print()
b = a.count(item)

if(b == 1):
    print(f"O item {item} existe {a.count(item)} vez na lista.")
elif(b != 1 and b > 0 ):
    print(f"O item {item} existe {a.count(item)} vezes na lista.")
elif(b == 0):
    print(f"O item {item} não foi encontrado.")