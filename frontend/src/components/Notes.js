import React, { useState, useEffect } from 'react';

const Notes = () => {
    const [notes, setNotes] = useState([]);
    const [selectedNote, setSelectedNote] = useState(null);

    useEffect(() => {
        const backendUrl = process.env.REACT_APP_BACKEND_URL;
        fetch(`${backendUrl}/api/notes`)
            .then((response) => response.json())
            .then((data) => setNotes(data))
            .catch((error) => console.error('Error fetching notes:', error));
    }, []);

    const handleNoteClick = (note) => {
        setSelectedNote(note);
    };

    return (
        <div className="container">
            <div className="sidebar">
                <h2>Notes</h2>
                <ul>
                    {notes.map(note => (
                        <li key={note.id} onClick={() => handleNoteClick(note)}>
                            {note.title}
                        </li>
                    ))}
                </ul>
            </div>
            <div className="content">
                {selectedNote ? (
                    <div className="note-item">
                        <h3>{selectedNote.title}</h3>
                        <p>{selectedNote.content}</p>
                    </div>
                ) : (
                    <p>Please select a note to view its content.</p>
                )}
            </div>
        </div>
    );
};

export default Notes;
