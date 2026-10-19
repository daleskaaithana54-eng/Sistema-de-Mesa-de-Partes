import unittest
from unittest.mock import patch, mock_open
import reportes


class TestBusquedaReportes(unittest.TestCase):

    @patch("builtins.input", return_value="hola")
    @patch("builtins.open", mock_open(read_data="Hola mundo, hola Python"))
    def test_contar_coincidencias(self, mock_input=None):
        with patch("builtins.print") as imprimir:
            reportes.contar_busqueda()

        imprimir.assert_called_with("Veces que aparece la palabra:", 2)

    @patch("builtins.input", return_value="")
    def test_busqueda_vacia(self, mock_input):
        with patch("builtins.print") as imprimir:
            reportes.contar_busqueda()

        imprimir.assert_called_with("Debe ingresar una palabra.")


if __name__ == "__main__":
    unittest.main()
