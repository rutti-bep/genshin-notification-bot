import discord
import datetime
from enum import Enum

class EmbedColor(Enum):
    RED=0xc30404
    GREEN=0x31af4b

class reactionEmoji(Enum):
    TRUE=":white_check_mark:"
    FALSE=":x:"

class genshinNotificationBot:
    daily = {"resin":0,"task":False,"pickingUpRelics":False}
    weekly = {"boss":{"Dvalin":False,"Andrius":False,"Childe":False},"reputation":{"bounties":0,"requests":0}}

    def getDaily(self):
        embed = discord.Embed(title="デイリー",description=datetime.date.today().strftime("%m/%d")+"分",color=EmbedColor.GREEN.value if self.daily["task"] and self.daily["pickingUpRelics"] else EmbedColor.RED.value)
        embed.add_field(name="樹脂", value= "{}/160(残り時間:{}min 満杯)".format(self.daily["resin"],(160-self.daily["resin"])*8), inline=False)
        embed.add_field(name="任務", value= reactionEmoji.TRUE.value if self.daily["task"] else reactionEmoji.FALSE.value, inline=True)
        embed.add_field(name="聖遺物拾い", value=reactionEmoji.TRUE.value if self.daily["pickingUpRelics"] else reactionEmoji.FALSE.value, inline=True)
        embed.set_footer(text="更新は5時")
        return embed
