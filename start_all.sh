#!/bin/bash
# Start PostgreSQL container
cd /path/to/your/project/db
docker-compose up -d

# Start Backend
cd /path/to/your/project/backend
npm start &

# Start Frontend
cd /path/to/your/project/frontend
npm start &
