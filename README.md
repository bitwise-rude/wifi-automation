# WIFI - Automation Tool
## WHAT is this?

Wifi-Nepal is a really cheap ISP service I use, but they don't provide
router-admin page privileges to change SSID and password or even view your subscription
, balance, etc.

Instead, you have to go their site, login at their website (super slow and tedious)
and use IPGEAR service to change stuff.

The IPGEAR service is really fast though, only the website login sucks even though
the same authentication is used.

This is the ultimate solution. Directly send requests with appropriate BEARED or Access_token
generated from your password and get information and change password, SSID easily

## How to use?
1. Install Python
2. Clone this repo 
3. Run `pip install requirements.txt`
4. Create a `.env` file in the same directory
5. Create field `SSID = "<your ssid>"` and `PASSWORD = "<your password>"` and 
save the file
6. OR you can go to `main.py` and change the variables `PASSWORD` to password and `USERNAME` to SSID respectively to accomplish the goal of above point.
6. Run the script `main.py`

viola! now you can use the script again and again without having to update
authentication always

### Keep in mind that the password you save in the environment file is your login password



