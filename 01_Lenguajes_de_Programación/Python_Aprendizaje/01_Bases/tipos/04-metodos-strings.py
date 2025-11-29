animal = " chanCHito feliz "
print(animal.upper())  # Convierte el string a mayusculas
print(animal.lower())  # Convierte el string a minusculas
print(animal.title())  # Convierte el string a formato titulo
print(animal.strip().capitalize())  # Elimina espacios al inicio y final, y capitaliza la primera letra
print(animal.split())  # Divide el string en una lista de palabras
print(animal.rsplit())  # Divide el string en una lista de palabras desde la derecha
print(animal.find("CH"))  # Encuentra la posicion de la primera ocurrencia de "CH" 
print(animal.find("nH")) # Encuentra la posicion de la primera ocurrencia de "nH" -1 si no lo encuentra
print(animal.replace("CH", "ch"))  # Reemplaza "CH" por "ch"
print("nCH" in animal)  # Verifica si "nCH" esta en el string, devuelve True o False
print("nCH" not in animal)  # Verifica si "nCH" no esta en el string, devuelve True o False
print(animal.count("ch"))  # Cuenta cuantas veces aparece "ch" en el
print(animal.startswith(" chan"))  # Verifica si el string empieza con " chan"
print(animal.endswith("feliz "))  # Verifica si el string termina con "feliz "
print(animal.center(30, "-"))  # Centra el string en un campo de 30 caracteres, rellenando con "-"
print(animal.ljust(30, "*"))  # Alinea a la izquierda en un campo de 30 caracteres, rellenando con "*"
print(animal.rjust(30, "+"))  # Alinea a la derecha en un campo de 30 caracteres, rellenando con "+"
print(animal.isalpha())  # Verifica si todos los caracteres son alfabeticos
print(animal.isdigit())  # Verifica si todos los caracteres son digitos
print(animal.isspace())  # Verifica si todos los caracteres son espacios
print(animal.encode())  # Codifica el string a bytes
print(animal.count("a"))  # Cuenta cuantas veces aparece "a" en el string
