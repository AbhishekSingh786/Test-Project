# Steps For BOT Integration

- Add the Script from BOT_SCRIPT.txt in Website

# Steps For RASA X Installation on Server

[Follow this Link for Complete RASA X Installation Guide](https://rasa.com/docs/rasa-x/installation-and-setup/install/docker-compose)

# Steps After Complete Installation on Server

- Go to /etc/rasa Directory

- Edit credentials.yml File with the Following Code

  `socketio:
  user_message_evt: user_uttered
  bot_message_evt: bot_uttered
  session_persistence: true`

- Save the Changes in File

- Restart Docker Compose

- Login to RASA X Server with Password You've Provided in the Installation

- Add Latest Model From /MASTER/models Directory (Note: You have to Clone this Directory to Upload Model to RASA X Server)

- After Uploading Model Make the Model Active and You are Ready to Go

- Note :- As For Now Currently Don't use "Connect to a Git Repositry Feature" on RASA X Server as It is BETA Feature and Sometimes It Doesn't Work Properly

- LINK - [Current RASA X Server Deployment (for Devs)](http://51.158.96.209/login?username=me&password=12345678)
- LINK - [RASA X Test Server (for Testers)](http://51.158.96.209/guest/conversations/production/a262832a12c841ce8bd3ad07a919c122)