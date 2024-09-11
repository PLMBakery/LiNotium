import React from 'react';
import './App.css';
import Notes from './components/Notes';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>My Notes App</h1>
            </header>
            <Notes />
        </div>
    );
}

export default App;
