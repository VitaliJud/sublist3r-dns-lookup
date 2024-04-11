## About Sublist3r 

Sublist3r is a python tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers and bug hunters collect and gather subdomains for the domain they are targeting. Sublist3r enumerates subdomains using many search engines such as Google, Yahoo, Bing, Baidu and Ask. Sublist3r also enumerates subdomains using Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS.

[subbrute](https://github.com/TheRook/subbrute) was integrated with Sublist3r to increase the possibility of finding more subdomains using bruteforce with an improved wordlist. The credit goes to TheRook who is the author of subbrute.

**Original Repo for [Sublist3r](https://github.com/aboul3la/Sublist3r.git).**


## Installation
Using Sublist3r involves Python. MacOS generally comes with pre-installed python3 - which is what used in the current example. Make sure to make adjustments to fit your current python version if needed.

1.**Clone Sublist3r**
  
  ```
  git clone https://github.com/aboul3la/Sublist3r.git && cd sublist3r
  ```
  
2.**Install Package**

    pip install -r requirements.txt
3.**Create a Python file to utilize Sublist3r - use `sub.py` file in current Repo**
  ```
# import the necessary package
import subprocess

# Function to call Sublist3r and get subdomains
def get_subdomains(domain):
    command = ["python", "sublist3r.py", "-d", domain, "-o", "subdomains.txt"]
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with open("subdomains.txt", "r") as file:
            subdomains = file.readlines()
        
        # Add the root domain to the list of subdomains
        subdomains.append(domain + '\n')  # Ensure it goes to a new line in the output

        # Write the updated list back to the file (optional)
        with open("subdomains.txt", "w") as file:
            file.writelines(subdomains)
        
        return ''.join(subdomains)  # Return as a single string if needed
    except subprocess.CalledProcessError as e:
        print("Failed to run Sublist3r")
        return None

# Example usage
domain = "example.com"
subdomains = get_subdomains(domain)
if subdomains:
    print("Found subdomains including the root domain:")
    print(subdomains)
```

4.**Run Your Script**

```
python3 your_script_name.py
```

5.**Check `subdomains.txt` file to make sure you have list of all subdomains including the root domain**

6.**Open a text editor and Create the following Bash script - use `run_nslookup.sh` file in current Repo**
```
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
```
7.**Check `nslookup_results.txt` file for your list of DNS records (A, CNAME and TXT) for all subdomains and root domain**


