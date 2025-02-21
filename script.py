import time
import requests

# Replace with your referral link
REFERRAL_LINK = "https://event.goldstation.io/?referral=2D660"

def visit_referral():
    response = requests.get(REFERRAL_LINK)
    if response.status_code == 200:
        print("Referral link visited successfully!")
    else:
        print("Failed to visit referral link.")

# Run the function
visit_referral()
