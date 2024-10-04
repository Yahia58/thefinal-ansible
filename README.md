# Ansible Project for Application Deployment

This project is an Ansible playbook designed to automate the deployment of a web application using Flask. It configures the necessary services, sets up the application files, and ensures the environment is ready for running the application.

## Project Structure

. ├── ansible.cfg # Configuration file for Ansible ├── group_vars │ └── all │ └── vault.yml # Variables file, typically contains sensitive data (encrypted) ├── inventory.ini # Inventory file listing the target hosts ├── kk.pem # Private key for SSH access to servers ├── roles # Directory containing Ansible roles │ ├── app_deployment # Role for deploying the application │ │ ├── files # Application files │ │ │ ├── app # Application directory │ │ │ │ ├── index.html # Main HTML file │ │ │ │ ├── scripts │ │ │ │ │ └── app.js # JavaScript file │ │ │ │ ├── server │ │ │ │ │ └── app.py # Flask application server script │ │ │ │ └── styles │ │ │ │ └── main.css # CSS file │ │ │ └── my_app.service # Systemd service file for the application │ │ ├── handlers # Handlers for the role │ │ │ └── main.yml │ │ └── tasks # Tasks for the role │ │ ├── main.yml │ │ └── main.yml.save │ ├── database # Role for database configuration │ │ ├── handlers │ │ │ └── main.yml │ │ └── tasks │ │ └── main.yml │ ├── dns_config # Role for DNS configuration │ │ ├── files │ │ │ └── named.conf │ │ ├── handlers │ │ │ └── main.yml │ │ └── tasks │ │ └── main.yml │ ├── firewall # Role for configuring the firewall │ │ ├── handlers │ │ │ └── main.yml │ │ └── tasks │ │ └── main.yml │ ├── users # Role for user management │ │ └── tasks │ └── webserver # Role for web server configuration │ ├── handlers │ │ └── main.yml │ ├── tasks │ │ └── main.yml │ └── templates │ ├── httpd.conf.j2 # Jinja2 template for httpd configuration │ └── my_app.service.j2 # Jinja2 template for systemd service ├── site.yml # Main playbook file └── {changed: # Placeholder for potential changes

## Images

### Image 1
![Image 1 Description](Screenshot.png)

### Image 2
![Image 2 Description](run.png)
