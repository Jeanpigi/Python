import unittest


def suma(num_1, num_2):
    return num_1 + num_2


class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivo(self):
        number_1 = 10
        number_2 = 5

        resultado = suma(number_1, number_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        number_1 = -10
        number_2 = -2

        resultado = suma(number_1, number_2)

        self.assertEqual(resultado, -12)


if __name__ == '__main__':
    unittest.main()
