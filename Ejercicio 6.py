#Escribir un programa que lea un entero positivo, n, introducido por el usuario y despues muestre en pantalla la suma de todos los enteros desde 1 hasta n.
#La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma 

n = int(input("Digite un numero: "))

suma = n * (n+1)/2

print("La suma de los primeros numeros enteros desde 1 hasta " + str(n) + " es " + str(suma))