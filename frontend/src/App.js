import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [notes, setNotes] = useState([]);
  const [selectedNote, setSelectedNote] = useState(null);

  // Hole die Notizen vom Backend
  useEffect(() => {
    fetch('http://localhost:5000/api/notes')
      .then(response => response.json())
      .then(data => setNotes(data));
  }, []);

  // Wenn auf eine Notiz geklickt wird, setze sie als ausgewählt
  const handleNoteClick = (note) => {
    setSelectedNote(note);
  };

  return (
    <div className="app-container">
      {/* Sidebar für die Notizenliste */}
      <div className="sidebar">
        <h3>Notes</h3>
        <ul>
          {notes.map(note => (
            <li key={note.id} onClick={() => handleNoteClick(note)}>
              {note.title}
            </li>
          ))}
        </ul>
      </div>

      {/* Hauptbereich zur Anzeige der ausgewählten Notiz */}
      <div className="note-display">
        {selectedNote ? (
          <>
            <h2>{selectedNote.title}</h2>
            <p>{selectedNote.content}</p>
          </>
        ) : (
          <p>Select a note to display</p>
        )}
      </div>
    </div>
  );
}

export default App;
