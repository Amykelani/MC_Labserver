# MC_Labserver
A server for coordinating work between chemistry robots. 

Uses Flask to create a web interface for users to monitor running robots and reactions. Robots can connect to the robots_api to get new instructions or to post their results.

## Setting up MariaDB
#### Ubuntu/Raspberry Pi OS

All `code blocks` signal that the command should be entered into a terminal using a user account with **sudo** privelages

`sudo apt-get update`

`sudo apt-get install mariadb-server mariadb-client mariadb-backup`

For new MariaDB installations, the next step is to run the included security script. This script changes some of the less secure default options for things like remote root logins and sample users.

`sudo mysql_secure_installation`

Configure the server to run on startup and start the server:

`sudo systemctl enable mariadb.service`

`sudo systemctl start mariadb.service`

The server can also be started using:

`sudo service mysql start`

Log in using the root password you just set:

`sudo mysql -u root -p`

Great, let's set up the database for the web server using MySQL:

```
CREATE DATABASE IF NOT EXISTS UJ_RobotsDB;
USE UJ_RobotsDB;
```

Let's set up a user for the flask app to use, and grant them access to the database:

```
CREATE USER 'username'@localhost identified by 'password';

GRANT ALL PRIVILEGES ON UJ_RobotsDB.* TO 'username'@localhost IDENTIFIED BY 'password';
```
You can now quit the MariaDB shell:

`QUIT`

To set up the correct tables for the webserver, we need mysqlclient and flask:

```
sudo apt-get install default-libmysqlclient-dev build-essential
pip3 install mysqlclient
```

Now you can run the database creation scripts for the web server, these are:

1. users.py
2. robots.py
3. reactions.py
4. reaction_status.py
5. robots_queue.py

To run each of the scripts navigate to the directory you unzipped or cloned the repository and run:

`python3 script_name.py`

Each script will prompt you to login with your database credentials, then it will create the database tables. You should see a summary of the items inserted and a message that they have been successfully inserted into the database.

### Setting up required python libraries
First, run the following to set up the connectors for python:

`sudo apt-get install libmariadb3 libmariadb-dev`

The following python libraries are required for the web server:

1. flask 
2. flask_sqlalchemy
3. flask-login
3. mariadb
4. python-dotenv

```
pip3 install flask flask_sqlalchemy flask-login
pip3 install mariadb
pip3 install python-dotenv
```

### Setting up flask config
To run the server we need to configure the secret key and database URI in a .env file. The secret key helps keep client sessions secure, and the database URI allows the webserver to connect to the MariaDB database.

Using the terminal, first navigate to the MC_Labserver directory and run random_key.py:
```
python3 random_key.py
```
Copy the key generated by that script. 

Create a .env file in the MC_Labserver/MC_Labserver directory containing the following:

```
SECRET_KEY = b'the_secret_key_you_generated'
SQLALCHEMY_DATABASE_URI = "mariadb+mariadbconnector://database_username:database_password@127.0.0.1:3306/UJ_RobotsDB"
```

On Windows you can use Notepad to make a .env file. Open Notepad, type in the above information, then use *save as* to save the file with the name ".env". 
