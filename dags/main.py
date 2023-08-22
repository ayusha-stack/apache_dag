import requests
import csv
from io import StringIO
import os

def download_csv_from_link(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            csv_content = response.content.decode('utf-8')
            
            
            with open(save_path, 'w', newline='') as csv_file:
                csv_file.write(csv_content)
            
            print(f"CSV downloaded and saved successfully to {save_path}")
            return True
        else:
            print(f"Failed to download CSV. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def count_rows_in_csv(csv_path):
    try:
        with open(csv_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            row_count = sum(1 for row in csv_reader)
            print(f"Number of rows in the CSV: {row_count}")
            return row_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

def delete_csv_file(file_path):
    try:
        os.remove(file_path)
        print(f"CSV file '{file_path}' deleted successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
# csv_url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv'  # Replace with your CSV URL
# csv_save_path = 'downloaded.csv'  # Replace with the desired local file path

# # Download CSV
# if download_csv_from_link(csv_url, csv_save_path):
#     # Count rows
#     row_count = count_rows_in_csv(csv_save_path)
    
#     # Delete CSV file
#     if row_count > 0:
#         delete_csv_file(csv_save_path)
