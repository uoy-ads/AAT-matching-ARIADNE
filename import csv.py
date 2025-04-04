import csv
import json

# Input and output file paths
input_csv = "SHFA-additional-20250404.csv"
output_json = "SHFA-additional-20250404.json"

# List to hold the JSON data
json_data = []

# Define the required fields
required_fields = ["sourceURI", "sourceLabel", "sourceLabelLanguage", "matchURI", "targetURI", "targetLabel"]

# Read the CSV file
with open(input_csv, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Process each row in the CSV
    for row in csv_reader:
        # Check if all required fields have data
        if all(row[field] for field in required_fields):
            json_entry = {
                "sourceURI": row["sourceURI"],
                "sourceLabel": row["sourceLabel"],
                "sourceLabelLanguage": row["sourceLabelLanguage"],
                "matchURI": row["matchURI"],
                "targetURI": row["targetURI"],
                "targetLabel": row["targetLabel"],
                "created": "",
                "updated": ""
            }
            json_data.append(json_entry)

# Write the JSON data to a file
with open(output_json, mode='w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print(f"JSON data has been written to {output_json}")

