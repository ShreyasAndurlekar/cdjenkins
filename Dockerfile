# Use the official PHP image with Apache
FROM php:8.0-apache

# Copy the HTML and PHP files into the Apache server directory
COPY . /var/www/html/

# Expose port 80 (the default HTTP port)
EXPOSE 80

