"""
Clase Perro.

Autor: Adrián González Martínez.
"""


class Perro:
    def __init__(self):
        """
        init de la clase Perro
        """
        self.guau = 'Guau'

    def ladrar(self):
        """
        hace un print self.guau
        :return:
        """
        print(self.guau)


p = Perro();
p.ladrar();
