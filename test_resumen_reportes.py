import unittest
from unittest.mock import patch, mock_open
import reportes


class TestResumenReportes(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data="Hola mundo\nPython"))
    def test_resumen_completo(self):
        with patch("builtins.print") as imprimir:
            reportes.resumen_completo()

        mensajes = [
            llamada.args
            for llamada in imprimir.call_args_list
            if llamada.args
        ]

        self.assertIn(("Total de palabras:", 3), mensajes)
        self.assertIn(("Total de lineas:", 2), mensajes)
        self.assertIn(("Total de caracteres:", 17), mensajes)


if __name__ == "__main__":
    unittest.main()

