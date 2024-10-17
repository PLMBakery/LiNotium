# Use an official Node.js image as the base image
FROM node:18

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install the backend dependencies
RUN npm install

# Copy the wait-for-it script
COPY wait-for-it.sh /usr/src/app/

# Copy the rest of the backend source code
COPY . .

# Expose the backend port
EXPOSE 5000

# Start the backend server
CMD ["node", "index.js"]

# Start the backend server and wait for the database to be ready
CMD ["./wait-for-it.sh", "db:5432", "--", "node", "index.js"]
