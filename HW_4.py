def write_polynomial():
    N = int(input("N --> "))
    import random
    z = ""
    stepen = N
    while stepen > 1:
        z = z + (str(random.randint(0, 100))) + "*(x**" + str(stepen) + ") + "
        stepen = stepen-1
    z = z + (str(random.randint(0, 100)))+ "*x + " + (str(random.randint(0, 100))) + " = 0 "
    # Z = str(a) +"x"+"^" str(a) +str(b) + str(c)
    f = open('text.txt', 'w')
    f.write(str(z))
    f.close()

write_polynomial()