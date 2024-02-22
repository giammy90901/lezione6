def costo_energia(kwh_consumati, tariffa_kwh):
    if kwh_consumati <= 100:
        costo = kwh_consumati * tariffa_kwh * 0.9
    else:
        costo = kwh_consumati * tariffa_kwh
    return costo
consumo = float(input("Inserisci i kWh consumati: "))
tariffa = float(input("Inserisci la tariffa per kWh: "))
costo_totale = costo_energia(consumo, tariffa)
print("Il costo totale dell'energia è:", costo_totale, "euro")
