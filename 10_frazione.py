def frazione_inversa(numeratore, denominatore):
    if numeratore != 0 and denominatore != 0:
        inversa = f"{denominatore}/{numeratore}"
        return inversa
    else:
        return "Errore: numeratore o denominatore uguali a zero"

numeratore = 2
denominatore = 5

print(frazione_inversa(numeratore, denominatore))