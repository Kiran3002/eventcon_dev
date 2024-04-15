FROM nginx:latest

# Copy the website files into the container
COPY . /usr/share/nginx/html

# Expose port 80 to allow outside access
EXPOSE 88