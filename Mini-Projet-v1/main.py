from api_handler import fetch_data
from data_manager import process_and_save_data

API_URL = "https://api.example.com/data"

def main():
    try:
        print("Fetching data from API...")
        data = fetch_data(API_URL)
        print("Processing and saving data...")
        process_and_save_data(data, 'output.csv')
        print("Data successfully processed and saved.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
