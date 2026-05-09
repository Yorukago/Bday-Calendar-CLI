import calendar
import os
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


def clear_screen():
    os.system("clear")


CAKE = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⢰⢋⢹⡀⢀⡼⠰⡀⠀⡞⡀⣷⠀⠀⡰⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⢀⢱⡄⢸⣿⢿⠀⡋⢀⠀⡇⠀⣿⣿⡇⠀⣞⣀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣯⠀⠘⣿⣻⣀⣙⣼⣴⡁⠀⣿⣿⠀⠀⣼⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣿⠶⢾⣿⣿⢋⣽⣿⣹⣛⠟⣿⣿⠻⠶⣿⣿⣮⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⡻⢧⣿⣿⣾⠺⠛⠿⠛⠁⢸⣿⣿⠁⠸⠿⠟⣴⠀⣿⣷⡿⠉⠹⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠠⢧⣀⣹⠿⣿⠆⠀⠀⠀⠀⢸⣿⣿⡀⠀⠀⠀⠀⠰⣿⡿⢿⠠⢀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠧⠈⡅⠘⠂⢎⢢⠜⣐⠀⡘⠹⠛⠟⢃⡀⡀⠀⠀⠄⠌⡀⠤⠒⠁⢀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣦⣿⣯⣶⣬⠀⠀⠉⢁⠉⢈⠃⠀⠂⠊⠈⠐⠂⠉⢀⣠⣤⣴⣦⣶⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣶⣶⣟⡟⠻⣿⣯⣿⣿⣷⣶⣴⣾⢿⣶⣷⡀⠀⠀⣠⣶⣶⣦⢰⣿⢿⣷⡟⣾⣯⠉⡷⣶⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣿⣿⣷⡿⣿⡂⡀⠈⠉⠳⢯⣿⣽⣫⢿⣯⡞⣽⣿⣇⣊⡿⢶⣛⣿⣾⣻⡮⠗⠋⠉⠉⢠⣿⣟⣾⣻⣿⡄⠀⠀⠀
⠀⠀⢠⣾⣿⢧⡿⣿⣟⡏⣲⡄⠄⠀⣴⣲⠀⠉⠉⠛⠛⠓⠚⠛⡛⠛⠛⠉⠉⠙⠄⠀⠀⠀⠄⡴⢙⢙⣿⣭⢿⣽⣿⡆⠀⠀
⠀⢠⣏⠻⢿⣿⣽⣿⣏⣷⣙⡉⡣⡀⠈⠁⠀⡀⠀⠀⠀⠀⠀⠙⠛⠁⠀⣀⠠⠤⠄⠖⢀⣾⠆⢀⣘⣨⣿⣯⣿⡾⠃⢹⡄⠀
⠀⢸⣟⠄⠀⣠⣿⣷⣹⣿⡻⢷⣤⣁⠭⠒⠉⠁⢿⡿⠂⢄⡀⠀⢀⡰⠆⢣⣿⡧⠀⠀⠂⣁⣴⢿⣿⣭⢿⣽⡄⠀⠀⣼⡇⠀
⠀⢀⣿⣦⠀⡛⢿⡷⠿⣝⡃⣠⣿⣻⣿⣷⣦⣄⡀⣄⠀⣀⡉⢒⡁⠀⠀⢈⠉⣤⣶⣞⣻⣯⡀⠙⡿⢾⠯⡿⠙⠀⣡⣿⠀⠀
⠀⠈⣿⣾⣷⣦⡄⢈⠁⠘⠃⣿⣿⣯⢷⣿⠧⠉⠉⠓⢲⣶⡟⣿⣶⡓⠒⠚⠉⣿⣿⣽⣳⣿⡇⠻⠃⠀⠀⠀⠔⣱⡟⣽⠆⠀
⠀⣠⣾⣽⡿⣿⣿⣆⠀⢂⠀⠉⠙⠿⠟⠃⠀⢌⣤⣄⢻⣿⣻⢿⣽⡇⢾⡿⠂⠈⠙⠓⠛⠋⠀⠀⠀⠀⠀⣴⣿⣿⠾⣿⡄⠀
⢠⠇⣿⣞⣿⣝⣻⣿⣷⡤⣅⢤⣀⡤⣀⠄⣄⠈⠈⠁⠀⠉⠛⠛⠋⠀⠀⠀⢈⡠⢀⣀⣀⡠⢀⠀⠀⣠⣾⠿⠛⢾⣫⣿⠹⠀
⠐⡎⣿⣿⣾⣳⣯⣞⠿⣿⡻⢿⣿⣟⡿⣿⣶⣌⡐⠢⢄⠀⠀⠀⠀⢀⡤⣶⡿⢟⡻⢛⡟⣿⣷⣾⣵⢾⡻⠿⣐⣟⣿⡟⢰⠁
⠀⢻⡌⢻⣿⣷⣟⡾⣿⣢⣿⣷⣬⠙⡙⠳⠟⡿⢿⣿⣿⣾⣖⢢⢴⣺⣿⠿⠾⠶⠛⠯⣛⡉⠈⠻⠍⢞⣣⢞⣵⣿⡿⢡⡟⠀
⠀⠀⠹⣕⣎⠻⣿⣿⣷⣳⣎⡟⣥⢛⣼⡷⠌⣴⣦⠀⠘⠿⣿⣿⣿⠋⠤⡀⢤⠀⢴⠊⣛⢁⡤⣖⢾⣭⣾⣿⡿⢋⣔⠏⠀⠀
⠀⠀⠀⠀⠙⠶⣄⡙⠻⢿⣿⣾⣽⣳⣞⡽⣶⣡⣍⡊⡔⣄⢮⡙⡥⡠⢔⡰⣂⢬⡤⣞⣮⣭⣷⣾⡿⠿⢋⢁⡰⠝⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⠱⢦⣈⣙⠛⠿⠿⣿⣷⣷⣾⣽⣧⣿⣶⣽⣷⣽⣽⣶⣿⣾⣿⠿⠿⠟⠋⡁⣔⠬⠖⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⠙⠳⠶⣠⣀⣉⠉⠉⠛⠛⠛⠛⠛⠛⠉⠉⢉⣀⣠⡤⠶⠙⠓⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠋⠓⠉⠈⠁⠋⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


def print_logo():
    console.print(Panel(CAKE, style="bold magenta", title="✨ Yoru's Birthday Tracker ✨", expand=False))


def print_list(data: dict):
    if not data:
        console.print("[yellow]No birthdays saved yet![/yellow]")
        return

    table = Table(title="All Birthdays", style="magenta")
    table.add_column("Name", style="bold cyan")
    table.add_column("Birthday", justify="center")
    table.add_column("Wishlist", style="italic yellow")
    table.add_column("Likes", style="italic green")

    today = datetime.now().date()

    for person in data.values():
        try:
            bday = datetime.strptime(person["birthday"], "%d-%m-%Y").date()
            this_year = bday.replace(year=today.year)
            if this_year < today:
                this_year = bday.replace(year=today.year + 1)
            days_left = (this_year - today).days
            date_str = f"{person['birthday']} [dim]({days_left}d)[/dim]"
        except ValueError:
            date_str = person["birthday"]

        table.add_row(person["name"], date_str, person["wishlist"], person["likes"])

    console.print(table)


def show_calendar(birthday_data: dict):
    now = datetime.now()
    year, month = now.year, now.month

    table = Table(
        title=f"{calendar.month_name[month].upper()} {year}",
        show_header=True,
        header_style="bold magenta",
        collapse_padding=True,
        expand=True,
        border_style="bright_blue",
    )

    for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        table.add_column(day, justify="center")

    for week in calendar.monthcalendar(year, month):
        row = []
        for day in week:
            if day == 0:
                row.append("")
                continue

            names_today = []
            for person in birthday_data.values():
                try:
                    d, m, _ = map(int, person["birthday"].split("-"))
                    if d == day and m == month:
                        names_today.append(f"[bold yellow]{person['name']}[/bold yellow]")
                except (ValueError, IndexError):
                    continue

            bday_display = "\n" + "\n".join(names_today) if names_today else ""
            if day == now.day:
                row.append(f"\n[bold green]> {day} <[/bold green]{bday_display}\n")
            else:
                row.append(f"\n{day}{bday_display}\n")

        table.add_row(*row)
        table.add_section()

    clear_screen()
    console.print(table)


def print_shell_reminder_banner():
    console.print("[dim]── Birthdays ──[/dim]")


def print_upcoming(upcoming: list[dict]):
    for person in upcoming:
        days = person["days_left"]
        name = person["name"]
        wish = person["wishlist"]
        date = person["date_this_year"].strftime("%d %b")

        if days == 0:
            console.print(f"[bold magenta]🎂 TODAY is {name}'s birthday! Wishlist: {wish}[/bold magenta]")
        elif days == 1:
            console.print(f"[bold yellow]🎁 Tomorrow is {name}'s birthday! ({date}) Wishlist: {wish}[/bold yellow]")
        else:
            console.print(f"[cyan]🕯  {name}'s birthday in {days} days ({date})[/cyan]")


def print_person(person: dict):
    table = Table(style="magenta", show_header=False)
    table.add_column("Field", style="bold cyan")
    table.add_column("Value")
    table.add_row("Name", person["name"])
    table.add_row("Birthday", person["birthday"])
    table.add_row("Wishlist", person["wishlist"])
    table.add_row("Likes", person["likes"])
    console.print(table)


def err(msg: str):
    console.print(f"[bold red]error:[/bold red] {msg}")


def ok(msg: str):
    console.print(f"[bold green]✓[/bold green] {msg}")
