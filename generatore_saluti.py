def messaggio_di_benvenuto(nome):
    return f"Benvenuto, {nome}! Spero tu stia avendo una splendida giornata."
nome_utente = input("Inserisci il tuo nome: ")
messaggio = messaggio_di_benvenuto(nome_utente)
print(messaggio)
