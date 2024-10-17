import React, { useState, useEffect } from "react";
import './App.css';

function App() {
  const [notes, setNotes] = useState([]);
  const [selectedNote, setSelectedNote] = useState(null);
  const [newNote, setNewNote] = useState({ title: '', content: '' });
  const [showNewNoteModal, setShowNewNoteModal] = useState(false);

  const backendUrl = process.env.REACT_APP_BACKEND_URL;

  useEffect(() => {
    if (!backendUrl) {
      console.error('Backend URL is not defined. Please set REACT_APP_BACKEND_URL in the environment variables.');
      return;
    }
    fetch(`${backendUrl}/api/notes`)
      .then(response => response.json())
      .then(data => setNotes(data))
      .catch(error => console.error('Error fetching notes:', error));
  }, [backendUrl]);

  const handleNoteSelect = (note) => {
    setSelectedNote(note);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewNote({ ...newNote, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!backendUrl) {
      console.error('Backend URL is not defined. Please set REACT_APP_BACKEND_URL in the environment variables.');
      return;
    }

    fetch(`${backendUrl}/api/notes`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newNote),
    })
      .then(response => response.json())
      .then(data => {
        setNotes([...notes, data]);
        setNewNote({ title: '', content: '' });
        setShowNewNoteModal(false);
      })
      .catch(error => console.error('Error adding note:', error));
  };

  const handleNewNoteClick = () => {
    setShowNewNoteModal(true);
  };

  const handleModalClose = () => {
    setShowNewNoteModal(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>My Notes App</h1>
      </header>

      <div className="App-content">
        <div className="Sidebar">
          <button className="add-note-button" onClick={handleNewNoteClick}>
            + Add New Note
          </button>
          <h2>Notes</h2>
          <ul>
            {notes.map(note => (
              <li key={note.id} onClick={() => handleNoteSelect(note)}>
                <strong>{note.title}</strong>
                <p>{note.content}</p>
              </li>
            ))}
          </ul>
        </div>

        <div className="Note-details">
          {selectedNote ? (
            <>
              <h2>{selectedNote.title}</h2>
              <p>{selectedNote.content}</p>
            </>
          ) : (
            <p>Please select a note to view details</p>
          )}
        </div>

        {showNewNoteModal && (
          <div className="modal">
            <div className="modal-content">
              <h2>Create a New Note</h2>
              <form onSubmit={handleSubmit}>
                <div>
                  <label>Title:</label>
                  <input
                    type="text"
                    name="title"
                    value={newNote.title}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div>
                  <label>Content:</label>
                  <textarea
                    name="content"
                    value={newNote.content}
                    onChange={handleInputChange}
                    required
                  ></textarea>
                </div>
                <button type="submit">Add Note</button>
              </form>
              <button onClick={handleModalClose}>Close</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
