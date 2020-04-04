# Project on python to automate creation react app plus initial commit.

Installation:

- Open terminal
- Type nano ~/.bashrc
- After last line add source ~/path/to/.my_create_command.sh
- ctrl+o, enter
- ctrl+x
- install selenium, python-dotenv, Firefox driver
- Create in root file .env

---

Add in this file:
user = "username123"
password = "password123"
py_path = "/path/to/project/folder"
driver_path = "/usr/local/bin/"

---

Firefox driver should be placed in /usr/local/bin/

# Helpful links:

- Open .bashrc file: https://askubuntu.com/questions/127056/where-is-bashrc
- Firefox driver: https://github.com/mozilla/geckodriver/releases
- How to create terminal command: https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e