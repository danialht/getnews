from datetime import date
from utils import get_nonempty_sections, print_section

def main():
    """
    Getting the news from newsletter website(s) and printing them
    on the terminal screen.
    """
    today_date = date.today()
    
    # url = "https://tldr.tech/tech/" + today_date.strftime("%Y-%m-%d")
    url = "https://tldr.tech/tech/2025-01-03"

    for section in get_nonempty_sections(url):
        if not print_section(section):
            break

if __name__ == "__main__":
    main()
