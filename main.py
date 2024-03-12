import pandas as pd

def convert_sheet_to_table(file_path):
    """
    Reads a spreadsheet and converts it into a pandas DataFrame (table).

    :param file_path: Path to the spreadsheet file (e.g., 'data.xlsx').
    :return: Pandas DataFrame.
    """
    try:
        # Read the file based on its extension
        if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported file format")

        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


file_path = 'tables/random_numbers.csv'
if (table := convert_sheet_to_table(file_path)) is not None:
    print(table)
