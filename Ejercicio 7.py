#Escribir un programa que pida al usuario su peso en kg y su estatura en metros, calcule el IMC y lo almacene en una variable
#y muestre por pantalla la frase Tu indice de masa corporal es <imc> donde ims es el indice de masa corporal calculado redondeado con dos decimales

peso = float(input("Digite su peso en kg: "))

estatura = float(input("Digite su estatura en metros: "))

imc = round(float(peso)/float(estatura)**2,2)

print("Tu indice de masa corporal es " + str(imc))

#Round lo que hace es que nos redondea a el numero que ponemos despues de la coma si ponemos el ,4 serian 4 digitos