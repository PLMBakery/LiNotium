# LiNotium: Personal Note-Taking App with Docker & PostgreSQL

## Overview
LiNotium is a small, open-source, personal note-taking app designed to run locally via Docker. It features a simple note-taking interface, supports multi-user access, and can be hosted on any platform including Raspberry Pi. The app stores data in PostgreSQL, ensuring persistent storage and easy scalability for features like note attachments and family collaboration.

## Features
- **Note-Taking**: Simple interface for creating, editing, and deleting notes.
- **TeX Formatting**: Write notes in TeX formatting for easy documentation and reuse.
- **Image Attachments**: Include pictures with notes for richer content.
- **Backup**: Easily back up notes to ensure data is secure.
- **Searchable Notes**: Quickly find notes using the search functionality.
- **Multi-User**: Multiple family members can access and use the app simultaneously.
- **Persistent Data**: Data is stored in PostgreSQL with Docker volumes to ensure persistence across restarts.
- **Dockerized**: Runs entirely in Docker for cross-platform compatibility.
- **Open-Source**: Available on GitHub for contributions and forks.

## Use Cases
1. **Personal Note-Taking**: 
   - Store and organize personal notes on a local machine.
   - Access the app through a web browser.
2. **Family Collaboration**: 
   - Share notes, to-do lists, and a family calendar across devices.
   - Multiple users can access the app simultaneously.
3. **Hosting on Raspberry Pi**: 
   - Deploy the app on a Raspberry Pi for 24/7 availability within a home network.

## Project Setup

### Prerequisites
- **Docker** and **Docker Compose**
- **Node.js** and **npm**
- **PostgreSQL** (handled via Docker)

### Backend Setup (Node.js + PostgreSQL)
1. **Navigate to the Backend Directory**:
   ```bash
   cd /path/to/your/project/backend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Ensure PostgreSQL is Running**:
   - Make sure your PostgreSQL Docker container is running, or start it:
     ```bash
     docker-compose up --build
     ```

4. **Start the Backend**:
   ```bash
   npm start
   ```

5. **Verify**:
   - The backend should be running at `http://localhost:5000`.

### Frontend Setup (React)
1. **Navigate to the Frontend Directory**:
   ```bash
   cd /path/to/your/project/frontend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Start the Frontend**:
   ```bash
   npm start
   ```

4. **Access the App**:
   Open your browser and go to `http://localhost:3000`.

### PostgreSQL Setup in Docker
1. **Navigate to the Project Directory**:
   ```bash
   cd /path/to/your/project
   ```

2. **Start PostgreSQL with Docker**:
   ```bash
   docker-compose up --build
   ```

   This will ensure that your PostgreSQL database (`linotium`) is up and running.

## Backup and Versioning
To ensure data and code stability, it is recommended to create a Git branch to save the current working version before adding new features:

1. **Create a New Branch**:
   ```bash
   git checkout -b stable-version
   ```

2. **Commit Changes**:
   ```bash
   git add .
   git commit -m "Save stable version of LiNotium"
   ```

3. **Push the Branch to GitHub**:
   ```bash
   git push origin stable-version
   ```

This ensures you have a stable version saved, allowing you to develop new features in a separate branch.
