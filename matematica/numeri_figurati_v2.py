#Numeri figurati


#Importa le librerie
import math

#Titolo
print "***************************"
print "***** Numeri Figurati *****"
print "***** Giorgio Abbadessa ***"
print "***************************"

#Funzione disegno quadrati perfetti
def fig_quad(radice_quad):
    for x in range(int(radice_quad)):
        figq = ['x']*int(radice_quad)
        print figq


def test_triang(n):
    x = (math.sqrt(8*n + 1) - 1) / 2
    if x == int(x):
        print "Il n e' TRIANGOLARE"


#Loop del programma
while True:

    #Richiestra numero da disegnare
    n = 0
    while n == 0:
        n = input ("Numero  ")
        if n == 0:
            print "Tranne lo 0(zero)"



    #Pari
    if n%2 == 0:
        print "Il n e' il PARI",n/2
        figp_r1 = ['x']*(n/2)
        figp_r2 = figp_r1[:]
        print figp_r1
        print figp_r2

    #Dispari
    if n%2 != 0:
        print "Il n e' il DISPARI", ((n/2)+1)
        figd_r1 = ['x']*(n/2)
        figd_r2 = ['x']*((n/2)+1)
        print figd_r1
        print figd_r2

    #Quadrati
    radice_quad = math.sqrt(n)
    if radice_quad == int(radice_quad):
        print "Il n e' il QUADRATO", int(radice_quad)
        print
        fig_quad(radice_quad)

    #Triangolari
    test_triang(n)
    
        
    print
    print
    
