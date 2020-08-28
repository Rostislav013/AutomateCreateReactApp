# Project on python to automate creation react app plus initial commit.

Installation:

- Open terminal
- Type nano ~/.bashrc
- After last line add: source ~/path/to/.my_create_command.sh
- ctrl+o, press ENTER
- ctrl+x
- Install selenium: pip install selenium
- Install python-dotenv: pip install python-dotenv
- Install Firefox driver: https://github.com/mozilla/geckodriver/releases
- Create in root file .env

---

Add in .env file:

- user = "username123"
- password = "password123"
- py_path = "/path/to/project/folder"
- driver_path = "/usr/local/bin/"

---

Firefox driver should be placed in /usr/local/bin/

---

Use:

- Open terminal
- Type "create name", where name is the name of your application to create
- During process it might ask github username and password

---

Project based on https://www.youtube.com/watch?v=7Y8Ppin12r4&list=PL5tVJtjoxKzqacJbIGbFbNTu7h2v4tsaF&index=2

# Helpful links:

- Open .bashrc file: https://askubuntu.com/questions/127056/where-is-bashrc
- Firefox driver: https://github.com/mozilla/geckodriver/releases
- How to create a terminal command: https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e
