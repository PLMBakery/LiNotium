const express = require('express');
const cors = require('cors');
const app = express();
const port = 5000;

// CORS aktivieren
app.use(cors());

// JSON-Payloads im Anfragetext verarbeiten
app.use(express.json());

// API-Route zum Abrufen der Notizen
app.get('/api/notes', (req, res) => {
    res.json([
        {
            id: 1,
            title: 'First Note',
            content: 'This is the content of the first note.'
        },
        {
            id: 2,
            title: 'Second Note',
            content: 'This is the content of the second note.'
        }
    ]);
});

// Server starten
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
