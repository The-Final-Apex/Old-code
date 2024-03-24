#!/usr/bin/python3
from plyer import notification
import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.africanews.com'

try:
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    just_in_title = soup.find('div', attrs={'class': 'just-in__content'})

    if just_in_title is None:
        print("ERROR: Unable to find 'just-in__title' section on Africanews website.")
    else:
        article_title = just_in_title.text.strip()

        # Extract the title text from the `a` tag inside the `h3` tag
except requests.exceptions.RequestException as e:
    print("ERROR: Failed to connect to Africanews website. Please check your internet connection and try again.")


while True:
    news_file = open("news.txt", "w")
    news_file.write("\n\nAfrica news: " + article_title)
    news_file.close()
    notification.notify(
        title = 'Latest Ethan News',
        message = f"Africanews: {article_title}",
        app_icon = "/home/em_coda/PycharmProjects/Cars/ggg/favicon.ico",
        timeout = 10,
    )

    time.sleep(3600)
