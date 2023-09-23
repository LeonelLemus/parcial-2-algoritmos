
mail = input("Ingrese un mail:") # Dejar solo un = para asignar el valor
cantidad = 0 # Dejar un solo signo igual y asignarle un valor inicial
x = 0       #Quitar un signo igual
while x<len(mail): # La variable leng es incorrecta debe ser len
 if mail[x] == "@": #Debe ser doble igual para comparar
  cantidad = cantidad+1
x = x+1 #Quitar un signo +, solo debe quedar x= x+1
if cantidad== 1: #Falto ponerle 2 puntos al final
 print("Contiene solo un caracter @ el mail ingresado") #No estaba cerrado el parentesis
else:
 print("incorrecto") #Faltaba una comilla
