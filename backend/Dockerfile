# Use an official Node.js image as the base image
FROM node:18

# Install postgresql-client to use pg_isready
RUN apt-get update && apt-get install -y postgresql-client

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install the backend dependencies
RUN npm install

# Copy the rest of the backend source code
COPY . .

# Expose the backend port
EXPOSE 5000

# Start the backend server
CMD ["node", "index.js"]
