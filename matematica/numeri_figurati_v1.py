#Numeri figurati
print "***** Numeri Figurati *****"

while True:

    #Richiestra numero da disegnare
    n = 0
    while n == 0:
        n = input ("Numero  ")
        if n == 0:
            print "Tranne lo 0(zero)"



    #Pari
    if n%2 == 0:
        print "Il n e' P",n/2
        figp_r1 = ['x']*(n/2)
        figp_r2 = figp_r1[:]
        print figp_r1
        print figp_r2

    #Dispari
    if n%2 != 0:
        print "Il n e' D", ((n/2)+1)
        figd_r1 = ['x']*(n/2)
        figd_r2 = ['x']*((n/2)+1)
        print figd_r1
        print figd_r2


    print
    print
    
    
    
    
    



