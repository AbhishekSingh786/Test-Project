# Steps For Adding Widget in the Website

- Add the Following Script in the Body Tag of Website 


<div id="webchat"></div>
<script src="https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.min.js"></script>
<script>
  WebChat.default.init({
    selector: "#webchat",
    initPayload: "/get_started",
    customData: {"language": "en"},
    socketUrl: "http://51.158.96.209",
    socketPath: "/socket.io/",
    title: "Welcome",
    subtitle: "I am Admin ChatBot",
    params: {"storage": "session"}
  })
</script>

Note - Change the socketUrl with the RASA X Server URL

# Steps For RASA X Installation on Server

[Follow this Link for Complete RASA X Installation Guide](https://rasa.com/docs/rasa-x/installation-and-setup/install/docker-compose)

# Steps After Complete Installation on Server

- Go to /etc/rasa Directory

- Edit credentials.yml File with the Following Information

  `socketio:
  user_message_evt: user_uttered
  bot_message_evt: bot_uttered
  session_persistence: true`

- Save the Changes in File

- Restart Docker Compose

- Login to RASA X Server with Password You've Provided in the Installation

- Add Latest Model From /models Directory (Note: You have to Clone this Directory to Upload Model to RASA X Server)

- After Uploading Model Make the Model Active and You are Ready to Go

- Note :- As For Now Currently Don't use "Connect to a Git Repositry Feature" on RASA X Server as It is BETA Feature and Sometimes It Doesn't Work Properly

- LINK - [Current RASA X Server Deployment (for Devs)](http://51.158.96.209/login?username=me&password=12345678)
- LINK - [RASA X Test Server (for Testers)](http://51.158.96.209/guest/conversations/production/a262832a12c841ce8bd3ad07a919c122)