
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

# ==========================================
# 1. Initialize Rich Console
# ==========================================

console = Console()

# Sample EA FC player ratings (illustrative data)
players = [
    {
        "name": "Jamal Musiala",
        "club": "Bayern Munich",
        "position": "CAM",
        "overall": 87
    },
    {
        "name": "Jude Bellingham",
        "club": "Real Madrid",
        "position": "CAM",
        "overall": 90
    }
]

# Store newly confirmed player entries separately
new_entries = []


# ==========================================
# 2. Reusable Table Function
# ==========================================

def show_players_table(player_list, title):
    """Display player data in a formatted Rich table."""

    table = Table(title=title)

    table.add_column("Player Name", style="cyan")
    table.add_column("Club", style="magenta")
    table.add_column("Position", style="green")
    table.add_column("Overall", justify="right")

    for player in player_list:
        table.add_row(
            player["name"],
            player["club"],
            player["position"],
            str(player["overall"])
        )

    console.print(table)


# ==========================================
# 3. Display Existing Player Data
# ==========================================

console.print(
    "\n[bold cyan]EA FC Player Ratings Database[/bold cyan]"
)

show_players_table(players, "Existing Player Data")


# ==========================================
# 4. Instructions for New Users
# ==========================================

console.print(
    "\n[bold cyan]Welcome to EA FC Data Entry![/bold cyan]"
)

console.print(
    "EA FC is a soccer video game that assigns numerical "
    "ratings to soccer players based on their in-game abilities."
)

console.print(
    "\n[dim]You can add soccer players to this dataset. "
    "Type ? at any input field to see an explanation "
    "and examples.[/dim]\n"
)


# ==========================================
# 5. Helper Function for User Input
# ==========================================

def ask_field(label, example, help_text):
    """Ask for a required field and provide optional help."""

    while True:
        answer = console.input(
            f"[bold]{label}[/bold] "
            f"[dim](e.g., {example}; ? for help)[/dim]: "
        ).strip()

        if answer.lower() in ("?", "help"):
            console.print(f"[cyan]{help_text}[/cyan]")
            continue

        if not answer:
            console.print(
                "[red]This field cannot be empty.[/red]"
            )
            continue

        return answer


# ==========================================
# 6. Validate Overall Rating
# ==========================================

def ask_rating():
    """Collect a whole-number rating between 0 and 99."""

    while True:
        answer = ask_field(
            "Overall Rating (0-99)",
            "85",
            "Overall rating measures a player's in-game "
            "ability on a scale from 0 to 99. "
            "A higher number means a stronger rating. "
            "You may use an illustrative value for practice."
        )

        if answer.isdigit() and 0 <= int(answer) <= 99:
            return int(answer)

        console.print(
            "[red]Please enter a whole number "
            "between 0 and 99.[/red]"
        )


# ==========================================
# 7. Collect and Confirm New Player Data
# ==========================================

console.print(
    "\n[bold cyan]Add New EA FC Players[/bold cyan]\n"
)

while True:

    # Repeat data entry until the user confirms
    while True:

        name = ask_field(
            "Player Name",
            "Jamal Musiala",
            "Enter the full name of a soccer player. "
            "For example: Jamal Musiala or Lionel Messi."
        )

        club = ask_field(
            "Club",
            "Bayern Munich",
            "A club is the soccer team a player represents. "
            "Examples include Bayern Munich, Barcelona, "
            "Real Madrid, and Manchester City."
        )

        position = ask_field(
            "Position",
            "CAM",
            "Common soccer positions:\n"
            "GK = Goalkeeper\n"
            "CB = Center Back (Defender)\n"
            "LB/RB = Left/Right Back\n"
            "CDM = Defensive Midfielder\n"
            "CM = Central Midfielder\n"
            "CAM = Attacking Midfielder\n"
            "LM/RM = Left/Right Midfielder\n"
            "LW/RW = Left/Right Winger\n"
            "ST = Striker"
        ).upper()

        overall = ask_rating()

        # Create a new player record
        new_player = {
            "name": name,
            "club": club,
            "position": position,
            "overall": overall
        }

        # Display the entry for review
        console.print(
            "\n[bold yellow]Review Your Entry[/bold yellow]"
        )

        show_players_table(
            [new_player],
            "Pending Player Entry"
        )

        # Ask the user to confirm the entry
        while True:
            confirm = console.input(
                "\nIs this information correct? (y/n): "
            ).strip().lower()

            if confirm in ("y", "yes", "n", "no"):
                break

            console.print(
                "[red]Please enter y or n.[/red]"
            )

        if confirm in ("y", "yes"):

            # Add the confirmed player to both lists
            players.append(new_player)
            new_entries.append(new_player)

            console.print(
                "\n[bold green]"
                "Player confirmed successfully!"
                "[/bold green]"
            )

            # ==================================
            # Table 1: Newly Added Players
            # ==================================

            console.print(
                f"\n[bold cyan]"
                f"Newly Added Players ({len(new_entries)})"
                f"[/bold cyan]"
            )

            show_players_table(
                new_entries,
                "Session Additions"
            )

            # ==================================
            # Table 2: Full Updated Dataset
            # ==================================

            console.print(
                f"\n[bold cyan]"
                f"Full Updated Dataset ({len(players)})"
                f"[/bold cyan]"
            )

            show_players_table(
                players,
                "All Player Records"
            )

            break

        else:
            console.print(
                "\n[yellow]"
                "Let's re-enter the player information."
                "[/yellow]\n"
            )

    # Ask whether to add another player
    while True:
        another = console.input(
            "\nWould you like to add another player? (y/n): "
        ).strip().lower()

        if another in ("y", "yes", "n", "no"):
            break

        console.print(
            "[red]Please enter y or n.[/red]"
        )

    if another in ("n", "no"):
        break


# ==========================================
# 8. Final Session Summary
# ==========================================

console.print(
    "\n[bold cyan]Session Summary[/bold cyan]"
)

console.print(
    f"New players added: [green]{len(new_entries)}[/green]"
)

console.print(
    f"Total players displayed: [green]{len(players)}[/green]"
)


# ==========================================
# 9. Save Confirmed Data to JSON
# ==========================================

if new_entries:

    # Save the file in the same folder as this script
    output_path = (
        Path(__file__).resolve().parent / "sample_data.json"
    )

    # Save only newly confirmed entries
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            new_entries,
            file,
            indent=4,
            ensure_ascii=False
        )

    console.print(
        "\n[bold green]Data saved successfully![/bold green]"
    )

    console.print(
        f"New players saved: {len(new_entries)}"
    )

    console.print(
        f"File location: [cyan]{output_path}[/cyan]"
    )

else:
    console.print(
        "\n[yellow]No new players to save.[/yellow]"
    )


# ==========================================
# 10. Exit Message
# ==========================================

console.print(
    "\n[bold cyan]"
    "Thank you for contributing to the "
    "EA FC Player Ratings dataset!"
    "[/bold cyan]"
)
