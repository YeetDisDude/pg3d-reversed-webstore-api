import api

id = 297974000 

while True:
    token = api.getToken(str(id))
    decoded_token = api.decode_token(token)
    username = api.getUsernameFromToken(token)
    status = api.freeChest(token)
    
    print(f"ID: {id} | Username: {username} | Free Chest Status: {'Success' if status == True else 'Failed (cooldown)'}")
    id += 1
    