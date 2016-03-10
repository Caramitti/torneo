import random

partecipanti=int(input("Numero di pertecipanti: "))
err=partecipanti//2
while partecipanti%2!=0 or err%2!=0:
    print ("La versione del programma permette solo un numero di partecipanti pari e che divisi per due siano ancora pari!")
    partecipanti=int(input("Numero di pertecipanti: "))
    err=partecipanti//2
indice = 0
dom=1
nomi=[]
# SCELTA PARTECIPANTI
for x in range(partecipanti):
    sdom=str(dom)
    dom1="nome del giocatore n." + sdom +": "
    nome=input(dom1)
    nomi[indice:indice]=[nome]
    indice = indice + 1
    dom=dom+1
print (nomi)
indice=0
scelti=[]
passa=False
# DISTRIBUZIONE DEI PARTECIPANTI
for x in nomi:
        ordine=random.choice(range(partecipanti))
        if passa==True:
            while scelti[ordine:ordine]=="":
                ordine=random.choice(range(partecipanti))
        scelti[ordine:ordine]=[x]
        indice=indice+1
        passa=True

# ORGANIZZAZIONE TORNEO
scelta=0
indice=0
nu=partecipanti//2
barra=1
for a in range(nu):
        giocatori=[]
        primo=scelti[indice]
        giocatori[scelta:scelta]=[primo]
        indice=indice+1
        scelta=1
        secondo=scelti[indice]
        giocatori[scelta:scelta]=[secondo]
        indice=indice+1
        scelta=0
        if barra%2==0:
            barr="\t /"
        else:
            barr= "\t \ "
        printa= str(giocatori)
        print (printa + barr )
        barra=barra+1
        secondo=scelti[indice]
        giocatori[scelta:scelta]=secondo
        indice=indice+1
        scelta=0
        if barra%2==0:
            barr=" /"
        else:
            barr= " \ "
        printa= str(giocatori)
        print (printa + barr )
        barra=barra+1
