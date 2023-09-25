import api

def generate_user_table(username, id, email, uninit, tried):
    table_row = "{:<25} | {:<25} | {:<25} | {:<25} | {:<25}".format(username, id, email, uninit, tried)
    return table_row

id = 297974000 # start from this id
uninit = 0 # count of players with "new_player" as their name
tried = 0

print("{:<25} | {:<25} | {:<25} | {:<25} | {:<25}".format('Username', 'ID', 'Email', 'Uninit', 'Tried'))
while True:
    tried += 1
    token = api.getToken(str(id))
    username = api.getUsernameFromToken(token)
    email = api.getEmailFromToken(token)
    if username == "new_player":
         uninit += 1
    table_row = generate_user_table(username, id, email, uninit, tried)
    print(table_row)
    id += 1
    