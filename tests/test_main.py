import pandas as pd
import unittest
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from main import create_random_data, send_email


class TestDataCreation(unittest.TestCase):
    def test_num_rows(self):
        num_rows = 100
        df = create_random_data(num_rows)
        self.assertEqual(len(df), num_rows, 'El número de filas generadas no coincide con el número especificado')

    def test_columns(self):
        num_rows = 100
        df = create_random_data(num_rows)
        expected_columns = ['ID', 'Country', 'Credit_Limit', 'Credit_Card_Name', 'Gender', 'Occupation', 'Marital_Status']
        self.assertCountEqual(df.columns, expected_columns, 'Las columnas generadas no coinciden con las esperadas')

    def test_data_types(self):
        num_rows = 100
        df = create_random_data(num_rows)
        self.assertTrue(df.dtypes['ID'] == int, 'El tipo de dato de la columna "ID" no es entero')
        self.assertTrue(df.dtypes['Country'] == str, 'El tipo de dato de la columna "Country" no es cadena')
        self.assertTrue(df.dtypes['Credit_Limit'] == int, 'El tipo de dato de la columna "Credit_Limit" no es entero')
        self.assertTrue(df.dtypes['Credit_Card_Name'] == str, 'El tipo de dato de la columna "Credit_Card_Name" no es cadena')
        self.assertTrue(df.dtypes['Gender'] == str, 'El tipo de dato de la columna "Gender" no es cadena')
        self.assertTrue(df.dtypes['Occupation'] == str, 'El tipo de dato de la columna "Occupation" no es cadena')
        self.assertTrue(df.dtypes['Marital_Status'] == str, 'El tipo de dato de la columna "Marital_Status" no es cadena')
        
    def test_send_email(self):
        html = '<html><body><h1>Test Email</h1></body></html>'
        self.assertTrue(send_email(html), 'No se pudo enviar el correo electrónico')


if __name__ == '__main__':
    unittest.main()
