import uvicorn
from fastapi import FastAPI, Body

app = FastAPI() #instance of fastAPI

users = [
    {
        "id": 1,
        "name": "Freddie",
        "city": "Ontario",
        "gender": "male",
        "email": "freddie@app.com"
    },
    {
        "id": 2,
        "name": "Aisha",
        "city": "Accra",
        "gender": "female",
        "email": "aisha@app.com"
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
    user = get_user_from_uniqueness(user.get("email"), users)
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

@app.put(path="/api/v1/users/{user_id}")
def update_user(user_id: int, user_update_data: dict) -> dict:
    """
    Update user by id
    :param user_update_data:
    :param user_id:
    :param user:
    :return:
    """
    user_to_update = get_user_from_list(user_id, users)
    if not user_to_update:
        return {"error": "User not found"}

    user_to_update.update(user_update_data)


def get_user_from_list(user_id: int, users_list: list[dict]) -> dict | None:
    """
    Get user from list
    :param users_list:
    :param user_id:
    :return: dict
    """
    for user in users:
        if user.get("id") == user_id:
            return user
    return None