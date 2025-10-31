# Navigate to your bot directory
cd "C:\directory" # Replace with your directory

# Create virtual environment if it doesn't exist
if (!(Test-Path "venv")) {
    python3 -m venv venv
}

# Activate the virtual environment
& "venv\Scripts\Activate.ps1"

# Run the bot
python Discord_Email.py
