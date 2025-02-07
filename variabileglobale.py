#variabile globaleù
numero = 10

def funzione esterna()
    #variabile locale nella funzione esterna
    numero = 5
     
     def funzione interna ():
        #UTILIZZO NONLOCAL PER MODIFICARE LA variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print ("numero dentro fiunzione_interna")