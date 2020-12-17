import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):

        hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
        data['password'] = hashed

        id = self.Users.insert(data)
        print('uid is', id)
        myuser = self.Users.find_one({"firstName": data['firstName']})

        if bcrypt.checkpw("avocado1".encode(), myuser['password']):
            print("MATCH FOUND")