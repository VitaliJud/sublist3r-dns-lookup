# import the necessary package
import subprocess

# Function to call Sublist3r and get subdomains
def get_subdomains(domain):
    command = ["python3", "sublist3r.py", "-d", domain, "-o", "subdomains.txt"]
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
