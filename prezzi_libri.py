def calcola_prezzo_finale(prezzo_libro, num_copie, sconto):
    if num_copie > 3:
        prezzo_scontato = prezzo_libro * num_copie * (1 - sconto / 100)
    else:
        prezzo_scontato = prezzo_libro * num_copie
    return prezzo_scontato

prezzo_libro = float(input("Inserisci il prezzo del libro: "))
num_copie = int(input("Inserisci il numero di copie: "))
sconto = float(input("Inserisci la percentuale di sconto (0 se non applicabile): "))

prezzo_finale = calcola_prezzo_finale(prezzo_libro, num_copie, sconto)
print("Il prezzo finale è:", prezzo_finale, "euro")
