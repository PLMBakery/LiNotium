const express = require('express');
const cors = require('cors'); // CORS hinzufügen

const app = express();
const port = 5000;

app.use(cors()); // CORS aktivieren
app.use(express.json());

let notes = [
    { id: 1, title: "First Note", content: "This is the content of the first note." },
    { id: 2, title: "Second Note", content: "This is the content of the second note." }
];

app.get('/api/notes', (req, res) => {
    res.json(notes);
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
