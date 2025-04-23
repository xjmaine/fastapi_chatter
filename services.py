from datetime import datetime, timezone

from fastapi import HTTPException
from starlette import status

from python_fastapi.helper_functions import get_user_from_list
from python_fastapi.models import User
from python_fastapi.schemas import UpdateUserSchema


def update_a_user(
        user_id: int,
        user_update_data: UpdateUserSchema,
        users_list: list[dict]
) -> User:
    """
    Update an existing user in the users list.
    
    :param user_id: The id of the user to update
    :param user_update_data: The data to update the user with
    :param users_list: The list of users to update the user in
    :return: The updated user
    """

    user = get_user_from_list(user_id, users_list)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    user_obj = User.create_instance( ** user)

    for key, value in user_update_data.model_dump().items():
        if hasattr(user_obj, key):
            setattr(user_obj, key, value)

    user_obj.updated_at = str(datetime.now(tz=timezone.utc))

    return user_obj