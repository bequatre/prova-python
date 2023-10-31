print("Hola mundo!")

# Variables
texto = "Clase de Python"
nombre = "Jordi"
altura = "185cm"
year = 2023

# Concatenar (Se puede hacer de las dos formas)
print(f"{texto} - {nombre} - {altura} - {str(year)}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

# Entrada
"""
sitioweb = input("¿Cúal es tu página web?")
print("Tu página web es: " + sitioweb)
"""

# Condiciones
"""
altura = int(input("¿Cúal es tu altura?: "))

if altura >= 180:
    print("Eres muy alto!")
else:
    print("No te veo desde aquí arriba...")
"""

# Funciones

def mostrarAltura():
    altura = int(input("¿Cúal es tu altura?: "))

    if altura >= 180:
        print("Eres muy alto!")
    else:
        print("No te veo desde aquí arriba...")

mostrarAltura()
mostrarAltura()
mostrarAltura()