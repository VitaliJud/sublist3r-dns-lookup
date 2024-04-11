#!/bin/bash

# Check if a file name is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# File where the subdomains are stored
FILE=$1

# Check if the file exists
if [ ! -f "$FILE" ]; then
    echo "File not found!"
    exit 1
fi

# Output file for nslookup results
OUTPUT_FILE="nslookup_results.txt"

# Ensure the output file is empty
> "$OUTPUT_FILE"

# Read the file line by line
while IFS= read -r subdomain
do
    echo "Running nslookup for $subdomain" | tee -a "$OUTPUT_FILE"
    echo "A and CNAME records:" | tee -a "$OUTPUT_FILE"
    nslookup "$subdomain" | tee -a "$OUTPUT_FILE"
    echo "TXT records:" | tee -a "$OUTPUT_FILE"
    nslookup -type=TXT "$subdomain" | tee -a "$OUTPUT_FILE"
    echo "-----------------------------------------------------" | tee -a "$OUTPUT_FILE"
done < "$FILE"

echo "All nslookup results have been saved to $OUTPUT_FILE"
