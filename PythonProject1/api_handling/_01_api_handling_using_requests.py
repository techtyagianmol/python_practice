import random

import requests


def fetch_user_data_pypi():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()

    if data.get("statusCode") == 200:
        user_data = random.choice(data["data"]["data"])
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return user_name, country,
    else:
        raise Exception("Something went wrong to fetch user data")


def main():
    try:
        user_name, country = fetch_user_data_pypi()
        print(f"user_name: {user_name}, \ncountry: {country}")
    except Exception as error:
        print(error)



if __name__ == "__main__":
    main()
