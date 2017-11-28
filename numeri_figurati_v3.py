# -*- coding: cp1252 -*-
#Numeri figurati


#Importa le librerie
import math

#Titolo
print "+++++++++++++++++++++++++++++++++"
print "--- Giorgio Abbadessa -----------"
print "--- IV D, Liceo Orazio ----------"
print "--- https://github.com/AbbyPy ---"
print "+++++++++++++++++++++++++++++++++"
print

#Funzione disegno QUADRATI
def fig_quad(radice_quad):
    for x in range(int(radice_quad)):
        figq = ['x']*int(radice_quad)
        print figq

#Funzione dei TRIANGOLI
def n_triang(n):
    x = (math.sqrt(8*n + 1) - 1) / 2
    if x == int(x):
        print "Il n è TRIANGOLARE", int(x)
        while x > 0:
            print ['x']*int(x)
            x = x-1

#Funzione degli GNOMONI
def fig_gnom(n):
    for x in range(int(n/2)):
        print ['x']
    print ['x']*((n/2)+1)


#Loop del programma
while True:

    #Richiestra numero da disegnare
    n = 0
    while n == 0:
        n = input ("Numero  ")
        if n == 0:
            print "Tranne lo 0(zero)"
            print



    #PARI
    if n%2 == 0:
        print "------------------"
        figp_r1 = ['x']*(n/2)
        figp_r2 = figp_r1[:]
        print figp_r1
        print figp_r2
        print "------------------"
        print

    #DISPARI
    if n%2 != 0:
        print "------------------"
        print "Il n è il DISPARI", ((n/2)+1)
        figd_r1 = ['x']*(n/2)
        figd_r2 = ['x']*((n/2)+1)
        print figd_r1
        print figd_r2
        print "------------------"
        print
        print "------------------"
        print "Il n è lo GNOMONE", ((n/2)+1)
        fig_gnom(n)
        print "------------------"
        print
        

    #Quadrati
    radice_quad = math.sqrt(n)
    if radice_quad == int(radice_quad):
        print "------------------"
        print "Il n è il QUADRATO", int(radice_quad)
        fig_quad(radice_quad)
        print "------------------"
        print

    #TRIANGOLI
    n_triang(n)
    
        
    print "*****************************"
    print "*****************************"
    print
    
