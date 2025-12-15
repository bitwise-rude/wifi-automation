import requests
import json
import sys
from dotenv import load_dotenv
import os 

load_dotenv()

#===================================

USERNAME = os.getenv("SSID")
PASSWORD = os.getenv("PASSWORD")
TOKEN_URL = "https://subscribers.beta.gispaas.geniussystems.com.np/subscriber/authentication/v1/tenants/13/subscribers/access-token"
INFO_URL = "https://subscribers.beta.gispaas.geniussystems.com.np/subscriber/account/v1/tenants/13/subscribers/detail"


def show_error_and_quit(e:Exception|str) -> None:
    print(e)
    print("\n\nFIX ERROR AND TRY AGAIN\n")
    sys.exit(1)

def get_bearer() -> str:
    ''' Gets the bearer/access token necassary for further works'''

    _payload = {
    "username": USERNAME,
    "password": PASSWORD
    }

    _headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
    }

    try:
        _response = requests.post(TOKEN_URL, json=_payload, headers=_headers)
    except Exception as e:
        show_error_and_quit(e)

    data = _response.json()

    access_token = data.get("access_token")
    if access_token:
        print("[BEARER SUCESSFULLY LOCATED]")
        return access_token
    else:
        show_error_and_quit("Couldn't Recieve access token")

def get_data(bearer:str) -> None:
    '''Gets user data abd subscription info through bearer ID and shows them'''

    def safe_print(label, value):
        '''Prints the Labels and values safely'''
        if value not in (None, "", []):
            print(f"{label}: {value}")


    _headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": f"Bearer {bearer}", 
    "Origin": "https://wifinepal.gispaas.geniussystems.com.np",
    "Referer": "https://wifinepal.gispaas.geniussystems.com.np/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5) AppleWebKit/537.36 Chrome/142.0.0.0 Mobile Safari/537.36"
    }

    try:
        _response = requests.get(INFO_URL, headers=_headers)
    except Exception as e:
        show_error_and_quit("Couldn't fetch User info")

    data =  _response.json()

    print("\n===== SUBSCRIBER DETAILS =====")

    safe_print("Subscriber ID", data.get("id"))
    safe_print("Full Name", data.get("full_name"))
    safe_print("Username", data.get("username"))
    safe_print("Email", data.get("email"))
    safe_print("Mobile", data.get("mobile"))
    safe_print("Address", data.get("address"))
    safe_print("Account Type", data.get("account_type"))
    safe_print("Connection Type", data.get("connection_type"))
    safe_print("Created At", data.get("created_at"))
    safe_print("Last Login", data.get("last_login_at"))
    
    print("\n===== SUBSCRIPTION DETAILS =====")

    subscription = data.get("subscription", {})
    if subscription:
        safe_print("Package ID", subscription.get("package_id"))
        safe_print("Subscription Status", subscription.get("status_label"))
        safe_print("Start Date", subscription.get("start_date"))
        safe_print("Expiry Date", subscription.get("expiry_date"))
        safe_print("Remaining Days", subscription.get("remaining_days"))
        safe_print("Internet Remaining Days", subscription.get("internet_remaining_days"))
        safe_print("Upload Speed (bps)", subscription.get("up"))
        safe_print("Download Speed (bps)", subscription.get("down"))




bearer = get_bearer()
get_data(bearer)


quit()

# for password change
#######https://ftth.beta.gispaas.geniussystems.com.np/subscriber/ftth/v2/tenants/13/acs/-/subscriber-service/120368

URL = "https://ftth.beta.gispaas.geniussystems.com.np/subscriber/ftth/v2/tenants/13/acs/-/subscriber-service/120368"
bearer = access_token

ans = input("Do you want to change the Wi-Fi password? (yes/no): ").strip().lower()
if ans != "yes":
    print("Aborted. No request sent.")
    sys.exit(0)

password = input("Enter new Wi-Fi password: ").strip()
confirm = input("Are you sure? Type YES to confirm: ").strip()

if confirm != "YES":
    print("Cancelled.")
    sys.exit(0)

headers = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "authorization": f"Bearer {bearer}",
    "origin": "https://wifinepal.gispaas.geniussystems.com.np",
    "referer": "https://wifinepal.gispaas.geniussystems.com.np/",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36",
}

payload = {
    "ssid_2": {
        "ssid": USERNAME,
        "wifi_password": password,
        "wifi_enabled": True,
        "ssid_broadcast": True
    }
}



resp = requests.patch(
    URL,
    headers=headers,
    data=json.dumps(payload),
    timeout=25
)

print(resp.status_code)
print(resp.json())
print("CHANGED")


    

