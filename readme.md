# LiNotium

## Projektname und Beschreibung

LiNotium ist ein flexibles und erweiterbares Notiz- und Projektmanagement-Tool, das Funktionen wie Markdown-Notizen, Kanban-Boards und Volltextsuche bietet. Es ist plattformübergreifend und sowohl auf Desktop als auch auf mobilen Geräten verfügbar.

## Features

- **Markdown-Notizen**: Unterstützung für Markdown-Formatierung und -Vorschau
- **Kanban-Board**: Integration eines Kanban-Boards zur Verwaltung von Aufgaben und Projekten
- **Volltextsuche**: Schnelles Durchsuchen von Notizen und Dokumenten
- **PDF-Export**: Exportiere Notizen als PDF-Dokumente
- **Responsive Design**: Verfügbar auf Desktop und mobilen Geräten

## Technologien und Frameworks

- **Frontend**: React, React Native
- **Backend**: Node.js, Express, Flask (Python)
- **Datenbank**: MongoDB, PostgreSQL
- **Volltextsuche**: Elasticsearch
- **Containerisierung**: Docker
- **Deployment**: Docker Compose, Kubernetes

## Installation und Einrichtung

### Voraussetzungen

- Node.js
- npm oder yarn
- Python 3.x
- Docker

### Installation

1. Klone das Repository:
    ```bash
    git clone https://github.com/PLMBakery/LiNotium.git
    cd LiNotium
    ```

2. Installiere die Abhängigkeiten für das Frontend:
    ```bash
    cd frontend
    npm install
    ```

3. Installiere die Abhängigkeiten für das Backend:
    ```bash
    cd ../backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. Starte Docker Compose:
    ```bash
    cd ..
    docker-compose up --build
    ```

## Benutzung

### Starten der Anwendung

- **Frontend**: 
    ```bash
    cd frontend
    npm start
    ```

- **Backend**:
    ```bash
    cd backend
    source venv/bin/activate
    flask run
    ```

### Zugriff auf die Anwendung

- Öffne deinen Browser und gehe zu `http://localhost:3000` für das Frontend.
- Die API ist unter `http://localhost:5000` erreichbar.

## Projektstruktur

LiNotium/
│
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── api.py
│ │ ├── models.py
│ │ └── ...
│ ├── Dockerfile
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ ├── App.js
│ │ ├── index.js
│ │ └── ...
│ └── package.json
│
├── docker-compose.yml
└── README.md


## Roadmap

- [ ] Initiale Projektstruktur erstellen
- [ ] Frontend-Layout und Komponenten entwickeln
- [ ] Backend-API entwickeln
- [ ] Volltextsuche integrieren
- [ ] Kanban-Board-Komponente entwickeln
- [ ] PDF-Export-Funktion hinzufügen
- [ ] Mobile Unterstützung (React Native) hinzufügen
- [ ] Tests und Dokumentation

## Contributing

Beiträge sind willkommen! Bitte erstelle einen Fork des Repositories und erstelle Pull Requests mit ausführlichen Beschreibungen der Änderungen.

## Lizenz

Dieses Projekt ist lizenziert unter der MIT-Lizenz. Siehe die [LICENSE](LICENSE) Datei für Details.
