def saluto_appropriato(ora, nome):
    saluto = "Ciao"
    if 0 <= ora < 12:
        saluto = "Buongiorno"
    if 12 <= ora < 18:
        saluto = "Buon pomeriggio"
    if 18 <= ora <= 23:
        saluto = "Buonasera"
    return f"{saluto}, {nome}!"
ora = int(input("Inserisci l'ora del giorno (0-23): "))
nome = input("Inserisci il tuo nome: ")
print(saluto_appropriato(ora, nome))
