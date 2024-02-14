import datetime
import os
import pandas as pd


class FileOperation:

    def catchErrorsFunc(self, massege):
        print(f"<miri & rivki, {datetime.datetime.now()}> {massege} <miri & rivki>")

    def read_excel(self, file_path: str):
        try:
            # Check if the file exists
            if not os.path.exists(file_path):
                self.catchErrorsFunc(f"File '{file_path}' not found. Creating a new one...")
                # Create a subfolder if it doesn't exist
                subfolder = os.path.dirname(file_path)
                os.makedirs(subfolder, exist_ok=True)
                # Create an empty DataFrame
                data = pd.DataFrame(columns=['Column1', 'Column2'])  # Adjust columns as needed
            else:
                # Check file extension to determine the appropriate method
                if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
                    # Read data from Excel file
                    data = pd.read_excel(file_path)
                elif file_path.endswith('.csv'):
                    # Read data from CSV file
                    data = pd.read_csv(file_path)
                else:
                    raise ValueError(
                        "Unsupported file format. Please provide an Excel (.xls, .xlsx) or CSV (.csv) file.")

            return data

        except Exception as e:
            self.catchErrorsFunc(f"An error occurred: {e}")
            return None

    def save_to_excel(self, data, file_name: str):
        try:
            # Save data to Excel file
            data.to_csv(file_name, index=False)
            print(f"Data saved to '{file_name}' successfully.")
        except Exception as e:
            self.catchErrorsFunc(f"An error occurred: {e} ")
