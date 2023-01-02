############################################
# To use this change your  bot token and #
# open_api key.                            #
#                                          #
# TO run this, run main.py                 #
#                                          #
# This is an EXTREMELY BASIC chat bot that #
# uses openai's apis to carry on a         #
# converstaion.                            #
############################################

import discord
import openai

def run_discord_bot():
    botToken = '_YOUR_BOT_TOKEN_HERE_'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print('------------------')
        print(f'ChatGPT bot has logged in as {client.user}')
        print(f'latency: {client.latency}')
        print(f'user id: {client.user.id}')
        print('------------------')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('>'):
            prompt = message.content
            openai.api_key = '_YOUR_OPEN_API_KEY_HERE_'
            response = openai.Completion.create(
                model="text-davinci-003", 
                prompt=prompt,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]                                
            )

            response_text = response["choices"][0]["text"]
            await message.channel.send(response_text)

    client.run(botToken)

