import requests
import json
import sys
from dotenv import load_dotenv
import os 

load_dotenv()


# for token
URL = "https://subscribers.beta.gispaas.geniussystems.com.np/subscriber/authentication/v1/tenants/13/subscribers/access-token"

payload = {
    "username": os.getenv("SSID"),
    "password": os.getenv("PASSWORD")
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(URL, json=payload, headers=headers)



data = response.json()

access_token = data.get("access_token")
token_type = data.get("token_type")
expires_in = data.get("expires_in")
refresh_token = data.get("refresh_token")

print("\n===== GOT TOKEN INFO =====")

# for data

url = "https://subscribers.beta.gispaas.geniussystems.com.np/subscriber/account/v1/tenants/13/subscribers/detail"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": f"Bearer {access_token}", 
    "Origin": "https://wifinepal.gispaas.geniussystems.com.np",
    "Referer": "https://wifinepal.gispaas.geniussystems.com.np/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5) AppleWebKit/537.36 Chrome/142.0.0.0 Mobile Safari/537.36"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)


data = response.json()

def safe_print(label, value):
    if value not in (None, "", []):
        print(f"{label}: {value}")



print("\n===== SUBSCRIBER DETAILS =====")

safe_print("Subscriber ID", data.get("id"))
safe_print("Full Name", data.get("full_name"))
safe_print("Username", data.get("username"))
safe_print("Email", data.get("email"))
safe_print("Mobile", data.get("mobile"))
safe_print("Alternate Mobile", data.get("mobile_alt"))
safe_print("Phone", data.get("phone"))
safe_print("Address", data.get("address"))
safe_print("Account Type", data.get("account_type"))
safe_print("Connection Type", data.get("connection_type"))
safe_print("Status", data.get("status"))
safe_print("Created At", data.get("created_at"))
safe_print("Last Login", data.get("last_login_at"))


region = data.get("region")
if region:
    safe_print("Region", region.get("name"))


macs = data.get("macs", [])
if macs:
    mac_list = [m.get("mac") for m in macs if m.get("mac")]
    safe_print("MAC Address(es)", ", ".join(mac_list))


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
        "ssid": "kushal50_wnepal",
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


    

