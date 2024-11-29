# Airtable Configuration File

# Your Airtable API key
# You can find your API key in your Airtable account settings
API_KEY = "patvJDTzSdcijlWmN.de90b6270b86256f00add5b9ed37620c0c7b4da16ac97431b87f34ae2fa3232d"

# Airtable base ID
# You can find the base ID from the Airtable API documentation or URL of your Airtable base
BASE_ID = "your_airtable_base_id"

# Table name in Airtable
# Ensure the table exists in your Airtable base
TABLE_NAME = "RAG Results"

# Function to verify the configuration (Optional)
def print_config():
    print(f"Airtable Config:")
    print(f"  API Key: {'*' * len(API_KEY)}")  # Obfuscate API Key
    print(f"  Base ID: {BASE_ID}")
    print(f"  Table Name: {TABLE_NAME}")

if __name__ == "__main__":
    print_config()
