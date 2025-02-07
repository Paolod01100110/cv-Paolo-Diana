# Richiede l'età dell'utente
eta = int(input("Inserisci la tua età: "))

# Controlla se l'età è maggiore o uguale a 18
if eta >= 18:
    print(f"Benvenuto utente di {eta} anni!")
else:
    print("Accesso negato.")

email_list = [] #lista per memorizzare le mail già registrate

while True:
    print("\n **Benvenuto nel sistema di accesso** ")
    print("1. Accedi")
    print("2. Registrati")
    print("3. Esci")

    scelta = input("Scegli un'opzione (1/2/3): ")

    if scelta == "1":  # ACCESSO
        email = input("Inserisci la tua email: ")

        if email in email_list:
            print(f"\n Accesso effettuato con successo! Bentornato {email}.")
            break  # Interrompe il ciclo e permette l'accesso
        else:
            print(" Email non registrata. Devi prima registrarti.")

    elif scelta == "2":  # REGISTRAZIONE
        email = input("Inserisci una nuova email per registrarti: ")

        if email in email_list:
            print(" Questa email è già registrata. Torna alla schermata di accesso.")
        else:
            email_list.append(email)  # Aggiunge l'email alla lista
            print(f" Registrazione completata! Ora puoi accedere con l'email {email}.")

    elif scelta == "3":  # USCITA
        print(" Uscita dal sistema. Arrivederci!")
        break  # Termina il programma

    else:
        print(" Opzione non valida. Riprova.")

# Lista delle email registrate
email_list = ["utente1@example.com", "utente2@example.com", "utente3@example.com"]

# Assegna ID agli utenti usando range()
print("\n🔹 Lista utenti registrati:")

for user_id in range(1, len(email_list) + 1, 1):  # Parte da 1, si ferma dopo l'ultimo utente, incrementa di 1
    print(f"ID {user_id}: {email_list[user_id - 1]}")



