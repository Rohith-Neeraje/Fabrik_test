# Use a lightweight web server as a base image
FROM nginx:alpine

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy the editor files into the container
COPY . .

# Expose the port on which the web server will run
EXPOSE 80
