def calcola_distanza(velocita, tempo):
    distanza = velocita * tempo
    return distanza
velocita = float(input("Inserisci la velocità media in chilometri all'ora: "))
tempo = float(input("Inserisci il tempo di viaggio in ore: "))
distanza_percorsa = calcola_distanza(velocita, tempo)
print("La distanza percorsa durante il viaggio è di", distanza_percorsa, "chilometri.")
