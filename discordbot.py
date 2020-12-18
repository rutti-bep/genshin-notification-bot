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
    print(bot.daily)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content == '/daily':
        await message.channel.send(embed=bot.getDaily())

    if message.content == '/weekly':
        embed=discord.Embed(title="ボス", color=0x31af4b)
        embed.add_field(name="トワリン", value=":x:", inline=True)
        embed.add_field(name="狼", value=":white_check_mark:", inline=True)
        embed.add_field(name="タルタル", value=":x:", inline=True)
        await message.channel.send(embed=embed)

        embed=discord.Embed(title="評判", color=0xc30404)
        embed.add_field(name="討伐", value="1/3", inline=True)
        embed.add_field(name="任務", value="3/3", inline=True)
        await message.channel.send(embed=embed)

        await message.channel.send('*mm/ddまで*')

# Botの起動とDiscordサーバーへの接続
client.run(settings.DiscordApiKey)
