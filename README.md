# data-representation-project - Peter Finnerty

## Project Overview

***

This project features an API that simulates a system for a Newsagents to order and record stock. It features a RESTFUL API, a DAO, a FLASK server and database to record the stock used.

The intention is to demonstrate an understanding of web-interface architecture. It features 3 files in particular that attempt to do this, a html file for interacting with a server, a server.py file that runs the FLASK server, and a DAO.py file that contains functions with the SQL commands that carry out the CRUD operations.

## Files

***

The below files are found in this project:

1. deliveryDAO.py - python file that uses MYSQL.connetor to SQL commands to the server
2. server_delivery.py - python file that uses FLASK and request to route the DAO commands to the FLASK server and interacts with the database
3. web_delivery.html - the webpage file that allows the browser to interact with the server
4. README - this file, outlining the project intention
5. requirements.txt - a text file containing the libraries that are required to run this project
6. LICENCE - the licence for this repository
7. dbconfig.py - the configuration file containing details for mysql database connection
8. delivery_table.sql - the SQL file containing the create and insert commands for the delivery table
9. .gitignore - the file containing the files that git should ignore when committing


## Installation

***

The following softwares must be installed for this repository to work:
* Anaconda - this will ensure that you can run Python and it's built in libraries. For Windows installation, go to this link: https://docs.anaconda.com/anaconda/install/windows/ - this will also provide instructions for download.

* Jupyter Notebook - this is a web-based computing interface, for runing Python interactively. It is launched from the command line, by first going to the repository address and typing 'jupyter notebook'. This is conveniently downloaded as part of Anaconda, so no installation is necessary.

* Git - you will need to have the Git software running on your machine, in order to copy the machine from GitHub to your local machine. Git can be downloaded here: https://git-scm.com/downloads

* To clone this repository down to your machine, copy the Https URL available on the GitHub repository page and run the following commands in your command terminal:
<br>*clone git@github.com:PJFinnerty/Machine-Learning-and-Statistics.git*
- The repository will then be copied to your local machine current folder, and will not require a password.

- Enter the repository by typing:
<br>*cd Machine-Learning-and-Statistics*

- Open the notebook by typing:
<br>*jupyter notebook*

* Go to your browser, and a tab should have opened on a local host address (typically port 8888). You can traverse the repository files from the Jupyter interface, including the specific notebooks and this README file.

## References

***

1. 'What is a REST API', Red Hat, May 2021, https://www.redhat.com/en/topics/api/what-is-a-rest-api

