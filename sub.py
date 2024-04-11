import subprocess

# Function to call Sublist3r and get subdomains
def get_subdomains(domain):
    command = ["python3", "sublist3r.py", "-d", domain, "-o", "subdomains.txt"]
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with open("subdomains.txt", "r") as file:
            subdomains = file.read()
        return subdomains
    except subprocess.CalledProcessError as e:
        print("Failed to run Sublist3r")
        return None

# Example usage
domain = "example.com"
subdomains = get_subdomains(domain)
if subdomains:
    print("Found subdomains:")
    print(subdomains)
