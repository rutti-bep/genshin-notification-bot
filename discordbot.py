# インストールした discord.py を読み込む
import discord
import settings
from genshinNotificationBot import genshinNotificationBot

# 接続に必要なオブジェクトを生成
client = discord.Client()
bot = genshinNotificationBot()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == '/daily':
        await message.channel.send(embed=bot.getDaily())

    if message.content == '/weekly':
        for _message in bot.getWeekly():
            if isinstance(_message, str): 
                await message.channel.send(_message)
            else: 
                await message.channel.send(embed =_message)


# Botの起動とDiscordサーバーへの接続
client.run(settings.DiscordApiKey)
