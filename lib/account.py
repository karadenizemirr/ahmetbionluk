import random
import string
from rich.console import Console
console = Console()

def create_keyword(len:int):
    try:
        keyword = ''.join(random.choices(string.ascii_letters + string.digits, k=len))
        return keyword
    except Exception as e:
        print(e)

def create_email(email_pass:string, len:int):
    try:
        email = create_keyword(len=len) + '@' + email_pass
        return email
    except:
        console.print('[bold red]An error occured while creating email.[/bold red]')


def create_password(len:int):
    try:
        password = create_keyword(len=len)
        return password
    except:
        console.print('[bold red]An error occured while creating password.[/bold red]')