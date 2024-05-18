# AUTO-WGET Script

This script is designed to scrape a website for video files and generate a wget script to download them. It's particularly useful for downloading series of videos, such as TV series episodes.

## Features

- Scrapes a website for video files
- Generates a wget script to download the video files
- Formats the video file names in the format "[Series Name] - S[season]E[episode]"
- Prints the total size of the video files to be downloaded

## Dependencies

This script requires the following Python libraries:

- requests
- BeautifulSoup
- re
- os
- colorama
- rich
- pyfiglet
- time

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 colorama rich pyfiglet
```

## Usage

Run the script:

```bash
python main.py
```

When prompted, enter the URL of the website you want to download from.

The script will scrape the website, generate a wget script, and print the total size of the video files to be downloaded.

You can then run the wget script to download the video files:

```bash
wget.sh
```

made this since i was too lazy to do it manually 

## Note

Please ensure that the structure of the HTML you're parsing matches your expectations, as BeautifulSoup relies on the specific structure of the HTML.
