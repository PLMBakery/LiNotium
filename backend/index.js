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
    user: 'marc',
    host: 'db', // Using Docker service name "db"
    database: 'linotium',
    password: 'marc',
    port: 5432,
});

// Check if the pool is running
pool.connect((err) => {
    if (err) {
        console.error('Error connecting to the database', err);
    } else {
        console.log('Connected to the database');
        
        // Initialize the table if it doesn't exist
        const createTableQuery = `
        CREATE TABLE IF NOT EXISTS notes (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL
        );
        `;
        pool.query(createTableQuery).catch((err) => console.error('Error creating table', err));

        // Start the server after the database is connected and the table is initialized
        app.listen(port, () => {
            console.log(`Server running on http://backend:${port}`);
            console.log('App is ready. You can access the frontend at http://localhost:3000/');
        });
    }
});

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
