from sys import platform
from os import system
import requests
import re
import threading
import time
from colorama import Fore, Style

class ItemsatisOneCikarmaBot:
    def __init__(self):
        self.clear()
        system('title Made By sadrazam1221 discord.gg/naz')
        self.ad_list = list()


        with open('yükseltilicekilanlar.txt', 'r', encoding='utf-8') as file:
            for ad in file.read().split('\n'):
                self.ad_list.append(re.search('(\d+)\.html$', ad).group(1))

    def clear(self):
        if platform.startswith('win'):
            system('cls')
        else:
            system('clear')

    def process(self):
        while True:
            for ad in self.ad_list:
                self.highlight_ad(ad)
            time.sleep(5420)

    def highlight_ad(self, ad):
        try:
            cookies = {
                'PHPSESSID': 'dltmb8aa1b6ichgis60raabkcp',
            }

            headers = {
                'authority': 'www.itemsatis.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.itemsatis.com',
                'referer': 'https://www.itemsatis.com/ilanlarim.html',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'Id': ad,
            }

            response = requests.post('https://www.itemsatis.com/api/moveUpPost', cookies=cookies, headers=headers, data=data, timeout=60)

            if response.json()['success'] == True:
                print(f'{Fore.GREEN}✓ İlan başarıyla öne çıkarıldı: {ad}{Style.RESET_ALL}')
                print('-' * 25)
                subprocess.run(["python", "main.py"])
            else:
                print(f'{Fore.RED}X Hata: {response.json()["message"]}{Style.RESET_ALL}')
                subprocess.run(["python", "main.py"])

        except Exception as e:
            print(f'{Fore.RED}X Hata: {response.json()["message"]}{Style.RESET_ALL}')
        except:
            pass
            subprocess.run(["python", "main.py"])

bot = ItemsatisOneCikarmaBot()
bot.process()