# Use an official Node.js runtime as a parent image
FROM node:18-alpine AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Angular application
ARG BACKEND_URL=http://localhost:52582
RUN echo "{\"BACKEND_URL\": \"$BACKEND_URL\"}" > public/env.json
RUN npm run build -- --output-path=dist --configuration production --base-href=/

# Use an Nginx image to serve the Angular app
FROM nginx:stable-alpine

# Copy the built Angular app to the Nginx HTML directory
COPY --from=build /app/dist/browser/ /usr/share/nginx/html/

# Ensure a default favicon is present to avoid 404 errors
RUN echo "" > /usr/share/nginx/html/favicon.ico

# Copy the custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
