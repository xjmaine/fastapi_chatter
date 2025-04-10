from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


male = Gender.MALE.name

gender = "male"

result = Gender.__contains__(gender.lower())
print(result)

for i in Gender:
    if gender.lower() == i.value:
        print(f"Found gender: {i.name}")
        break
    else:
        print("Gender not found")

