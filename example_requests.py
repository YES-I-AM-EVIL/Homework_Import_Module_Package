import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Данные успешно получены")
        print(response.text)
    else:
        print(f"Ошибка при получении данных: {response.status_code}")

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts'
    fetch_data(url)
