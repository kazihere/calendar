import calendar
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

themes = {
    "light": {"header": "black on white", "days": "blue", "weekend": "red"},
    "dark": {"header": "white on black", "days": "green", "weekend": "bright_red"},
    "colorful": {"header": "bold magenta", "days": "cyan", "weekend": "bold yellow"},
}

current_theme = "dark"

def render_month(year, month, theme_name):
    theme = themes[theme_name]
    cal = calendar.Calendar()
    month_name = calendar.month_name[month]

    table = Table(title=f"{month_name} {year}", box=box.ROUNDED, title_style=theme['header'])
    
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        style = theme['weekend'] if day in ["Sat", "Sun"] else theme['days']
        table.add_column(day, justify="center", style=style)
    
    month_days = cal.monthdayscalendar(year, month)
    for week in month_days:
        row = []
        for i, day in enumerate(week):
            if day == 0:
                row.append("")
            else:
                day_style = theme['weekend'] if i >= 5 else theme['days']
                row.append(f"[{day_style}]{day}[/{day_style}]")
        table.add_row(*row)
    
    console.print(table)

def main():
    global current_theme
    while True:
        console.print("\n[bold cyan]-- Themed Calendar Menu --[/bold cyan]")
        console.print("1. Show Month")
        console.print("2. Change Theme")
        console.print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            try:
                year = int(input("Enter year: "))
                month = int(input("Enter month (1-12): "))
                render_month(year, month, current_theme)
            except ValueError:
                console.print("[red]Invalid input![/red]")
        elif choice == '2':
            console.print("Available themes: light, dark, colorful")
            new_theme = input("Enter theme name: ").strip().lower()
            if new_theme in themes:
                current_theme = new_theme
                console.print(f"Theme changed to [bold]{new_theme}[/bold].")
            else:
                console.print("[red]Invalid theme name.[/red]")
        elif choice == '3':
            console.print("[bold green]Goodbye![/bold green]")
            break
        else:
            console.print("[red]Invalid choice![/red]")

if __name__ == "__main__":
    main()
