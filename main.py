from app.api_client import ApiClient
from app.menu import Menu


if __name__ == "__main__":

    url_adress = "https://jsonplaceholder.typicode.com"

    api_client = ApiClient(url_adress)

    menu = Menu(api_client)
    menu.run()
