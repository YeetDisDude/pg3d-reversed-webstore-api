import httpx
import base64
import json
import random
print("Made by: YeetDisDude\n")

PROJECT_ID = 196500
MERCHANT_ID = 319917

country_codes = ["TH", "EN", "US", "CA", "FR", "DE", "IT", "JP", "CN", "IN", "BR", "MX", "AR", "AU", "NZ", "ZA", "EG", "SA", "RU", "UA", "TR", "GR", "ES", "PT", "NL", "BE", "SE", "NO", "FI", "DK", "PL", "CZ", "HU", "AT", "CH", "IE", "GB", "IS", "NO", "SE", "FI", "DK", "EE", "LV", "LT", "BG", "RO", "HR", "RS", "SI", "SK", "MK", "BA", "ME", "AL", "XK", "RS", "SI", "HR", "RO", "BG", "UA", "BY", "MD", "KZ", "UZ", "TM", "KG", "TJ", "AM", "AZ", "GE", "IL", "LB", "JO", "IQ", "KW", "BH", "QA", "OM", "AE", "YE", "SY", "PS", "SA", "EG", "SD", "LY", "TN", "DZ", "MA", "PT", "ES", "FR", "MC", "IT", "SM", "VA", "MT", "GR", "CY", "MK", "BG", "RO", "UA", "BY", "MD", "RU", "KZ", "UZ", "TM", "KG", "TJ", "AM", "AZ", "GE", "TR", "IR", "AF", "PK", "NP", "BD", "LK", "MV", "MY", "SG", "BN", "ID", "PH", "TH", "VN", "KH", "LA", "MM", "BN", "BD", "NP", "LK", "IN", "PK", "AF", "IR", "IQ", "JO", "LB", "SY", "IL", "PS", "QA", "BH", "KW", "AE", "OM", "SA", "YE", "ER", "DJ", "SO", "ET", "KE", "UG", "RW", "TZ", "BI", "MW", "MZ", "ZM", "ZW", "NA", "BW", "ZA", "LS", "SZ", "IN", "LK", "NP", "BD", "BT", "MV", "PK", "AF", "IR", "IQ", "JO", "LB", "SY", "IL", "PS", "QA", "BH", "KW", "AE", "OM", "SA", "YE", "ER", "DJ", "SO", "ET", "KE", "UG", "RW", "TZ", "BI", "MW", "MZ", "ZM", "ZW", "NA", "BW", "ZA", "LS", "SZ", "LS", "SZ", "GR", "TR", "CY", "MT", "VA", "IT", "SM", "SM", "VA", "MT", "MT", "GR", "ES", "PT", "FR", "MC", "AD", "MC", "AD", "AD", "ES", "PT", "VA", "SM", "IT", "MT", "CY", "TR", "GE", "AZ", "AM", "RU", "KZ", "UZ", "TJ", "KG", "TM", "UZ", "KZ", "RU", "TJ", "KG", "TM", "AM", "AZ", "GE", "LB", "SY", "IQ", "IR", "AE", "OM", "BH", "KW", "QA", "SA", "YE", "YE", "PS", "IL", "JO", "LB", "SY", "IQ", "KW", "BH", "QA", "OM", "AE", "SA", "EG", "LY", "LY", "EG", "SD", "LY", "EG", "LY", "TN", "DZ", "TN", "MA", "MA", "PT", "ES", "AD", "MC", "IT", "VA", "SM", "MT", "CY", "TR", "UA", "BG", "RO", "MK", "AL", "ME", "RS", "XK", "MK", "XK", "XK", "XK", "XK", "XK", "XK"]
itemData = {
    "Gems": {
        "item_id": 455578,
        "sku": "2015"
    },
    "Coins": {
        "item_id": 455579,
        "sku": "1015"
    },
    "Keys": {
        "item_id": 455580,
        "sku": "6015"
    },
    "PP Tickets": {
        "item_id": 455581,
        "sku": "26015"
    },
    "Coupons": {
        "item_id": 455582,
        "sku": "7015"
    },
    "Booster 100%": {
        "item_id": 455583,
        "sku": "3030"
    },
    "Booster 200%": {
        "item_id": 455584,
        "sku": "4030"
    },
    "freeChest": {
        "item_id": 505329,
        "sku": "121027"
    }
}

def decode_token(token):
    token = token.split(".")[1] + "=="
    decoded_token = base64.urlsafe_b64decode(token).decode("utf-8")
    decoded_data = json.loads(decoded_token)
    return decoded_data

def getToken(id: str):
    payload = {
        "settings": {
            "projectId": PROJECT_ID,
            "merchantId": MERCHANT_ID
        },
        "loginId": "ee2f78e4-2f53-4a29-b26f-c4911cacb2ab",
        "webhookUrl": "https://offerwall-currency.lightmap.com/xsolla/login",
        "user":{
                "id": id,
                "country": random.choice(country_codes)
        },
        "isUserIdFromWebhook": False
    }
    r = httpx.post("https://sb-user-id-service.xsolla.com/api/v1/user-id",json=payload)
    rawToken = json.loads(r.text)["token"]
    return rawToken

def getUsernameFromToken(token: str):
    decodedToken = decode_token(token)
    username = json.loads(decodedToken['payload'])['userInfo']['name']
    return username

def getEmailFromToken(token: str):
    decodedToken = decode_token(token)
    email = str(decodedToken["email"])
    if email == "":
        return "None"
    else:
        return email

def freeChest(token: str):
    url = f"https://store.xsolla.com/api/v2/project/{PROJECT_ID}/free/item/{itemData['freeChest']['sku']}"
    headers= {"Authorization": f"Bearer {token}"}
    r = httpx.post(url, json={}, headers=headers)
    jsonStr = json.loads(r.text)
    try:
        jsonStr["order_id"] # check if free chest was a success
        return True
    except KeyError:
        return False
    
token = getToken("298922020")


