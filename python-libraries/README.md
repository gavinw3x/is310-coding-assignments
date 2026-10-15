
# EA FC Player Data Curation

## Project Overview

This project is part of IS 310: Culture As Data at the
University of Illinois Urbana-Champaign.

The project explores how EA SPORTS FC represents soccer
players through numerical ratings and categories.

Users can contribute player data including:
- Player name
- Club
- Position
- Overall rating (0–99)

The application includes two interfaces:
1. A Python command-line interface (CLI)
2. An HTML, CSS, and JavaScript web interface

Both interfaces display example data, collect multiple
entries, validate user input, require confirmation,
and export confirmed records as JSON.

The included example ratings are illustrative rather
than verified against a specific EA FC edition.

## Installation and Requirements

The Python application requires Python 3 and the Rich
library.

From the repository root, create a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install the required packages:

    python -m pip install -r python-libraries/requirements.txt

## Running the Python CLI

From the repository root, run:

    python python-libraries/cli_data_entry.py

The program displays example player records and asks
the user to enter additional players.

Users can type "?" at an input field to get help.
Each entry is reviewed before confirmation.

Confirmed entries are saved to:

    python-libraries/sample_data.json

The file contains newly confirmed entries from the
current run. Running the CLI again and saving entries
replaces the previous file.

## Running the HTML Interface

Open python-libraries/index.html in a web browser.

On macOS, from the repository root:

    open python-libraries/index.html

No additional dependencies or web server are required.

Users can:
- View example records
- Enter player information
- Read field descriptions and position explanations
- Review and edit an entry before confirmation
- Add multiple confirmed players
- Download their dataset as JSON

The HTML version exports only confirmed entries from
the current browser session.

## Comparing the Two Interfaces

### What does each interface make easier or harder?

The CLI provides a straightforward, sequential
data-entry process. It guides users through one field
at a time and is convenient for people familiar with
terminal applications.

However, the CLI can be less intuitive for beginners
because it requires running commands and entering
information through text prompts.

The HTML interface is more accessible to users who
are unfamiliar with programming or command-line tools.
Its labeled fields, dropdown menu, and visible dataset
make the process easier to understand.

The HTML interface requires additional HTML, CSS,
and JavaScript code, making its implementation more
complex than the CLI.

### Different design decisions

The CLI uses text prompts and a help command ("?")
to explain unfamiliar soccer terminology.

The HTML interface uses field descriptions and a
position dropdown instead. This reduces the need
to remember position abbreviations.

Both interfaces validate required fields and overall
ratings, but the HTML form makes the available
choices more visible before submission.

### AI contributions and modifications

ChatGPT assisted with generating, explaining, and
revising the Python CLI and HTML interface code.

AI helped implement:
- Rich tables for displaying player data
- Interactive user input and validation
- Entry confirmation and correction
- JSON export
- HTML form functionality and styling

I requested additional help text and examples because
the original CLI assumed users were already familiar
with soccer terminology and EA FC ratings.

The interface was revised to include explanatory
prompts, examples, and a help command.

The AI-generated code was tested locally, and the
working HTML interface was checked in a browser.

### Which interface is better for the intended user?

I think the HTML interface is better suited for
people who may not be familiar with EA FC or soccer.

Its visual structure, field descriptions, and dropdown
menu help users understand what data they are entering.

The CLI is useful for demonstrating Python scripting
and structured data collection, but the HTML interface
offers a more approachable experience for a general
audience.

## Data Curation Considerations

EA FC ratings simplify complex player abilities into
numerical values and predefined positions.

These categories are useful for organizing and
comparing players, but they cannot fully represent
real-world soccer performance.

The project demonstrates how interface design and
data structures influence the kinds of information
users can contribute.
