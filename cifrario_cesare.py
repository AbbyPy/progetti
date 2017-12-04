import sys, string

print "\ncifrario di cesare\ngiorgio abbadessa\nAbbyPy"

try:
    chiave = input("chiave: ")

except NameError:
    print "Ops, non hai inserito un numero"
    sys.exit()

alf_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't', 'u', 'v', 'z']* (int(chiave)+10)

alf_2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
         '', '', '', '', '']


x = 0
y = 0
z = 0



for x in range (21):
    alf_2[x] = alf_1[x+chiave]


testo = []
testo = raw_input ("testo: ")

finale = ['']* (len(testo))


for y in range(len(testo)):

    for z in range (21):
        if testo[y] == alf_1[z]:
            finale[y] = alf_2[z]

print
print string.join(finale)
