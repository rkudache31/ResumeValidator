# Use the official MySQL image as the base image
FROM mysql:latest

# Set environment variables
ENV MYSQL_ROOT_PASSWORD Test123
ENV MYSQL_DATABASE resumedetails
ENV MYSQL_USER hr
ENV MYSQL_PASSWORD hr123

# Copy SQL script to initialize the database schema
COPY init.sql /docker-entrypoint-initdb.d/
COPY my.cnf /etc/my.cnf
EXPOSE 3306
