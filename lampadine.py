def consumo_mensile_lampadine(num_lampadine, consumo_giornaliero_per_lampadina):
    return num_lampadine * consumo_giornaliero_per_lampadina * 30
num_lampadine = int(input("Inserisci il numero di lampadine in casa: "))
consumo_giornaliero_per_lampadina = float(input("Inserisci il consumo giornaliero per lampadina (in kWh): "))
consumo_totale_mensile = consumo_mensile_lampadine(num_lampadine, consumo_giornaliero_per_lampadina)
print("Il consumo totale mensile delle lampadine è:", consumo_totale_mensile, "kWh")
