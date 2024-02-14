import unittest
import pandas as pd
import numpy as np
from classes.SalesData import SalesData


class TestSalesData(unittest.TestCase):

    def setUp(self):
        # Generate sample data for testing
        np.random.seed(0)
        data = {
            'Product': ['A', 'B', 'C'] * 5,
            'Date': pd.date_range(start='2023-01-01', periods=15),
            'Quantity': np.random.randint(1, 10, size=15),
            'Price': np.random.randint(50, 500, size=15),
            'Total': np.random.randint(100, 1000, size=15)
        }
        self.sales_data = SalesData(pd.DataFrame(data))

    def tearDown(self):
        pass

    def test_eliminate_duplicates(self):
        cleaned_data = self.sales_data.eliminate_duplicates()
        self.assertEqual(len(cleaned_data), 15)  # Ensure no duplicates

    def test_calculate_total_sales(self):
        total_sales = self.sales_data.calculate_total_sales()
        self.assertIsInstance(total_sales, pd.DataFrame)
        self.assertEqual(len(total_sales), 3)  # Three products in the sample data

    def test_calculate_mean_quantity(self):
        mean_quantity = self.sales_data.calculate_mean_quantity()
        self.assertIsInstance(mean_quantity, dict)
        self.assertEqual(len(mean_quantity), 3)  # Three statistics calculated

    def test_filter_by_sellings_or_and(self):
        filtered_data = self.sales_data.filter_by_sellings_or_and()
        self.assertIsInstance(filtered_data, pd.DataFrame)
        self.assertTrue(len(filtered_data) < len(self.sales_data.data))

    def test_divide_by_2(self):
        modified_data = self.sales_data.divide_by_2()
        self.assertIsInstance(modified_data, pd.DataFrame)
        self.assertTrue('BlackFridayPrice' in modified_data.columns)

    def test_get_original_and_new_values(self):
        original_values, new_values = self.sales_data.get_original_and_new_values()
        self.assertIsInstance(original_values, list)
        self.assertIsInstance(new_values, list)
        self.assertEqual(len(original_values), len(self.sales_data.data))
        self.assertEqual(len(new_values), len(self.sales_data.data))


    def test_plot_total_sales(self):
        total_sales = self.sales_data.calculate_total_sales()
        self.sales_data.plot_total_sales(total_sales)  # Manual inspection required

    def test_plot_total_sales_per_month(self):
        total_sales_per_month = self.sales_data._calculate_total_sales_per_month()
        self.sales_data.plot_total_sales_per_month(total_sales_per_month)  # Manual inspection required

    def test_plot_total_sales_per_month2(self):
        total_sales_per_month = self.sales_data._calculate_total_sales_per_month()
        self.sales_data.plot_total_sales_per_month2(total_sales_per_month)  # Manual inspection required

    def test_plot_monthly_sales_histogram(self):
        total_sales_per_month = self.sales_data._calculate_total_sales_per_month()
        self.sales_data.plot_monthly_sales_histogram(total_sales_per_month)  # Manual inspection required

    def test_analyze_sales_data(self):
        analysis_results = self.sales_data.analyze_sales_data()
        self.assertIsInstance(analysis_results, dict)
        self.assertEqual(len(analysis_results), 4)  # Four analysis results expected

    def test_plot_cumulative_sales_pie(self):
        cumulative_sales = self.sales_data.calculate_cumulative_sales()
        self.sales_data.plot_cumulative_sales_pie(cumulative_sales)  # Manual inspection required

    def test_seaborn_cumulative_sales_pie(self):
        cumulative_sales = self.sales_data.calculate_cumulative_sales()
        self.sales_data.seaborn_cumulative_sales_pie(cumulative_sales)  # Manual inspection required

    def test_add_90_percent_values_column(self):
        modified_data = self.sales_data.add_90_percent_values_column()
        self.assertTrue('Discount' in modified_data.columns)


    def test_extract_sales_and_highest_amount(self):
        random_amount, range_between = self.sales_data.extract_sales_and_highest_amount('A')
        self.assertIsInstance(random_amount, float)
        self.assertIsInstance(range_between, int)

    def test_display_table_and_rows(self):
        # No assertion can be made as this function prints output
        self.sales_data.display_table_and_rows()

    if __name__ == '__main__':
        unittest.main()
