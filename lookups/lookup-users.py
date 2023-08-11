# Lookups primarily make use of hashing and dictionaries
# If you are interested in how these work under the hood
# Check out our hashing article here: https://schulichignite.com/blog/verifying-quickly
from __future__ import annotations
import uuid
from dataclasses import dataclass

database = dict() # Stores users with a unique ID
email_to_id = dict() # Links emails to unique ID's

# This means we only need to know someone's email to lookup
# Their information directly instead of searching a list!

@dataclass
class User:
    name:str
    age:int
    birthday:str
    email:str
    phone:str
    
    def __post_init__(self):
        # Add user to database and email_to_id after creation
        user_id = str(uuid.uuid4())
        email_to_id[self.email] = user_id
        database[user_id] = self

def find_user_by_email(email:str) -> User:
    """Finds a User by email

    Parameters
    ----------
    email : str
        The email to find

    Returns
    -------
    User
        The user information associated with the email
    """
    user_id = email_to_id[email]
    return database[user_id]

if __name__ == "__main__":
    User("Kieran Wood", 24, "Jan 1st 2023", "kieran@canadiancoding.ca", "+1(123)123-1234")
    print(email_to_id)
    print(database)

    User("Jamie Avernus", 26, "March 4th 2023", "jamie@example.com", "+1(403)123-1234")
    print(email_to_id)
    print(database)