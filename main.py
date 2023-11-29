import camelot
import pandas as pd
import os

#tables = camelot.read_pdf("sample.pdf", "all", flavor="stream")
#print(tables)





# Directory containing your PDF files
pdf_directory = "./Pdf/"

# Output directory for CSV files
output_directory = "./output/"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Iterate through each PDF file in the directory
for pdf_file in os.listdir(pdf_directory):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, pdf_file)

        # Read tables from the current PDF file
        tables = camelot.read_pdf(pdf_path, "all", flavor="stream")

        # Create a subfolder based on the PDF file name
        pdf_folder = os.path.join(output_directory, os.path.splitext(pdf_file)[0])
        os.makedirs(pdf_folder, exist_ok=True)

        tables.export(pdf_folder + '/file.csv', f="csv", compress=False)

        # Export tables to CSV files in the output directory
        # Export tables to CSV files in the subfolder
        # for i, table in enumerate(tables):
        #     # Get the DataFrame from the Table object
        #     df = table.df

        #      # Export DataFrame to CSV file within the subfolder
        #     csv_file_path = os.path.join(pdf_folder, f"{pdf_file}_table_{i + 1}.csv")
        #     df.to_csv(csv_file_path, index=False)

            # Export DataFrame to CSV file
            #df.to_csv(os.path.join(output_directory, f"{pdf_file}_table_{i + 1}.csv"), index=False)