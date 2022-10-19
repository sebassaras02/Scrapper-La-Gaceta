import requests
import lxml.html as html
from datetime import date
import os

HOME_URL = 'https://lagaceta.com.ec/'

XPATH_IMAGES_LINK = '//h3[@class = "entry-title td-module-title"]/a/@href'
XPATH_TITLE_LINK = '//h1[@class ="entry-title"]/text()'
XPATH_PARAGRAPHS_LINK = '//div[@class = "td-post-content"]/p/text()'

def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)
            try:
                title = parsed.xpath(XPATH_TITLE_LINK)[0]
                title = title.replace('\"', '')
                paragraph = parsed.xpath(XPATH_PARAGRAPHS_LINK)
            except IndexError:
                return

            with open(f'{today}/{title}.txt', 'w', encoding = 'utf-8') as f:
                f.write(title)
                f.write("\n\n")
                for p in paragraph:
                    f.write(p)
                    f.write("\n")
        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as ve:
        print(ValueError)


def link_images():
    try:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        response = requests.get(HOME_URL, headers = headers)
        if response.status_code == 200:
            # get the html file
            home = response.content.decode('utf-8')
            # transform from html to a xpath file compatible
            parsed = html.fromstring(home)
            links_to_images = parsed.xpath(XPATH_IMAGES_LINK)
            today = date.today().strftime('%d-%m-%Y')
            # print(links_to_images)
            if not os.path.isdir(today):
                os.mkdir(today)
            for link in links_to_images:
                parse_notice(link, today)


        else:
            raise ValueError(f"Error: {response.status_code}")
    except ValueError as ve:
        print(ve)

def run():
    link_images()


if __name__ == "__main__":
    run()
