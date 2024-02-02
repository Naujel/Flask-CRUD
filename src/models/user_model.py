from .entities.user_entitie import User
from database.database import db_connection

class UserModel:

    @classmethod
    def getUsers(self):
        connection = db_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM USERS ORDER BY username ASC")
            result = cursor.fetchall()

        connection.close()
        return result
    
    @classmethod
    def getUser(self, id):
        connection = db_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM USERS WHERE id=%s", (id))
            result = cursor.fetchone()

        connection.close()
        return result
    
    @classmethod
    def addUser(self, user):
        connection = db_connection()

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO USERS (id, username, email, login_date) VALUES (%s, %s, %s, %s)", (user.id, user.name, user.email, user.date))
            result = cursor.rowcount
            connection.commit()

        connection.close()
        return result
    
    @classmethod
    def deleteUser(self, id):
        connection = db_connection()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM USERS WHERE id=%s", (id))
            result = cursor.rowcount
            connection.commit()

        connection.close()
        return result
    
    @classmethod
    def updateUser(self, user):
        connection = db_connection()

        with connection.cursor() as cursor:
            cursor.execute("UPDATE USERS SET username=%s, email=%s WHERE id=%s", (user.name, user.email, user.id))
            result = cursor.rowcount
            connection.commit()

        connection.close()
        return result

    @classmethod
    def getUserDate(self, id):
        connection = db_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT login_date FROM USERS WHERE id=%s", (id))
            result = cursor.fetchone()
            connection.commit()

        connection.close()
        return result[0]