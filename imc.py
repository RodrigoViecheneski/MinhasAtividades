paciente = input("Nome do paciente:.. ")
pc = float(input("Peso Corporal(kgs): "))
alt = float(input("Altura (m).......: "))

vlr_IMC = pc / (alt ** 2)

if(vlr_IMC < 18.5):
    print(f"Paciente: {paciente} - IMC: {vlr_IMC:.2f} - Abaixo do peso")
elif(vlr_IMC >= 18.5 and vlr_IMC < 25):
    print(f"Paciente: {paciente} - IMC: {vlr_IMC:.2f} - Peso normal")
elif(vlr_IMC >= 25 and vlr_IMC < 30):
    print(f"Paciente: {paciente} - IMC: {vlr_IMC:.2f} - Sobrepeso")
else:
    print(f"Paciente: {paciente} - IMC: {vlr_IMC:.2f} - Obesidade")