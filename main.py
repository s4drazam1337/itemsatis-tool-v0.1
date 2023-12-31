from colorama import init, Fore, Style
import subprocess
import time
import os

init()

print(" ")
print(" ")
print(f'{Fore.BLUE}  ░▀░ ▀▀█▀▀ █▀▀ █▀▄▀█ █▀▀ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀   ▀▀█▀▀ █▀▀█ █▀▀█ █░░   ▀█░█▀ █▀▀█ ░ ▄█░')
print(f'{Fore.BLUE}  ▀█▀ ░░█░░ █▀▀ █░▀░█ ▀▀█ █▄▄█ ░░█░░ ▀█▀ ▀▀█   ░░█░░ █░░█ █░░█ █░░   ░█▄█░ █▄▀█ ▄ ░█░')
print(f'{Fore.BLUE}  ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀   ░░▀░░ ▀▀▀▀ ▀▀▀▀ ▀▀▀   ░░▀░░ █▄▄█ █ ▄█▄')
print(f'{Fore.MAGENTA}                                                                                        Made By Sadrazam1221')

def main():
    print(" 1. İlan Yükseltme")
    print(" 2. İlan Silme")
    print(" 3. Ekranı Temizle")
    print(" ")
    
    secim = input("Lütfen bir seçenek girin (1 veya 2): ")

    if secim == "1":
        ilanyukseltme()
    elif secim == "2":
        ilansilme()
    elif secim ==  "3":
        ekransilme()
    else:
        print("Geçersiz seçenek. Lütfen 1 veya 2 girin.")
        subprocess.run(["python", "main.py"])

def ilanyukseltme():
    time.sleep(2)
    subprocess.run(["python", "ilanyükseltme.py"])
    

def ilansilme():
    time.sleep(2)
    subprocess.run(["python", "ilansilme.py"])

def ekransilme():
    os.system('cls')
    subprocess.run(["python", "main.py"])

if __name__ == "__main__":
    main()
