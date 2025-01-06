from datetime import date
from utils import get_nonempty_sections, print_section
from rich.console import Console

def main():
    """
    Getting the news from newsletter website(s) and printing them
    on the terminal screen.
    """
    today_date = date.today()
    
    url = "https://tldr.tech/tech/" + today_date.strftime("%Y-%m-%d")
    print(url)
    console = Console()

    for section in get_nonempty_sections(url):
        if not print_section(section, console):
            break

if __name__ == "__main__":
    main()
