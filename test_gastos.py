
import unittest
from unittest.mock import patch

import gastos


class TestModuloGastos(unittest.TestCase):

    def setUp(self):
        gastos.gastos.clear()

    @patch("builtins.input", side_effect=["Pasajes", "12.50"])
    def test_registrar_gasto_valido(self, mock_input):
        gastos.registrar_gasto()

        self.assertEqual(len(gastos.gastos), 1)
        self.assertEqual(gastos.gastos[0]["descripcion"], "Pasajes")
        self.assertEqual(gastos.gastos[0]["monto"], 12.50)

    @patch("builtins.input", side_effect=["", "12.50"])
    def test_rechazar_descripcion_vacia(self, mock_input):
        gastos.registrar_gasto()

        self.assertEqual(len(gastos.gastos), 0)

    @patch("builtins.input", side_effect=["Pasajes", "abc"])
    def test_rechazar_monto_no_numerico(self, mock_input):
        gastos.registrar_gasto()

        self.assertEqual(len(gastos.gastos), 0)

    @patch("builtins.input", side_effect=["Pasajes", "0"])
    def test_rechazar_monto_cero(self, mock_input):
        gastos.registrar_gasto()

        self.assertEqual(len(gastos.gastos), 0)

    @patch("builtins.input", side_effect=["Pasajes", "-5"])
    def test_rechazar_monto_negativo(self, mock_input):
        gastos.registrar_gasto()

        self.assertEqual(len(gastos.gastos), 0)

    def test_calcular_total_gastos(self):
        gastos.gastos.extend([
            {"descripcion": "Pasajes", "monto": 12.50},
            {"descripcion": "Materiales", "monto": 7.50}
        ])

        self.assertEqual(gastos.calcular_total_gastos(), 20.00)

    def test_total_sin_gastos(self):
        self.assertEqual(gastos.calcular_total_gastos(), 0)


if __name__ == "__main__":
    unittest.main()
