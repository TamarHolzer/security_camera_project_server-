import pypyodbc as odbc
import models.User as userModel

# פונקצית החיבור לDB
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-V6585A6\SQLEXPRESS;'
    r'DATABASE=SECURITY_CAMERA_PROJECT;'
    r'Trusted_Connection=yes;'
)


"""
פונקציה לשליפת כל המשתמשים
מחזירה רשימה עם כל המשתמשים שבסיס נתונים
"""
#פונקציה לשליפת כל המשתמשים
def get_all_users():
    try:
        conn = odbc.connect(conn_str)
        cursor = conn.cursor()

        # Execute the query to retrieve all user data
        cursor.execute("SELECT * FROM Users")

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Process the retrieved data
        users_list = []
        for row in rows:
            a_user = userModel.User(row[1], row[2], row[0])
            users_list.append(a_user)

        return users_list

    except Exception as e:
        print("Error retrieving user data:", e)
        return None

    finally:
        # Ensure the cursor and connection are closed
        try:
            cursor.close()
        except Exception as e:
            print(f"Failed to close cursor: {e}")

        try:
            conn.close()
        except Exception as e:
            print(f"Failed to close connection: {e}")


"""
פונקציה ששולפת משתמש לפי אימייל,
מקבלת מחרוזת של מייל
ומחזירה משתמש מסוד User או None
"""
#שליפת המשתמש לפי מייל
def get_user_by_email(user_email):
    try:
        conn = odbc.connect(conn_str)
        cursor = conn.cursor()

        # Execute the query to retrieve user data by ID
        cursor.execute("SELECT * FROM Users WHERE email = ?", (user_email,))

        # Fetch the row from the executed query
        row = cursor.fetchone()

        if row:
            # Create a User object from the row data
            a_user = userModel.User(row[1], row[2], row[0])
            return a_user
        else:
            print("User not found")
            return None

    except Exception as e:
        print("Error retrieving user data:", e)
        return None

    finally:
        # Ensure the cursor and connection are closed
        try:
            cursor.close()
        except Exception as e:
            print(f"Failed to close cursor: {e}")

        try:
            conn.close()
        except Exception as e:
            print(f"Failed to close connection: {e}")

# # Example usage
# user_id = "user@example.com"  # Replace with the user ID you want to search for
# user = get_user_by_email(user_id)
# if user:
#     print(f"ID: {user.id}, Email: {user.email}, Password: {user.password}")


"""
פונקציה להכנסת משתמש חדש,
הפונקציה מקבלת משתמש מסוג User
ומחזירה את פרטי המשתמש או None
"""
#פונקציה ליצירת משתמש חדש
def create_a_user(new_user):
    try:
        # Connect to the database
        conn = odbc.connect(conn_str)
        cursor = conn.cursor()

        if get_user_by_email(new_user.email) == None:
            # SQL query to insert a new user
            insert_query = f"""
                INSERT INTO Users (email, password)
                VALUES (?, ?)
                """

            # Execute the query with the new user's details
            cursor.execute(insert_query, (new_user.email, new_user.password))

            # Commit the transaction
            conn.commit()
        else:
            print("None, the email already existing")
            return None

    except odbc.Error as e:
        print(f"Error occurred: {e}")
        return e.__str__()
    finally:
        # Ensure the cursor and connection are closed
        try:
            cursor.close()
            return get_user_by_email(new_user.email)
        except Exception as e:
            print(f"Failed to close cursor: {e}")

        try:
            conn.close()
        except Exception as e:
            print(f"Failed to close connection: {e}")


"""
פונקציה להתחברות למערכת,
מקבלת משתמש מסוג User
ומחזירה את המשתמש או None
"""
#התחברות
def sign_in(user_to_login):
    is_the_user_existing = get_user_by_email(user_to_login.email)
    if is_the_user_existing == None:
        print("The user is not sign up")
        return None
    elif is_the_user_existing.password != user_to_login.password:
        print("the password is not match")
        return None
    else:
        return is_the_user_existing


# Example usage

# new_user = userModel.User(email="myemail@example.com", password="12ygRF")
# print(create_a_user(new_user))
# print(get_all_users())