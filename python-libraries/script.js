
"use strict";

// 1. Example dataset (illustrative ratings)
const examplePlayers = [
    {
        name: "Jamal Musiala",
        club: "Bayern Munich",
        position: "CAM",
        overall: 87
    },
    {
        name: "Jude Bellingham",
        club: "Real Madrid",
        position: "CAM",
        overall: 90
    }
];

// Only confirmed user entries are saved.
const confirmedPlayers = [];
let pendingPlayer = null;

// 2. Get HTML elements
const form = document.getElementById("player-form");
const reviewPanel = document.getElementById("review-panel");
const formMessage = document.getElementById("form-message");
const exampleBody = document.getElementById("example-body");
const confirmedBody = document.getElementById("confirmed-body");

const editButton = document.getElementById("edit-button");
const confirmButton = document.getElementById("confirm-button");
const downloadButton = document.getElementById("download-button");

// 3. Add a player to a table
function addTableRow(player, tableBody) {
    const row = document.createElement("tr");

    const values = [
        player.name,
        player.club,
        player.position,
        player.overall
    ];

    for (const value of values) {
        const cell = document.createElement("td");
        cell.textContent = String(value);
        row.appendChild(cell);
    }

    tableBody.appendChild(row);
}

// Display example data
examplePlayers.forEach(player => {
    addTableRow(player, exampleBody);
});

// 4. Validate and review new player entries
form.addEventListener("submit", function(event) {
    event.preventDefault();

    if (!form.reportValidity()) {
        return;
    }

    const name = document.getElementById("name").value.trim();
    const club = document.getElementById("club").value.trim();
    const position = document.getElementById("position").value;
    const ratingInput = document.getElementById("overall").value;
    const overall = Number(ratingInput);

    if (!name || !club || !position) {
        formMessage.textContent = "Please complete all fields.";
        return;
    }

    if (
        ratingInput.trim() === "" ||
        !Number.isInteger(overall) ||
        overall < 0 ||
        overall > 99
    ) {
        formMessage.textContent =
            "Overall rating must be a whole number from 0 to 99.";
        return;
    }

    formMessage.textContent = "";

    // Prepare a record, but don't save it yet.
    pendingPlayer = {
        name: name,
        club: club,
        position: position,
        overall: overall
    };

    // Display the review information
    document.getElementById("review-name").textContent = name;
    document.getElementById("review-club").textContent = club;
    document.getElementById("review-position").textContent = position;
    document.getElementById("review-overall").textContent = overall;

    form.hidden = true;
    reviewPanel.hidden = false;
});

// 5. Allow users to correct their entry
editButton.addEventListener("click", function() {
    reviewPanel.hidden = true;
    form.hidden = false;
    pendingPlayer = null;
    document.getElementById("name").focus();
});

// 6. Confirm the entry
confirmButton.addEventListener("click", function() {
    if (!pendingPlayer) {
        return;
    }

    confirmedPlayers.push({ ...pendingPlayer });

    // Update the visible dataset
    addTableRow(pendingPlayer, confirmedBody);

    document.getElementById("count").textContent =
        confirmedPlayers.length;

    document.getElementById("empty-state").hidden = true;
    document.getElementById("confirmed-table").hidden = false;

    downloadButton.disabled = false;

    // Reset the form for another entry
    pendingPlayer = null;
    reviewPanel.hidden = true;
    form.hidden = false;
    form.reset();

    formMessage.textContent =
        "Player confirmed! You can add another player.";
    formMessage.style.color = "#23744e";

    document.getElementById("name").focus();
});

// 7. Download confirmed records as JSON
downloadButton.addEventListener("click", function() {
    if (confirmedPlayers.length === 0) {
        return;
    }

    const json = JSON.stringify(confirmedPlayers, null, 4);

    const blob = new Blob([json], {
        type: "application/json"
    });

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = "ea_fc_players.json";

    document.body.appendChild(link);
    link.click();
    link.remove();

    // Release the temporary download URL
    setTimeout(() => URL.revokeObjectURL(url), 1000);
});
