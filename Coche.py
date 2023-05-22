"""


Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Adrián González
"""


class Vehicle:

    """
    Esta es la superclase Vehículo


    """

    def __init__(self, num_serie, fabricante, color):
        """

        :param num_serie:
        :param fabricante:
        :param color:
        """

        self.num_serie = num_serie;
        self.fabricante = fabricante;
        self.color = color;


class Coche(Vehicle):
    """
    Esta es la clase Coche
    """
    num_serie = 1;
    cilindrada = 1000;
    fabricante = 'seat';
    color = 'rojo';

    def __init__(self):
        pass;

    @property
    def num_serie(self):
        """

        :return: self.__num_serie
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """

        :param value:
        :return:
        """
        self.__num_serie = value

    @property
    def color(self):
        """

        :return: self.__color
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """

        :param value:
        :return:
        """
        self.__color = value

    @property
    def cilindrada(self):
        """

        :return: self.__cilindrada
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """

        :param value:
        :return:
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """

        :return: self.__fabricante
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """

        :param value:
        :return:
        """
        self.__fabricante = value
