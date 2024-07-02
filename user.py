from mysqlconnection import connectToMySQL
from pprint import pprint


class Users:
    _db = "users_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def retrieve_info(cls):
        """retrieve all users info from database"""
        query = "Select * FROM users;"
        list_of_dicts = connectToMySQL(Users._db).query_db(query)
        pprint(list_of_dicts)

        users = []
        for user_info in list_of_dicts:
            user = Users(user_info)
            users.append(user)
        return users

    @classmethod
    def create(cls, form_data):
        """insert a new user into the database"""
        query = """
        INSERT INTO users
        (first_name, last_name, email)
        Values
        (%(first_name)s,  %(last_name)s, %(email)s);
        """
        user_id = connectToMySQL(Users._db).query_db(query, form_data)
        return user_id

    @classmethod
    def retrieve_info_id(cls, user_id):
        """retrieve one user info from database"""
        query = "SELECT * FROM users WHERE id = (%(user_id)s);"
        data = {"user_id": user_id}
        list_of_dicts = connectToMySQL(Users._db).query_db(query, data)
        pprint(list_of_dicts)
        return Users(list_of_dicts[0])

    @classmethod
    def update(cls, form_data):
        """Update a user by id"""

        query = """
        UPDATE users
        SET
        first_name = %(first_name)s,
        last_name = %(last_name)s,
        email = %(email)s
        WHERE id = %(user_id)s;

        """
        connectToMySQL(Users._db).query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, user_id):
        """Deletes a user by id"""

        query = "DELETE FROM users WHERE id = %(user_id)s;"
        data = {"user_id": user_id}
        connectToMySQL(Users._db).query_db(query, data)
        return
