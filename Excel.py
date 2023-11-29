import pandas as pd
import os

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = "./output/foo-page-2-table-1.csv"

# Replace 'your_main_folder' with the path to the main folder containing subfolders with CSV files
main_folder = "./output/"

# Define the expected column names
expected_columns = ["Time", "Type", "Username", "Domain", "Workstation"]


def merge_cells(csv_file_path):
    df = pd.read_csv(csv_file_path)

    # Group by index // Change the index to a proper grouping column if needed
    grouped_df = df.groupby(df.index // 5)

        #Aggregate the grouped data by concatenating the values
    combined_df = grouped_df.agg(lambda x: ' '.join(str(val) for val in x if pd.notna(val)))

        #Display the combined DataFrame
        # print(combined_df)

    # Export the combined DataFrame to a CSV file
    return combined_df

# Function to check if a CSV file has the expected columns in its first row
def check_csv_file(file_path):
    try:
        # Read the first row of the CSV file
        first_row = pd.read_csv(file_path, nrows=1)
        
        # Check if the first row contains the expected columns
        return any(column in first_row.columns for column in expected_columns)
    except pd.errors.EmptyDataError:
        # Handle empty CSV files
        return False
    except Exception as e:
        # Handle other exceptions
        print(f"Error reading file {file_path}: {e}")
        return False
    
# Iterate through each subfolder in the main folder
for subfolder_name in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder_name)

    # Check if the current item in the main folder is a subfolder
    if os.path.isdir(subfolder_path):
        print(f"Processing subfolder: {subfolder_name}")

        df_list = []

    df_list = []
    # Iterate through all CSV files in the subfolder
    for file_name in os.listdir(subfolder_path):
            if file_name.endswith('.csv'):
                file_path = os.path.join(subfolder_path, file_name)
        
        # Check if the CSV file has the expected columns in its first row
    if check_csv_file(file_path):
            df_list.append(merge_cells(file_path))
            # print(f"The CSV file '{file_name}' has the expected columns.")
        # else:
            # print(f"The CSV file '{file_name}' does not have the expected columns.")
    result_df = pd.DataFrame(columns=expected_columns)

    # Iterate through each DataFrame in the list
    for df in df_list:
        # If the DataFrame has the expected columns, extract and append the values
        if all(column in df.columns for column in expected_columns):
            result_df = pd.concat([result_df, df[expected_columns]], ignore_index=True)
        else:
            # If the DataFrame doesn't have the expected columns, pick values based on index
            result_df = pd.concat([result_df, df.iloc[:, :len(expected_columns)]], ignore_index=True)

    # Reset the index of the resulting DataFrame
    result_df.reset_index(drop=True, inplace=True)

    # Display the resulting DataFrame
    result_df.to_csv('output.csv', index=False)
    # # Display the DataFrame
    # print(df)

