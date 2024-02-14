import unittest
import pandas as pd
from datetime import datetime
from classes import FileOperation

class TestFileOperation(unittest.TestCase):

    def setUp(self):
        self.file_op = FileOperation()

    def tearDown(self):
        pass

    def test_read_excel_file_not_found(self):
        file_path = "non_existing_file.xlsx"
        data = self.file_op.read_excel(file_path)
        self.assertIsNone(data)

    def test_read_excel_csv(self):
        file_path = "test_data/test_data.csv"
        data = self.file_op.read_excel(file_path)
        self.assertIsInstance(data, pd.DataFrame)

    def test_read_excel_excel(self):
        file_path = "test_data/test_data.xlsx"
        data = self.file_op.read_excel(file_path)
        self.assertIsInstance(data, pd.DataFrame)

    def test_save_to_excel(self):
        data = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']})
        file_name = "test_data/test_output.xlsx"
        self.file_op.save_to_excel(data, file_name)
        saved_data = pd.read_excel(file_name)
        self.assertTrue(data.equals(saved_data))

    def test_save_to_excel_error(self):
        data = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']})
        file_name = "test_data/invalid_folder/test_output.xlsx"
        with self.assertRaises(Exception):
            self.file_op.save_to_excel(data, file_name)

    def test_catch_errors_func(self):
        test_message = "Test error message"
        expected_output = f"<miri & rivki, {datetime.now()}> {test_message} <miri & rivki>"
        with self.assertLogs() as log:
            self.file_op.catchErrorsFunc(test_message)
        self.assertIn(expected_output, log.output[0])

if __name__ == '__main__':
    unittest.main()
