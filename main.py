import pandas as pd

from classes.FileOperation import FileOperation
from classes.SalesData import SalesData


def main():
    # Test catchErrorsFunc
    file_op = FileOperation()
    file_op.catchErrorsFunc("This is a test error message.")

    # Test read_excel
    file_path = r'assets\YafeNof.csv'
    data = file_op.read_excel(file_path)
    if data is not None:
        print("Data read from Excel file:")
        print(data.head())

    # Test save_to_excel
    new_file_name = 'output_data.csv'
    file_op.save_to_excel(data, new_file_name)
    print(f"Data saved to '{new_file_name}' successfully.")
    df = pd.DataFrame(data)
    sales_data = SalesData(df)

    # Test eliminate_duplicates
    cleaned_data = sales_data.eliminate_duplicates()
    print("Cleaned Data:")
    print(cleaned_data)

    # Test calculate_total_sales
    total_sales = sales_data.calculate_total_sales()
    print("\nTotal Sales:")
    print(total_sales)

    # Test _calculate_total_sales_per_month
    total_sales_per_month = sales_data._calculate_total_sales_per_month()
    print("\nTotal Sales per Month:")
    print(total_sales_per_month)

    # Test analyze_sales_data
    analysis_results = sales_data.analyze_sales_data()
    print("\nAnalysis Results:")
    print(analysis_results)

    # Test plot_total_sales
    sales_data.plot_total_sales(total_sales)

    # Test plot_total_sales_per_month
    sales_data.plot_total_sales_per_month(total_sales_per_month)

    # Test plot_total_sales_per_month2
    sales_data.plot_total_sales_per_month2(total_sales_per_month)

    # Test plot_monthly_sales_histogram
    sales_data.plot_monthly_sales_histogram(total_sales_per_month)

    # Test calculate_cumulative_sales
    cumulative_sales = sales_data.calculate_cumulative_sales()
    print("\nCumulative Sales:")
    print(cumulative_sales)

    # Test seaborn_cumulative_sales_pie
    sales_data.seaborn_cumulative_sales_pie(cumulative_sales)

    # Test plot_cumulative_sales_pie
    sales_data.plot_cumulative_sales_pie(cumulative_sales)

    # Test add_90_percent_values_column
    modified_data = sales_data.add_90_percent_values_column()
    print("\nModified Data:")
    print(modified_data)

    # Test get_original_and_new_values
    original_values, new_values = sales_data.get_original_and_new_values()
    print("\nOriginal Values:")
    print(original_values)
    print("\nNew Values:")
    print(new_values)

    # Test seaborn_90_percent_values_comparison
    sales_data.seaborn_90_percent_values_comparison(original_values, new_values)

    # Test plot_90_percent_values_comparison
    sales_data.plot_90_percent_values_comparison(original_values, new_values)

    # Test create_stats_dataframe
    stats = sales_data.calculate_stats()
    stats_df = sales_data.create_stats_dataframe(stats)
    print("\nStats DataFrame:")
    print(stats_df)

    # Test plot_stats_bar_chart
    sales_data.plot_stats_bar_chart(stats)

    # Test seaborn_stats_bar_chart
    sales_data.seaborn_stats_bar_chart(stats)

    # Test plot_stats_table
    sales_data.plot_stats_table(stats_df)

    # Test seaborn_stats_table
    sales_data.seaborn_stats_table(stats_df)

    # Test bar_chart_category_sum
    sales_data.bar_chart_category_sum()

    # Test calculate_mean_quantity
    mean_quantity = sales_data.calculate_mean_quantity()
    print("\nMean Quantity:")
    print(mean_quantity)

    # Test filter_by_sellings_or_and
    filtered_data = sales_data.filter_by_sellings_or_and()
    print("\nFiltered Data:")
    print(filtered_data)

    # Test divide_by_2
    modified_data = sales_data.divide_by_2()
    print("\nModified Data:")
    print(modified_data)

    # Test plot_total_distribution
    sales_data.plot_total_distribution(df, modified_data)

    # Test extract_sales_and_highest_amount
    product_name = 'A'
    random_amount, range_between = sales_data.extract_sales_and_highest_amount(product_name)
    print("\nRandom Amount:", random_amount)
    print("Range Between:", range_between)

    # Test display_table_and_rows
    sales_data.display_table_and_rows()

    # Test iterate_numerical_values
    sales_data.iterate_numerical_values()


if __name__ == "__main__":
    main()
