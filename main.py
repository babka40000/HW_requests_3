import requests

if __name__ == '__main__':
    url = "https://api.stackexchange.com/2.3/questions"
    params = {"fromdate": "2022-05-13", "todate": "2022-05-15", "tagged": "Python", "site": "stackoverflow"}

    response = requests.get(url, params=params)
    response_json = response.json()

    for item in response_json['items']:
        print(item["link"])

    print(f"Нашлось {len(response_json['items'])} статей")