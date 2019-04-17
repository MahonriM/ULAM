numero=int(input("\tIngresa un numero y te mostrare la sucesion ulam"))
if numero>0:
  while int (numero!=1):
   div=numero%2
   if (div ==0):
     numero=numero/2
     print(numero)
   else:
    numero=numero*3+1
    print(numero)


