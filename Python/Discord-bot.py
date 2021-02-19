import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Hurensohn"):
        await message.channel.send("Selber")

    if message.author.id == 452487678345347083:
        await message.channel.send("Du Hurensohn")

client.run("MzIyMDc1MTE4MjAzNDM3MDU2.YAp4Dg.vc0a1wuYucSgkJU38DN7cIzRlnA", bot=False)