# Determinar un triagulo por sus lados

print("-----------------------------------")
print("---------------LADOS---------------")
print("-----------------------------------")

#input
a = int(input("Digite el valor de a:"))
b = int(input("Digite el valor de b:"))
c = int(input("Digite el valor de c:"))

#processing
if a+b>c:
    t=("si es un triangulo")
else:
    t=("no es un triangulo")
if a+c>b:
    t=("si es un triangulo")
else:
    t=("no es un triangulo")
if b+c>a:
    t=("si es un triangulo")
else:
    t=("no es un triangulo")

#output
print("por ende: "+str(t))