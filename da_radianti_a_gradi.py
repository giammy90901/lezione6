import math

def gradi_a_radianti(gradi):
    rad = (gradi * math.pi) / 180
    return rad
gradi = float(input("Inserisci il valore dell'angolo in gradi: "))
radianti = gradi_a_radianti(gradi)
print("Il valore dell'angolo in radianti è:", radianti)
