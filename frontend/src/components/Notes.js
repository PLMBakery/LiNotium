import React, { useEffect, useState } from 'react';

function Notes() {
    const [notes, setNotes] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/notes')
            .then(response => response.json())
            .then(data => setNotes(data))
            .catch(error => console.error('Error fetching notes:', error));
    }, []);

    return (
        <div>
            <h1>Notes</h1>
            <ul>
                {notes.map(note => (
                    <li key={note.id}>
                        <h2>{note.title}</h2>
                        <p>{note.content}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Notes;
