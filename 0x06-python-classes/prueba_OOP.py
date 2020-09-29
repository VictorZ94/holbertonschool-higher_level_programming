#!/usr/bin/python3
class coche():
    largochasis = 250
    anchochasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

micoche=coche()
print(micoche.largochasis)
print(micoche.ruedas)

# micoche.arrancar()
(print(micoche.estado()))