def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return db.execute(query)

def divide(a, b):
    return a / b

def process_items(items):
    for i in range(len(items) + 1):
        print(items[i])
