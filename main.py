import requests
from bs4 import BeautifulSoup
import re
import fs
from colorama import Fore, Style
from rich import print
import pyfiglet
import time
import os

# Vanity
os.system('clear')
title = pyfiglet.figlet_format('AUTO-WGET', font='puffy', justify="center")
print(f'[bold magenta]{title}[/bold magenta]')
print(f'[green]Created by [/green][bold cyan]Rednotsus[/bold cyan]')
print("      ")
print("       ")
start_time = time.time()
print(f"[yellow][ AUTO-WGET ]  |  Starting auto-wget")
print(f"[yellow][ AUTO-WGET ]  |  Please enter the URL of the website you want to download from")
url = input()

print(f"[yellow]p AUTO-WGET ]  |  Scraping website...")
file = open("wget.sh", "a")

source = requests.get(url).text
episodes = 0

soup = BeautifulSoup(source, 'html.parser')
name_divs = soup.find_all('div', class_='centerflex name-div')

for div in name_divs:
    episodes += 1
time.sleep(0.5)
print(f"[green][ AUTO-WGET ]  |  Scraped {episodes} episodes")
print(f"[yellow][ AUTO-WGET ]  |  Generating wget script...")
time.sleep(0.5)


for div in name_divs:
    a_tag = div.find('a')
    if a_tag:
        name = a_tag.text
        if "Parent Directory" not in name:
            match = re.match(r"(.*).S(\d{2})E(\d{2}).*", name, re.IGNORECASE)
            if match:
                series_name, season, episode = match.groups()
                series_name = series_name.replace('.', ' ')
                formatted_name = f"{series_name} - S{season}E{episode}"
                link = "https://vadapav.mov" + a_tag['href']
                file.write(f"wget '{link}' -O '{formatted_name}.mkv'\n")
                print(f"[green][ AUTO-WGET ]  |  Added {formatted_name}")
                time.sleep(0.025)
            size_div = div.find_next_sibling('div', class_='size-div')
            if size_div:
                mbsize = round(int(size_div.text)/1048576)
gbsize = round(mbsize/1024, 2)
elapsed_time = float(time.time() - start_time)
print(f"[yellow][ AUTO-WGET ]  |  Generated wget script at wget.sh")
time.sleep(0.5)
print(f"[green][ AUTO-WGET ]  |  Done, Completed in {elapsed_time} seconds")
print(f"[green][ AUTO-WGET ]  |  Total Size for {episodes} episodes: {gbsize} GB")
print(f"[green][ AUTO-WGET ]  |  Press enter to quit...")
input(f"    >    ")
if input() == " ":
    os.system('clear')
    time.sleep(0.5)
    exit()

file.close()
