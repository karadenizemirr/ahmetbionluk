from rich.console import Console
from lib.operations import create_account

console = Console()


console.print('[bold green]Account Creator App[/bold green]\n')
console.print(''' 
    Author: [bold green]@karadenizemirr[/bold green]
    Version: [bold green]1.0.0[/bold green]
    Description: [bold green]A simple account creator app.[/bold green]
    Github: [bold blue sparkles]https://github.com/karadenizemirr[/bold blue sparkles]\n''')
console.print('Please select an option:\n')

limit = input('How many accounts do you want to create?:  ')
server = input('Which server do you want to use? (ro,de,tr,gr,pl):  ')
email_pass = input('Which email provider do you want to use? (gmail.com,hotmail.com,yandex.com):  ')

# Create Operations
account_list = create_account(int(limit), server, email_pass)

# Write Accounts to File

isSave = input('Do you want to save the accounts to a file? (y/n):  ')

if isSave:
    try:
        filepath = f"{server}_accounts.txt"
        with open(filepath, 'w') as file:
            for account in account_list:
                file.write(account + "\n")
    except:
        console.print('[bold red]An error occurred while saving the accounts to a file.[/bold red]\n')