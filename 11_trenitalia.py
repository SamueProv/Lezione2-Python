def calcola_costo_totale(costo_camera, durata_soggiorno):
    costo_biglietto = 30
    costo_albergo = costo_camera * durata_soggiorno
    costo_totale = costo_biglietto + costo_albergo
    return costo_totale

costo_camera = float(input("Inserisci il costo per notte per studente (in euro): "))
durata_soggiorno = int(input("Inserisci la durata del soggiorno in notti: "))
costo = calcola_costo_totale(costo_camera, durata_soggiorno)
print(f"Il costo totale per ogni studente è: {costo:.2f} euro")
