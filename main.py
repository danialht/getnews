import sys
import requests
from bs4 import BeautifulSoup, Tag
from datetime import date
import getch
from typing import Generator

def delete_last_line():
    "Use this function to delete the last line in the STDOUT"
    #cursor up one line
    sys.stdout.write('\x1b[1A')
    #delete last line
    sys.stdout.write('\x1b[2K')

def get_nonempty_sections(url: str) -> Generator:
    """
    Returns a generator for articles found in the url.
    """
    request = requests.get(url)
    page_content = request.content
    soup = BeautifulSoup(page_content, 'html.parser')
    all_sections = soup.find_all('section')
    for section in all_sections:
        if len(section):
            yield section

def print_article(article: Tag) -> None:
    print(article.a.text)
    print(article.div.text)

def print_section(section: Tag) -> bool:
    """
    Outputs a section on terminal and returns True if the user
    wants to continue getting feed or False otherwise (in case
    of keyboard interrupts like cntrl-C or pressing Q)
    """
    print(section.header.text, '\n')
    articles = section.find_all('article')
    for article in articles:
        print_article(article)
        try:
            # Getting input for next article
            # TODO: change background to black and text to white for this
            print('Q: EXIT | OTHER KEYS: NEXT ARTICLE')
            char = getch.getch()
            if char == 'q' or char == 'Q':
                delete_last_line()
                return False
        except:
            # For cases like key interrupts
            delete_last_line()
            return False
        delete_last_line()
        print('')
    return True

def main():
    today_date = date.today()
    
    url = "https://tldr.tech/tech/" + today_date.strftime("%Y-%m-%d")
    
    for section in get_nonempty_sections(url):
        if not print_section(section):
            break

if __name__ == "__main__":
    main()

    