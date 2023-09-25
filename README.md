# pg3d reversed webstore api
 Pixel Gun 3D's reversed webstore api made in Python.
# example usage:
```py
import api

# getting a token from user ID
token = api.getToken("297974059")
print("Token: " + token + "\n")

# getting a username from a token
username = api.getUsernameFromToken(token)
print("Username" + username + "\n")

# getting an email from a token, will only work if the user has bought something from the web store
email = api.getEmailFromToken(token)
print("Email: " + email + "\n")

# give free chest
status = api.freeChest(token)
print("Free chest status: " + str(status))
```
