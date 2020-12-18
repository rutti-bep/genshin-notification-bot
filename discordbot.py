import discord
from discord.ext import commands
import settings
from genshinNotificationBot import genshinNotificationBot

discordBot = commands.Bot(command_prefix='/')
genshinBot = genshinNotificationBot()

# 起動時に動作する処理
@discordBot.event
async def on_ready():
    print('ログインしました')
    print(discordBot.user.name)
    print(discordBot.user.id)

@discordBot.command()
async def daily(ctx):
    await ctx.send(embed=genshinBot.getDaily())

@discordBot.command()
async def weekly(ctx):
    for _message in genshinBot.getWeekly():
        if isinstance(_message, str): 
            await ctx.send(_message)
        else: 
            await ctx.send(embed =_message)

@discordBot.command()
async def set(ctx,*args):
    await ctx.send( genshinBot.set(*args));

discordBot.run(settings.DiscordApiKey)
