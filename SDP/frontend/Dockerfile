# Use Node.js to build the Angular app
FROM node:18 AS build

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the Angular app source code
COPY . .

# Build the Angular app for production
RUN npm run build --prod

# Use Nginx to serve the app
FROM nginx:alpine
COPY --from=build /app/dist/frontend /usr/share/nginx/html

# Expose port 80 for web traffic
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]