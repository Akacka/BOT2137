import discord
import datetime

client = discord.Client()
#link do bota

#tutaj coś robi

@client.event
async def on_ready():
    print("online jestem")


while True:
    now = datetime.datetime.now()
    if str(now.hour) == '21' and str(now.minute) == '37':
        print("wybiła godzina na kremówke")
        @client.event
        async def on_message():
            general_channel = client.get_channel(816259598494466048)
            print("online jestem")
            await general_channel.send("tak pan bóg powiedział ")
        break








#to coś go budzi do życia
client.run('')
