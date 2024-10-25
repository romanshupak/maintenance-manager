# Maintenance Manager


## Overview
Maintenance Manager is a comprehensive tool designed to streamline and manage onboard vessel maintenance efficiently. It offers a robust solution for handling various aspects of vessel maintenance, ensuring safety, compliance, and operational efficiency.

# Features
### Vessel Departments and Positions

* Organize and manage different departments and roles within the vessel.
* Access detailed information about each department and the corresponding positions.
  
### Worker Information

* Maintain detailed profiles for all workers involved in maintenance tasks.
* Include personal information and work history to keep track of responsibilities and performance.

### Maintenance Management

* Create, update, and delete maintenance tasks (available for logged-in users).
* Track completed and pending maintenance tasks to ensure timely execution and compliance.
* Include detailed descriptions, deadlines, and status updates for each task.
* Search Option: Easily find maintenance tasks by name using the search functionality.

### Regulatory Information

* Access static, read-only information about crucial maritime conventions:
  * SOLAS (Safety of Life at Sea)
  * MARPOL (Marine Pollution)
  * MLC (Maritime Labour Convention)
  * COLREG (International Regulations for Preventing Collisions at Sea)
* Stay informed about important regulations and standards that impact vessel operations and maintenance.

### Powerful admin panel for advanced managing

## Usage
### User Authentication

* Secure login system to ensure only authorized personnel can create, update, or delete maintenance tasks.

### User-Friendly Interface

* Intuitive design for easy navigation and management of maintenance tasks.
* Clear categorization and search functionality for quick access to information.

## Installation
Python3 must be already installed
* git clone https://github.com/romanshupak/maintenance-manager.git
* cd maintenance_manager
* python -m venv venv
* venv\Scripts\activate (on Windows)
* source venv/bin/activate (on macOS)
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py runserver

## Getting Started
To get started with Maintenance Manager, follow these steps:

1. Clone the repository from GitHub.
2. Install the necessary dependencies.
3. Set up the database with the required schemas.
4. Run the application and log in to access the full range of features.

## Check it out! 

[Maintenance Manager project deployed to Render](https://maintenance-manager.onrender.com)

## Additional Info
For demonstration purposes, you can use the following login credentials:

* Username: admin
* Password: Super1234User!
#### These credentials provide access, allowing you to explore the application's features.