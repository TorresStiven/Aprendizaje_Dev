# for numero in range(5):
#     print(numero)

# for palabra in range(3):
#     print(palabra, palabra * "Hola")

buscar = 6
for numero in range(5):
    if numero == buscar:
        print("Lo encontré", buscar)
        break
else:
    print("no encontrado :(")


for char in "ultimate python":
    print(char)