import amino
import time

email = ""  # Set your own password here!
password = ""  # Set your own password here!
cid = "226547416"  # Community ID

client = amino.Client()
client.login(email=email, password=password)
print("Bot logged in")
sub = amino.SubClient(comId=cid, profile=client.profile)
print("Bot logged onto the community, id:", cid, "\nBot Name:", sub.profile.nickname)


join = """welcome in the chat"""

@client.callbacks.event('on_group_member_join')
def on_group_member_join(data):
        nick = data.message.author.nickname
        msg = {
        'message': f"{join}\n\n[CB]{nick} welcome 🌹🌹🌹🌹!!",
        'chatId': data.message.chatId,
        'mentionUserIds': [data.message.author.userId]
        }
        sub.send_message(**msg)
def socketRoot( ) :
	j = 0
	while True:
		if j >= 30:
			print("updating socket...")
			client.socket.close( )
			client.socket.start( )
			print("updated socket!")
			j = 0
		j += 1
		time.sleep(1)
socketRoot( )			        
