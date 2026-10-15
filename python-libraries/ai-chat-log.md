# AI Chat Log — IS 310 Command Line Data Curation

## AI Tool Used
- **Tool:** ChatGPT 
- **Assignment:** Command Line Data Curation (Pathway 2)

## 1. Assignment Discussion and Topic Selection

I used ChatGPT to review the assignment requirements and discuss possible approaches to building a command-line data curation application.

We decided to create an **EA FC Player Data Entry application**, connecting the assignment to my group's broader research topic about how EA SPORTS FC quantifies soccer players through numerical ratings and categories.

The application collects player names, clubs, positions, and overall ratings.

## 2. Python CLI Development

I asked ChatGPT to help set up the Python virtual environment, install the Rich library, and generate the Python CLI application.

ChatGPT generated code for displaying existing player records, collecting multiple entries, validating inputs, confirming information, and exporting the data as JSON.

## 3. UX Improvements and Troubleshooting

During development, I noticed that the initial interface assumed users were familiar with soccer terminology and EA FC ratings.

I discussed this usability issue with ChatGPT and requested improvements, including:

- A short introduction explaining EA FC ratings.
- Example inputs for each field.
- A help command (`?`) explaining unfamiliar terminology.
- A review and confirmation process that allows users to correct mistakes before saving.

We revised the data-entry flow to make the application more approachable for users without prior knowledge of soccer.

## 4. HTML Interface Development

For Pathway 2, I asked ChatGPT to generate an HTML interface with equivalent functionality.

ChatGPT generated the HTML, CSS, and JavaScript code for the web application, including form fields, validation, contextual help, a review screen, and JSON export.

The HTML version uses a dropdown menu for player positions instead of requiring users to type abbreviations manually.

## 5. Testing and Documentation

I tested the Python CLI and HTML interface locally to check their basic functionality.

ChatGPT also assisted in drafting the README, including installation instructions and a comparison of the two interfaces.
