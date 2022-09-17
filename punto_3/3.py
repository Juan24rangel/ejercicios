# No.3 : Determinar si un triangulo es equilatero, isoceles o escaleno.

print("-----------------------------------")
print("---------------LADOS---------------")
print("-----------------------------------")

# input
a = int(input("Digite el lado a:"))
b = int(input("Digite el lado b:"))
c = int(input("Digite el lado c:"))

# processing
if a==b and a==c:
    t = ("es un triangulo equilatero")
else:
    if a==b and a!=c:
        t = ("es un triangulo isoceles")
    
    else:
        if a!=b and a!=c:
            t = ("es un triangulo escaleno")

#output
print("la figura: " +str(t))