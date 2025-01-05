from bs4 import BeautifulSoup, Tag
import sys
import requests
from typing import Generator
from getch import getch
import ANSIEscapeCodes

def delete_last_lines(count: int) -> None:
    """Use this function to delete the last line in the STDOUT using ansi escapse codes"""
    for _ in range(count):
        #cursor up one line
        sys.stdout.write(ANSIEscapeCodes.CURSOR_UP)
        #delete last line
        sys.stdout.write(ANSIEscapeCodes.DEL_LINE)

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
    """
    Printing the article 
    """
    print("" + article.a.text)
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
            # Printing the text with negative colors in background and foreground
            # \033[3m is the Ansi escape code for it
            print('\n\033[7mQ: EXIT | OTHER KEYS: NEXT ARTICLE\033[0m')
            char = getch()
            if char == 'q' or char == 'Q':
                delete_last_lines(2)
                return False
        except:
            # For cases like key interrupts
            delete_last_lines(2)
            return False
        delete_last_lines(2)
        print('')
    return True
