/*******************************************************************************
   Rescue Me Database - Custom Schema
   Script: RescueMe_PostgreSql.sql
   Description: Creates and populates the Rescue Me database.
   DB Server: PostgreSql
   Author: [Your Name]
********************************************************************************/


/*******************************************************************************
   Create Tables
********************************************************************************/

-- Create animals table
CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(100),
    breed VARCHAR(100),
    age INTEGER,
    status VARCHAR(50)
);

-- Create rescue_centers table
CREATE TABLE rescue_centers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(255),
    contact_info VARCHAR(255)
);

-- Create contacts table
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(50),
    email VARCHAR(100),
    rescue_center_id INTEGER REFERENCES rescue_centers(id)
);


/*******************************************************************************
   Populate Tables
********************************************************************************/

-- Insert sample data into animals table
INSERT INTO animals (name, species, breed, age, status) VALUES
('Bella', 'Dog', 'Labrador Retriever', 3, 'Adoptable'),
('Milo', 'Cat', 'Siamese', 2, 'Adopted');

-- Insert sample data into rescue_centers table
INSERT INTO rescue_centers (name, location, contact_info) VALUES
('Happy Paws Rescue', '1234 Elm St, Bristol', 'contact@happypaws.org'),
('Forever Homes', '5678 Oak St, Bristol', 'info@foreverhomes.org');

-- Insert sample data into contacts table
INSERT INTO contacts (name, phone_number, email, rescue_center_id) VALUES
('Alice Johnson', '555-1234', 'alice@happypaws.org', 1),
('Bob Smith', '555-5678', 'bob@foreverhomes.org', 2);
