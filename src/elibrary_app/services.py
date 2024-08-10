import requests


def get_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')

    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = 'Sorry'

    return joke


if __name__ == '__main__':
    print(get_joke())