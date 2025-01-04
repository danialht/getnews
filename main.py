import sys
import requests
from bs4 import BeautifulSoup
from datetime import date
import getch

def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

def main():
    
    today_date = date.today()
    url = "https://tldr.tech/tech/" + today_date.strftime("%Y-%m-%d")

    request = requests.get(url)
    page_content = request.content
    soup = BeautifulSoup(page_content, 'html.parser')

    # sections could be Tech, science, programming, e.g. each having multiple articles
    all_sections = soup.find_all('section')
    news_sections = [section for section in all_sections if section.text]

    for section in news_sections:
        print(section.header.text, '\n')
        articles = section.find_all('article')
        for article in articles:
            print(article.a.text)
            print(article.div.text)
            try: # Getting input for next article
                # TODO: change background to black and text to white for this
                print('Q: EXIT | OTHER KEYS: NEXT ARTICLE')
                char = getch.getch()
                if char == 'q' or char == 'Q':
                    delete_last_line()
                    return
            except: # Key Interrupt
                delete_last_line()
                return
            delete_last_line()
            print('')

if __name__ == "__main__":
    main()

    