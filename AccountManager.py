from utils import create_connection, hash_data


def check_user_doesnt_exist(user:tuple, cursor):
    if not user:
        cursor.close()
        raise Exception("User Doesn't Exists")

def create_acc(username:str, password:str, db_connection=None):
    db_cursor = db_connection.cursor()
    db_cursor.execute(""" SELECT * FROM users WHERE username=? """, (username, ))

    if db_cursor.fetchone():
        db_cursor.close()
        raise Exception("User Already Exists")
    
    db_cursor.execute(""" INSERT INTO users (username, password) VALUES (?, ?) """, (username, hash_data(password)))
    db_cursor.close()

def login_acc(username:str, password:str, db_connection=None):
    db_cursor = db_connection.cursor()
    db_cursor.execute(""" SELECT * FROM users WHERE username=? """, (username, ))
    user = db_cursor.fetchone()
    
    check_user_doesnt_exist(user, db_cursor)

    db_cursor.close()

    if hash_data(password) != user[1]:
        return False
    
    return True
    
def reset_pass(username:str, password:str, new_password:str, db_connection=None):
    db_cursor = db_connection.cursor()
    db_cursor.execute(""" SELECT * FROM users WHERE username=? """, (username, ))
    user = db_cursor.fetchone()
    
    check_user_doesnt_exist(user, db_cursor)

    if hash_data(password) != user[1]:
        return False
    
    db_cursor.execute(""" UPDATE users SET password=? WHERE username=? """, (hash_data(new_password), username))
    db_cursor.close()

    return True


if __name__ == "__main__":
    with create_connection() as con:
        con.cursor().execute(""" CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT) """)
        # create_acc("Lucky13", "1234546", con)
        print(login_acc("Lucky13", "1234546", con))
        print(reset_pass("Lucky13", "1234546", "MyBad", con))