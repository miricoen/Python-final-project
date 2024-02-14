import random
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from classes.FileOperation import FileOperation


class SalesData:
    def __init__(self, data):
        self.data = data

    def eliminate_duplicates(self):
        try:
            # Remove duplicate rows while handling null values
            cleaned_data = self.data.drop_duplicates()
            return cleaned_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def calculate_total_sales(self):
        try:
            # Group by product and sum up the sales
            total_sales = self.data.groupby('Product')['Total'].sum().reset_index()
            return total_sales
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def plot_total_sales(self, total_sales):
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(total_sales['Product'], total_sales['Total'], color="pink")
            plt.xlabel('Product')
            plt.ylabel('Total Sales')
            plt.title('Total Sales per Product')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def _calculate_total_sales_per_month(self):
        try:
            # Convert date column to datetime format
            self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y', errors='coerce')

            # Handle invalid dates by dropping NaT (Not a Time) values
            self.data = self.data.dropna(subset=['Date'])
            # Extract month from the date column and group by month, summing up the sales
            total_sales_per_month = self.data.groupby(self.data['Date'].dt.month)['Total'].sum().reset_index()
            return total_sales_per_month
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def plot_total_sales_per_month(self, total_sales_per_month):
        try:
            plt.figure(figsize=(10, 6))
            plt.plot(total_sales_per_month['Date'], total_sales_per_month['Total'], marker='o')
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.title('Total Sales per Month')
            plt.xticks(range(1, 13),
                       ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def plot_total_sales_per_month2(self, total_sales_per_month):
        try:
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Date', y='Total Sales', data=total_sales_per_month, color='skyblue')
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.title('Total Sales per Month')
            plt.xticks(range(1, 13),
                       ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def plot_monthly_sales_histogram(self, total_sales_per_month):
        try:
            # Plotting the histogram
            plt.figure(figsize=(10, 6))
            plt.hist(total_sales_per_month['Total'], bins=12, color='red', edgecolor='black', alpha=0.7)
            plt.xlabel('Total Sales')
            plt.ylabel('Frequency')
            plt.title('Monthly Sales Distribution')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def _identify_best_selling_product(self):
        try:
            # Group by product and sum up the sales, then find the product with the maximum sales
            best_selling_product = self.data.groupby('Product')['Total'].sum().idxmax()
            return best_selling_product
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def _identify_month_with_highest_sales(self):
        try:
            # Group by month and sum up the total sales, then find the month with the maximum total sales
            month_with_highest_sales = self.data.groupby(self.data['Date'].dt.month)['Total'].sum().idxmax()
            return month_with_highest_sales
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def _identify_minimum_selling_product(self):
        try:
            # Group by product and sum up the total, then find the product with the minimum total
            min_selling_product = self.data.groupby('Product')['Total'].sum().idxmin()
            return min_selling_product
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

        # פונקציה זו מחשבת את הממוצע של המכירות לכל החודשים

    def _calculate_average_sales(self):
        try:
            # Calculate the average of the total sales for all months
            average_sales = self.data['Total'].mean()
            return average_sales
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def analyze_sales_data(self):
        try:
            # Utilize previously defined private methods to perform analysis
            best_selling_product = self._identify_best_selling_product()
            month_with_highest_sales = self._identify_month_with_highest_sales()
            min_selling_product = self._identify_minimum_selling_product()
            average_sales = self._calculate_average_sales()

            # Create a dictionary with the analysis results
            analysis_results = {
                'best_selling_product': best_selling_product,
                'month_with_highest_sales': month_with_highest_sales,
                'min_selling_product': min_selling_product,
                'average_sales': average_sales
            }
            return analysis_results
        except Exception as e:
            FileOperation.catchErrorsFunc(f" An error occurred: {e} ")
            return None

    def plot_sales_distribution_pie_chart(self, sales_distribution):
        try:
            # Create figure and axes
            fig, ax = plt.subplots(figsize=(8, 8))

            # Plot pie chart
            ax.pie(sales_distribution.values(), labels=sales_distribution.keys(), autopct='%1.1f%%', startangle=140)

            # Add title
            ax.set_title('Sales Distribution')

            # Show plot
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def calculate_cumulative_sales(self):
        try:
            # Convert 'Date' column to datetime format
            self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')

            # Group by product and date, then calculate cumulative sum of sales
            cumulative_sales = self.data.groupby(['Product', self.data['Date'].dt.month])['Total'].sum().groupby(
                level=0).cumsum()
            return cumulative_sales
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def seaborn_cumulative_sales_pie(self, cumulative_sales):
        try:
            # Calculate total cumulative sales for each product
            total_cumulative_sales = cumulative_sales.groupby('Product').max()

            # Plot pie chart using Seaborn
            plt.figure(figsize=(8, 8))
            sns.pieplot(x=total_cumulative_sales.values, labels=total_cumulative_sales.index, startangle=140)
            plt.title('Distribution of Cumulative Sales Across Products')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def plot_cumulative_sales_pie(self, cumulative_sales):
        try:
            # Calculate total cumulative sales for each product
            total_cumulative_sales = cumulative_sales.groupby('Product').max()

            # Plot pie chart
            plt.figure(figsize=(8, 8))
            plt.pie(total_cumulative_sales, labels=total_cumulative_sales.index, autopct='%1.1f%%', startangle=140)
            plt.title('Distribution of Cumulative Sales Across Products')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def add_90_percent_values_column(self):
        try:
            # Calculate discount (assuming it's a percentage)
            discount = self.data['Total'] * 0.1  # Assuming 10% discount

            # Calculate price after discount
            price_after_discount = self.data['Total'] - discount

            # Create a new column in the DataFrame with the calculated price after discount
            self.data.loc[:, 'Discount'] = price_after_discount

            return self.data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_original_and_new_values(self):
        try:
            # Extract original values from the DataFrame
            original_values = self.data['Quantity'].tolist()  # Assuming 'Quantity' is the column you're operating on

            # Apply the calculation to get new values
            new_values = self.data['Quantity'] * 0.9  # For example, multiplying by 0.9

            return original_values, new_values.tolist()
        except Exception as e:
            print(f"An error occurred while getting original and new values: {e}")
            return None, None

    def seaborn_90_percent_values_comparison(self, original_values, new_values):
        try:
            # Create figure and axes
            fig, ax = plt.subplots(figsize=(8, 6))

            # Plot original values
            sns.scatterplot(x=range(len(original_values)), y=original_values, color='green', label='Original Values')

            # Plot new values
            sns.scatterplot(x=range(len(new_values)), y=new_values, color='red', label='New Values')

            # Add labels and legend
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            ax.set_title('Comparison of Original and New Values')
            ax.legend()

            # Show plot
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def plot_90_percent_values_comparison(self, original_values, new_values):
        try:
            # Create figure and axes
            fig, ax = plt.subplots(figsize=(8, 6))

            # Plot original values
            ax.scatter(range(len(original_values)), original_values, color='blue', label='Original Values')

            # Plot new values
            ax.scatter(range(len(new_values)), new_values, color='red', label='New Values')

            # Add labels and legend
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            ax.set_title('Comparison of Original and New Values')
            ax.legend()

            # Show plot
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def create_stats_dataframe(self, stats):
        try:
            # Create DataFrame from the stats dictionary
            stats_df = pd.DataFrame(stats).T
            return stats_df
        except Exception as e:
            print(f"An error occurred while creating DataFrame: {e}")
            return None

    def plot_stats_bar_chart(self, stats):
        try:
            # Extract statistic values for plotting
            categories = list(stats.keys())
            stats_values = {stat: [stats[col][stat] for col in categories] for stat in stats[categories[0]].keys()}

            # Plot
            fig, ax = plt.subplots(figsize=(10, 6))
            bar_width = 0.2
            index = np.arange(len(categories))

            for i, (stat, values) in enumerate(stats_values.items()):
                ax.bar(index + i * bar_width, values, bar_width, label=stat)

            ax.set_xlabel('Columns')
            ax.set_ylabel('Values')
            ax.set_title('Statistics of Numeric Columns')
            ax.set_xticks(index + bar_width)
            ax.set_xticklabels(categories)
            ax.legend()

            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def seaborn_stats_bar_chart(self, stats):
        try:
            # Create DataFrame from the stats dictionary
            stats_df = pd.DataFrame(stats).T

            # Plot bar chart using Seaborn
            plt.figure(figsize=(10, 6))
            sns.barplot(data=stats_df)
            plt.xlabel('Columns')
            plt.ylabel('Values')
            plt.title('Statistics of Numeric Columns')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def plot_stats_table(self, stats_df):
        try:
            # Create figure and axes
            fig, ax = plt.subplots(figsize=(10, 6))

            # Hide axes
            ax.axis('off')

            # Plot table
            ax.table(cellText=stats_df.values,
                     colLabels=stats_df.columns,
                     loc='center')

            # Show plot
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting table: {e}")

    def seaborn_stats_table(self, stats_df):
        try:
            # Create figure and axes
            fig, ax = plt.subplots(figsize=(10, 6))

            # Plot table using Seaborn
            sns.heatmap(stats_df, annot=True, fmt=".2f", cmap='coolwarm', linewidths=.5, ax=ax)

            # Show plot
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting table: {e}")

    def bar_chart_category_sum(self):
        try:
            # Group data by 'Product' and sum up the quantities sold for each product
            product_quantities = self.data.groupby('Product')['Quantity'].sum()

            # Plotting the bar chart
            plt.figure(figsize=(10, 6))  # Set the figure size
            product_quantities.plot(kind='bar', color='skyblue')  # Plotting the bar chart
            plt.title('Sum of Quantities Sold for Each Product')  # Set the title of the plot
            plt.xlabel('Product')  # Set the label for the x-axis
            plt.ylabel('Total Quantity Sold')  # Set the label for the y-axis
            plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels for better readability
            plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines to the plot
            plt.tight_layout()  # Adjust layout to prevent clipping of labels
            plt.show()  # Show the plot

        except Exception as e:
            print(f"An error occurred: {e}")

    def calculate_mean_quantity(self):
        try:
            # Extract 'Total' column as a NumPy array
            total_values = self.data['Total'].values

            # Calculate mean, median, and second max using NumPy functions
            mean_total = np.mean(total_values)
            median_total = np.median(total_values)
            second_max_total = np.partition(total_values, -2)[-2]  # Find second max using partitioning

            # Return calculated statistics
            return {
                'mean': mean_total,
                'median': median_total,
                'second_max': second_max_total
            }
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def filter_by_sellings_or_and(self):
        try:
            # Condition 1: If number of selling more than 5 or number of selling equals 0
            condition1 = (self.data['Quantity'] > 5) | (self.data['Quantity'] == 0)

            # Condition 2: If the price above 300 $ and sold less than 2 times
            condition2 = (self.data['Price'] > 300) & (self.data['Quantity'] < 2)

            # Filter the data based on both conditions
            filtered_data = self.data[condition1 & condition2]

            return filtered_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def divide_by_2(self):
        try:
            # Create a new column 'BlackFridayPrice' by dividing 'BLACK FRIDAY' column values by 2
            self.data.loc[:, 'BlackFridayPrice'] = self.data['Total'] / 2

            return self.data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def plot_total_distribution(self, original_data, modified_data):
        try:
            plt.figure(figsize=(10, 6))
            plt.boxplot([original_data['Total'], modified_data['BlackFridayPrice']],
                        labels=['Original Total', 'BlackFridayPrice'])
            plt.xlabel('Columns')
            plt.ylabel('Values')
            plt.title('Distribution of Total and BlackFridayPrice')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def calculate_stats(self, columns: list = None):
        try:
            if columns is None:
                columns = ['Price', 'Quantity', 'Total']

            stats = {}

            for col in columns:
                # Calculate statistics for each column
                max_value = self.data[col].max()
                sum_value = self.data[col].sum()
                abs_value = self.data[col].abs()
                cum_max_value = self.data[col].cummax()

                # Store statistics in a dictionary
                stats[col] = {
                    'max': max_value,
                    'sum': sum_value,
                    'abs': abs_value,
                    'cum_max': cum_max_value
                }

            return stats
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    # def plot_heatmap(data):
    #     try:
    #         # Plotting a heatmap using Seaborn
    #         plt.figure(figsize=(10, 6))
    #         sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    #         plt.title('Correlation Heatmap')
    #         plt.show()
    #     except Exception as e:
    #         print(f"An error occurred while plotting heatmap: {e}")

    def extract_sales_and_highest_amount(self, product_name):
        try:
            # Filter the data for the specific product
            product_data = self.data[self.data['Product'] == product_name]

            # Extract the number of sales and the highest amount paid
            num_sales = product_data['Quantity'].sum()
            highest_amount = product_data['Total'].max()

            # Generate a random number between num_sales and highest_amount
            random_amount = random.uniform(num_sales, highest_amount)

            # Calculate the range between the number of sales and the highest amount paid
            range_between = highest_amount - num_sales

            # Return the extracted values, random amount, and the range between them
            return random_amount, range_between
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None

    def display_table_and_rows(self):
        # Display the first three rows
        print("First Three Rows:")
        print(self.data.head(3))
        print()

        # Display the last two rows
        print("Last Two Rows:")
        print(self.data.tail(2))
        print()

        # Display a randomly selected row
        random_index = random.randint(0, len(self.data) - 1)
        print("Randomly Selected Row:")
        print(self.data.iloc[random_index])

    def iterate_numerical_values(self):
        for row in self.data.values:
            for value in row:
                if isinstance(value, (int, float)):
                    print(value)
