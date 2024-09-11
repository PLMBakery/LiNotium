const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const port = 5000;

// Enable CORS
app.use(cors());

// Middleware to handle JSON requests
app.use(bodyParser.json());

// In-memory storage for notes (would be replaced by a database in a real app)
let notes = [
    { id: 1, title: "First Note", content: "This is the content of the first note." },
    { id: 2, title: "Second Note", content: "This is the content of the second note." }
];

// Get all notes (READ)
app.get('/api/notes', (req, res) => {
    res.json(notes);
});

// Create a new note (CREATE)
app.post('/api/notes', (req, res) => {
    const { title, content } = req.body;

    // Validate request body
    if (!title || !content) {
        return res.status(400).json({ message: "Title and content are required" });
    }

    const newNote = {
        id: Date.now(), // Simple ID generation based on timestamp
        title,
        content
    };

    // Add the new note to the in-memory notes array
    notes.push(newNote);

    // Send back the newly created note
    res.status(201).json(newNote);
});

// Delete a note (DELETE)
app.delete('/api/notes/:id', (req, res) => {
    const { id } = req.params;
    
    // Filter out the note with the specified ID
    notes = notes.filter(note => note.id != id);

    // Return the remaining notes
    res.json(notes);
});

// Update a note (UPDATE)
app.put('/api/notes/:id', (req, res) => {
    const { id } = req.params;
    const { title, content } = req.body;

    // Find the note by ID and update it
    const noteIndex = notes.findIndex(note => note.id == id);
    if (noteIndex === -1) {
        return res.status(404).json({ message: "Note not found" });
    }

    // Update title and content
    if (title) notes[noteIndex].title = title;
    if (content) notes[noteIndex].content = content;

    // Send back the updated note
    res.json(notes[noteIndex]);
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
