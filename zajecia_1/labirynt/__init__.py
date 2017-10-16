plik = open("labirynt0.txt")
znak = plik.readlines()
dlugosc = int(znak[0][0:2])
szerokosc = int(znak[0][3:5])
#print dlugosc 
#print szerokosc
poczatek = "@"
koniec = "$"

for i in xrange(1,dlugosc+1):
    for x in xrange(szerokosc):
        print znak[i][x]
        if znak[i][x]==poczatek:
            print "znalazlem"
            if x+1<=szerokosc and znak[i][x+1]=='#':
                    if [x-1]>=szerokosc and znak[i][x+1]=='#':
                        pass         
