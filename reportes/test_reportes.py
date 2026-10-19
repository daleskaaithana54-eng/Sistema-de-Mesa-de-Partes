import unittest
from unittest.mock import patch
import reportes


class TestReportes(unittest.TestCase):

    def test_contar_palabras(self):
        with patch("builtins.open", unittest.mock.mock_open(
            read_data="Hola mundo desde Python"
        )):
            with patch("builtins.print") as imprimir:
                reportes.contar_palabras()

        imprimir.assert_called_with("Cantidad de palabras:", 4)

    def test_contar_lineas(self):
        with patch("builtins.open", unittest.mock.mock_open(
            read_data="Primera linea\nSegunda linea\n"
        )):
            with patch("builtins.print") as imprimir:
                reportes.contar_lineas()

        imprimir.assert_called_with("Cantidad de lineas:", 2)

    def test_contar_caracteres(self):
        with patch("builtins.open", unittest.mock.mock_open(
            read_data="Hola"
        )):
            with patch("builtins.print") as imprimir:
                reportes.contar_caracteres()

        imprimir.assert_called_with("Cantidad de caracteres:", 4)


if __name__ == "__main__":
    unittest.main()
