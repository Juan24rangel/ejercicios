# No.2: Determinar si un triangulo es recto, agudo u obtuso.

print("-------------------------------------")
print("---------------ANGULOS---------------")
print("-------------------------------------")

# input
a = int(input("Digite el valor del angulo a:"))
b = int(input("Digite el valor del angulo b:"))
c = int(input("Digite el valor del angulo c:"))

# processing
if a<90:
    if b<90:
        if c<90:
            t = ("un triangulo agudo")
else:
    if a>90:
        if b<90:
            if c<90:
                t = ("un triangulo obtuso")
    else:
        if a==90:
            if b<90:
                if c<90:
                    t = ("un triangulo rectangulo")

# output
print("es: "+str(t))