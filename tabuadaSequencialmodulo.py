def tabuada(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
    print()
    
#módulo principal (main)
t = int(input("Qual tabuada você quer? "))
tabuada(t)