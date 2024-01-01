from sys import platform
from os import system
import requests
import re
import threading
import time
from colorama import Fore, Style
import subprocess

class ItemsatisKonuSilmeBot:
    def __init__(self):
        self.clear()
        system('title Made By sadrazam1221 discord.gg/naz')
        self.ad_list = list()


        with open('silinecekilanlar.txt', 'r', encoding='utf-8') as file:
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
                'PHPSESSID': 'ayarla',
            }

            headers = {
                'authority': 'www.itemsatis.com',
                'method': 'POST',
                'path': '/api/unPublishPost',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Content-Length': '10',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.itemsatis.com',
                'Referer': 'https://www.itemsatis.com/ilanlarim.html',
                'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            }

            data = {
                'Id': ad,
            }

            response = requests.post('https://www.itemsatis.com/api/unPublishPost', cookies=cookies, headers=headers, data=data, timeout=60)

            if response.json()['success'] == True:
                print(f'{Fore.GREEN}✓ İlan başarıyla silindi: {ad}{Style.RESET_ALL}')
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

bot = ItemsatisKonuSilmeBot()
bot.process()
