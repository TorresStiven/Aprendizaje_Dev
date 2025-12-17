print ("Bienvenido a la calculadora Python")
print ("Ingrese 'salir' para terminar")
print ("Operaciones disponibles: suma, resta, multiplicacion, division")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese un numero: ")
        if resultado.lower() == "salir":
            break
    op = input ("ingresa una operación: ")
    if op.lower() == "salir":
        break
    n2 =  input("ingresa el soguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int (n2)

    if op.lower() == "suma":
        resultado = int (resultado) + n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print ("Operación no reconocida")
        break
    print(f"El resultado es: {resultado}")