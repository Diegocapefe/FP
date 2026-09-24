edad=int(input("Inserte su edad: "))
nivelFisico=int(input("Inserte su nivel físico 1-10: "))

if edad<18:
    print("Debes ser mayor de edad")
elif nivelFisico <5:
    print("Debes estar en mejor forma")
    
else:
    print("Listo para despegar")
