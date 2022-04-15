from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "users_schema"
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            users = []
        # Iterate over the db results and create instances of friends with cls.
            for user in results:
                users.append( cls(user) )
            return users
        return False

    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        # data is a dictionary that will be passed into the save method from server.py
        user_id= connectToMySQL(DATABASE).query_db( query, data )
        return user_id 

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result= connectToMySQL(DATABASE).query_db( query, data )
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query= "UPDATE users SET first_name= %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id =%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data:dict):
        query= "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)