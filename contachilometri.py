def tempo_di_percorrenza(distanza, velocita):
    tempo = distanza / velocita
    return tempo
distanza = float(input("Inserisci la distanza da percorrere in chilometri: "))
velocita = float(input("Inserisci la velocità costante in chilometri all'ora: "))
tempo_necessario = tempo_di_percorrenza(distanza, velocita)
print("Il tempo necessario per percorrere", distanza, "chilometri alla velocità di", velocita, "chilometri all'ora è di", tempo_necessario, "ore.")
