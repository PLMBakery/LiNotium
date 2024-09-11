Project: LiNotium - Note Taking App
Current Status (091124)
We have successfully set up the main layout for the Note Taking App.
The app now displays a Sidebar with a list of notes on the left and a Note Display section on the right where the content of the selected note is shown.
CSS styles have been updated to reflect the desired structure similar to Notion with a sidebar and a content area.
The app structure now includes both a frontend and backend, with functionality for fetching notes.
Changes Implemented
App.js:

We structured the app to display a sidebar and a note display section.
Used a useState hook to manage the selected note and displayed it when clicked.
App.css:

Replaced the default React CSS with custom styles for the sidebar and the note display.
The sidebar has a dark background and shows a hover effect for each note.

CSS Structure

.app-container {
  display: flex;
  height: 100vh;
}

.sidebar {
  width: 250px;
  background-color: #2c3e50;
  color: white;
  padding: 20px;
}

.sidebar h3 {
  font-size: 24px;
  margin-bottom: 20px;
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar li {
  margin: 10px 0;
  cursor: pointer;
}

.sidebar li:hover {
  background-color: #34495e;
  padding: 10px;
}

.note-display {
  flex-grow: 1;
  padding: 20px;
}

.note-display h2 {
  font-size: 28px;
  margin-bottom: 10px;
}


Next Steps
Fetch notes dynamically from the backend and display them in the sidebar.
Implement the ability to create new notes and update the note display.
Ensure data persistence and synchronization with the backend.
Begin implementing functionality for editing and deleting notes.
Known Issues
None currently.

How to Run the App
Ensure you have the latest version of Node.js and npm installed.
Run the backend by navigating to the backend folder and running npm start.
Start the frontend by navigating to the frontend folder and running npm start.
Open localhost:3000 to view the current app.