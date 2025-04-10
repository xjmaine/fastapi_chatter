import uvicorn
from fastapi import FastAPI, Body

app = FastAPI() #instance of fastAPI

users = [
    {
        "id": 1,
        "name": "Freddie",
        "city": "Ontario",
        "gender": "male"
    },
    {
        "id": 2,
        "name": "Aisha",
        "city": "Accra",
        "gender": "female"
    },
    {
        "id": 3,
        "name": "Kwame",
        "city": "Kumasi",
        "gender": "male"
    },
    {
        "id": 4,
        "name": "Sarah",
        "city": "London",
        "gender": "female"
    },
    {
        "id": 5,
        "name": "David",
        "city": "Adenta",
        "gender": "male"
    },
    {
        "id": 6,
        "name": "Fatou",
        "city": "Paris",
        "gender": "female"
    }
]
@app.get(path="/api/v1/users")
def get_all_users() -> list[dict[str, str | int]]:
    """
    Test route to check if server is running
    :return: String
    """
    # return {"message": "Hello FastAPI"}
    return users

@app.get(path="/api/v1/users/{user_id}")
def get_user(user_id: int)->dict:
    """
    Get user by id
    :param user_id:
    :return: dict
    """
    print(type(user_id))
    for user in users:
        if user.get("id") == user_id:
            return user
    return {"error": "user id not found!"}

@app.post(path="/api/v1/users")
def create_user(user: dict = Body()) -> dict:
    """
    Create a new user
    :param user:
    :return:
    """
    # check if email is unique
    for existing_user in users:
        if existing_user.get("email") == user.get("email"):
            return {"error": "Email already exists"}

    user["id"] = len(users) + 1
    users.append(user)

    return user

