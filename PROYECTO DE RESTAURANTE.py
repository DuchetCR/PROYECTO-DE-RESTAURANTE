'''
Universidad Fidelitas
Programacion Basica
PROYECTO DE RESTAURANTE
KENNETH RUBI Y VALERIA RODRIGUEZ
09-11
Version 2.1
'''
Alimento_lista=[]
Bebida_lista=[]
Postre_Lista=[]
def Menu_principal():
    print("***************************")
    print("Bienvenido a Xpress")
    print("Menu Principal")
    print("1. Menu")
    print("2. Precio de envio")
    print("3. Datos y Factura")
    print("0. Salir")
    opcion = int(input("Elija una opcion: "))
    print("***************************")
    if opcion == 1:
        Menu_de_Comidas()
    elif opcion == 2:
        Distacia_calculo()
    elif opcion==3:
        Facturacion()
    elif opcion == 0:
        print("Gracias por usar el programa")
        import sys
        sys.exit()

def Menu_de_Comidas ():
    global Suma_de_costo
    Suma_de_costo=0
    global Suma_de_bebida
    Suma_de_bebida = 0
    global Suma_de_Postres
    Suma_de_Postres = 0
    print("***************************")
    CatidadComidas=int(input("Cuantas comidas le gustaria pedir: "))
    if CatidadComidas == 0:
        Costo = 0
        Alimento = "No solicito"
        Alimento_lista.append(Alimento)
    else:
        for i in range (CatidadComidas):
            print("***************************")
            print("1. Hamburguesa")
            print("2. Tacos")
            print("3. Papas")
            print("4. Nachos")
            print("5. Nuggets")
            print("6. Pizza")
            print("***************************")
            Comida = int(input("Elija una opcion: "))

            if Comida == 1:
                Costo = 1500
                Alimento="Hamburguesa"
                Alimento_lista.append(Alimento)
                Suma_de_costo =Suma_de_costo+Costo
            elif Comida == 2:
                Costo = 2500
                Alimento="Tacos"
                Alimento_lista.append(Alimento)
                Suma_de_costo =Suma_de_costo+Costo
            elif Comida == 3:
                Costo = 1500
                Alimento="Papas"
                Alimento_lista.append(Alimento)
                Suma_de_costo =Suma_de_costo+Costo
            elif Comida == 4:
                Costo = 4000
                Alimento="Nachos"
                Alimento_lista.append(Alimento)
                Suma_de_costo =Suma_de_costo+Costo
            elif Comida == 5:
                Costo = 3500
                Alimento="Nuggets"
                Alimento_lista.append(Alimento)
                Suma_de_costo =Suma_de_costo+Costo
            elif Comida == 6:
                Costo = 5000
                Alimento="Pizza"
                Alimento_lista.append(Alimento)
                Suma_de_costo =Suma_de_costo+Costo
    print("***************************")
    CatidadRefresco = int(input("Cuantas bebidas le gustaria pedir: "))
    if CatidadRefresco == 0:
        Costo_bebida = 0
        Bebida = "No solicito"
        Bebida_lista.append(Bebida)
    else:
        for i in range(CatidadRefresco):
            print("***************************")
            print("1. Coca-Cola")
            print("2. Fanta Naranja")
            print("3. Fanta Uva")
            print("4. Fanta Kolita")
            print("5. Pepsi")
            print("6. Te Melocoton")
            print("***************************")
            Refresco = int(input("Elija una opcion: "))
            if Refresco == 1:
                Costo_bebida = 1100
                Bebida = "Coca-Cola"
                Bebida_lista.append(Bebida)
                Suma_de_bebida = Suma_de_bebida + Costo_bebida
            elif Refresco == 2:
                Costo_bebida = 1200
                Bebida = "Fanta Naranja"
                Bebida_lista.append(Bebida)
                Suma_de_bebida = Suma_de_bebida + Costo_bebida
            elif Refresco == 3:
                Costo_bebida = 1300
                Bebida = "Fanta Uva"
                Bebida_lista.append(Bebida)
                Suma_de_bebida = Suma_de_bebida + Costo_bebida
            elif Refresco == 4:
                Costo_bebida = 1400
                Bebida = "Fanta Kolita"
                Bebida_lista.append(Bebida)
                Suma_de_bebida = Suma_de_bebida + Costo_bebida
            elif Refresco == 5:
                Costo_bebida = 1500
                Bebida = "Pepsi"
                Bebida_lista.append(Bebida)
                Suma_de_bebida = Suma_de_bebida + Costo_bebida
            elif Refresco == 6:
                Costo_bebida = 1600
                Bebida = "Te Melocoton"
                Bebida_lista.append(Bebida)
            Suma_de_bebida = Suma_de_bebida + Costo_bebida
    print("**************************************************")
    CatidadPostres = int(input("Cuantos Postres le gustaria pedir: "))
    if CatidadPostres == 0:
        Costo_Postres = 0
        Postre = "No solicito"
        Postre_Lista.append(Postre)
    else:
        for i in range(CatidadPostres):
            print("***************************")
            print("1. Queque")
            print("2. Helado")
            print("3. Milkshake")
            print("4. Brownie")
            print("5. Tarta de frambuesa y queso crema")
            print("6. Natillas caramelizadas")
            print("***************************")
            Postres = int(input("Elija una opcion: "))
            if Postres == 1:
                Costo_Postres = 1000
                Postre = "Queque"
                Postre_Lista.append(Postre)
                Suma_de_Postres = Suma_de_Postres + Costo_Postres
            elif Postres == 2:
                Costo_Postres = 700
                Postre = "Helado"
                Postre_Lista.append(Postre)
                Suma_de_Postres = Suma_de_Postres + Costo_Postres
            elif Postres == 3:
                Costo_Postres = 1500
                Postre = "Milkshake"
                Postre_Lista.append(Postre)
                Suma_de_Postres = Suma_de_Postres + Costo_Postres
            elif Postres == 4:
                Costo_Postres = 2500
                Postre = "Brownie"
                Postre_Lista.append(Postre)
                Suma_de_Postres = Suma_de_Postres + Costo_Postres
            elif Postres == 5:
                Costo_Postres = 3500
                Postre = "Tarta de frambuesa y queso crema"
                Postre_Lista.append(Postre)
                Suma_de_Postres = Suma_de_Postres + Costo_Postres
            elif Postres == 6:
                Costo_Postres = 3000
                Postre = "Natillas caramelizadas"
                Postre_Lista.append(Postre)
            Suma_de_Postres = Suma_de_Postres + Costo_Postres

    Menu_principal()

def Distacia_calculo():
    global Envio
    Envio=0
    print("***************************")
    print("Eliga la provincia de destino")
    print("1. Heredia")
    print("2. San jose")
    print("3. Alajuela")
    print("0. Salir")
    print("***************************")
    Destino=int(input("Elija una opcion: "))
    if Destino == 1:
        Envio=2000
        print("El precio de envio es", Envio)
    if Destino == 2:
        Envio = 3000
        print("El precio de envio es", Envio)
    if Destino == 3:
        Envio = 4000
        print("El precio de envio es", Envio)
    elif Destino == 0:
        print("Volviendo al menu Principal")
    Menu_principal()
    return Envio

def crearFactura():
    print("**************************************")
    file=open("Factura.txt", "w")
    print("La factura esta lista para guardar informacion")
    print("**************************************")

def Facturacion():
    global Suma_de_costo
    global Envio_final
    global Suma_de_bebida
    crearFactura()
    nombreContacto=input("Digite el nombre: ")
    telefono=input("Digite el celular: ")
    Direcion=input("Digite la direcion exacta de Envio: ")
    total=Suma_de_costo+Envio+Suma_de_bebida+Suma_de_Postres
    file=open("Factura.txt", "a")
    file.write('Factura')
    file.write("\n")
    file.write('SISTEMA XPRESS')
    file.write("\n")
    file.write('Cedula juridica 3 102 808095')
    file.write("\n")
    file.write('Sede Heredia')
    file.write("\n")
    file.write('***************************************')
    file.write("\n")             
    file.write('Nombre facturacion: % s' %nombreContacto)
    file.write("\n")
    file.write('Telefono facturacion: % s' %telefono)
    file.write("\n")
    file.write('Direcion exacta: % s' %Direcion)
    file.write("\n")
    file.write('Su Comidas son =%s' %Alimento_lista)
    file.write("\n")
    file.write('Su Bebidas son =%s' % Bebida_lista)
    file.write("\n")
    file.write('Su Postres son =%s' % Postre_Lista)
    file.write("\n")
    file.write('Total de comida es: % s' % Suma_de_costo)
    file.write("\n")
    file.write('Total de bebida es: % s' %Suma_de_bebida)
    file.write("\n")
    file.write('Total de Postres es: % s' % Suma_de_Postres)
    file.write("\n")
    file.write('Total del envio % s'%Envio)
    file.write("\n")
    file.write('Total a cancelar % s' %total)
    file.write("\n")
    file.write('***************************************')
    file.write("\n")         
    file.write('Gracias por utilizar Xpress Sistema')
    print("\nLa facturacion ha cerrado exitosamente")
    print("**************************************")
    file = open("Factura.txt", "r")
    mostrar()

def mostrar():
    print("**************************************")
    file=open("Factura.txt", "r")
    lectura=file.read()
    print(lectura)
    print("**************************************")
    import sys
    sys.exit()

def Inicio():
    for i in range (3):
        Usuario = input("Usuario: ")
        Password = input("Password: ")
        if Usuario == "Kenneth" and Password == "Rubi_22" or "Valeria" and Password == "Rodriguez_22":
            Menu_principal()
        elif i < 2:
            print("Usuario rechazado, Intenta nuevamente ")
        elif i==2:
            print("Usuario Bloquedo, vuelve a intentar mas tarde")

Inicio()