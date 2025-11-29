n1 = input ("Ingrese el primer número: ")
n2 = input ("Ingrese el segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
      Para los múmeros {n1} y {n2}, 
      los resultados son:
      Suma: {suma}
      Resta: {resta}
      Multiplicación: {multiplicacion}
      División: {division}
      """

print(mensaje)