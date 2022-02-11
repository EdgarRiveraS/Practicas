
def switch_demo(argument):
    switcher = {
        1: num1 +num2,
        2: num1 - num2,
        3: num1 * num2,
        4: num1 / num2,
           }
    print (switcher.get(argument, "operación Invalida"))

print ("""Escoje que tipo de opercaión deceas realizar"
Suma 1
Resta 2
Multiplicación 3
divición 4""")
entrada = int(input ("Que operación deceas realizar "))
num1 = int(input("Ahora ingresa el 1er numero "))
num2 = int(input("ahora ingresa el 2do numero "))
switch_demo(abs(entrada))
