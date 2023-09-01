import os
from rich.console import Console
from requests_html import HTMLSession
from lib import account



session = HTMLSession()
console = Console()

def create_account(limit:int, server:str = 'tr', email:str="gmail.com"):
    try:
        runner = 0
        account_list = []

        while runner < limit:
            runner += 1
            proxy = {
                "http": "http://karadenizemirr:karadeniz75_streaming-1@geo.iproyal.com:12321",
                "https":"http://karadenizemirr:karadeniz75_streaming-1@geo.iproyal.com:12321"
            }
            session.proxies = proxy
            ip_response = session.get('https://api.ipify.org')
            console.print(f'\n[bold green]Your IP Address:[/bold green] [bold blue]{ip_response.text}[/bold blue]\n')
            response = session.get(f'https://{server}.metin2.gameforge.com/landing/partner')
            response.html.render()

            # Get Post Parameters
            bb_field = response.html.find('input[name="bb_field"]', first=True).attrs['value']
            action = response.html.find('form', first=True).attrs['action']

            # Create Account Info
            email = account.create_email(email_pass=email, len=10)
            password = account.create_password(len=10)
            account_list.append(f"{email}:{password}")

            params = {
                "bb_field": bb_field,
                "tac":"tac",
                "email": email,
                "password": password,
                "SubmitRegisterForm": ""
            }

            register_response = session.post(action, data=params, allow_redirects=False)
    

            if register_response.status_code == 303:
                console.print(f'[bold green]Account created successfully.[/bold green] [bold blue]{email}:{password}[/bold blue]')

        console.print(f'[bold green]Account creation process completed.[/bold green] [bold blue]{len(account_list)}[/bold blue] accounts created.\n')
        return account_list

    except Exception as e:
        console.print('[bold red]An error occurred while creating the account.Please try again.[/bold red]\n', e)