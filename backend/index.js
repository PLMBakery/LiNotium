const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { Pool } = require('pg');

const app = express();
const port = 5000;

// Enable CORS
app.use(cors());

// Middleware to handle JSON requests
app.use(bodyParser.json());

// PostgreSQL connection pool
const pool = new Pool({
    user: process.env.POSTGRES_USER || 'marc',
    host: process.env.POSTGRES_HOST || 'localhost', // change to 'db' if running in Docker Compose
    database: process.env.POSTGRES_DB || 'linotion',
    password: process.env.POSTGRES_PASSWORD || 'password',
    port: 5432,
});

// Initialize the table if it doesn't exist
const createTableQuery = `
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);
`;
pool.query(createTableQuery).catch((err) => console.error('Error creating table', err));

// Get all notes (READ)
app.get('/api/notes', async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM notes');
        res.json(result.rows);
    } catch (error) {
        console.error('Error fetching notes', error);
        res.status(500).json({ message: 'Error fetching notes' });
    }
});

// Create a new note (CREATE)
app.post('/api/notes', async (req, res) => {
    const { title, content } = req.body;

    // Validate request body
    if (!title || !content) {
        return res.status(400).json({ message: "Title and content are required" });
    }

    try {
        const result = await pool.query(
            'INSERT INTO notes (title, content) VALUES ($1, $2) RETURNING *',
            [title, content]
        );
        res.status(201).json(result.rows[0]);
    } catch (error) {
        console.error('Error creating note', error);
        res.status(500).json({ message: 'Error creating note' });
    }
});

// Delete a note (DELETE)
app.delete('/api/notes/:id', async (req, res) => {
    const { id } = req.params;

    try {
        await pool.query('DELETE FROM notes WHERE id = $1', [id]);
        res.status(204).send();
    } catch (error) {
        console.error('Error deleting note', error);
        res.status(500).json({ message: 'Error deleting note' });
    }
});

// Update a note (UPDATE)
app.put('/api/notes/:id', async (req, res) => {
    const { id } = req.params;
    const { title, content } = req.body;

    try {
        const result = await pool.query(
            'UPDATE notes SET title = $1, content = $2 WHERE id = $3 RETURNING *',
            [title, content, id]
        );
        if (result.rows.length === 0) {
            return res.status(404).json({ message: "Note not found" });
        }
        res.json(result.rows[0]);
    } catch (error) {
        console.error('Error updating note', error);
        res.status(500).json({ message: 'Error updating note' });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
