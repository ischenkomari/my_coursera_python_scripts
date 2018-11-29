import requests

def get_location_info():
    return requests.get("http://ip-api.com/json").json()['country']

if __name__ == "__main__":
    print(get_location_info())
