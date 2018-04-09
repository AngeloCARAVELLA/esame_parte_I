# Utilizzando il inguaggio python determinare la durata massima di un volo 
# di un areoplano dati in input la quantita' di carburante (in galloni)
# e il consumo orario (in galloni/h).
# Il programma tenga conto di eventuali input negativi 
# In tal caso stampi un opportuno messaggio di errore 

#stampe
print "voglio determinare la durata massima di un volo" 
print "con in input la quanita' di carburante e il consumo orario"
print "tenendo conto di eventuali input negativi" 

#input 
consumo_h = raw_input (" inserisci il consumo orario in galloni")
carburante = raw_input ("inserisci il carburante a disposizione")

#casting in float e salvo nelle variabili di lavoro  
consumo_h  =  float (consumo_h)
carburante =  float (carburante)
 
if carburante < 0:
    print "La quantita' di carburante non puo' essere negativa!"
elif consumo_h <= 0:
    print "Il consumo orario deve essere positivo!"
else:
# tempo di volo
        t = carburante / consumo_h 
# ore intere
        ore = int(t)

        # minuti restanti
        t = t - ore
        t = t*60 
# minuti interi
        minuti = int(t)

# secondi restanti
        t = t - minuti
        t = t*60 
        secondi = int(t)# secondi interi

        print "Durata volo:", ore, "h", minuti, "min", secondi, "sec"
