import discord
import datetime
from enum import Enum

class EmbedColor(Enum):
    RED=0xc30404
    GREEN=0x31af4b

class reactionEmoji(Enum):
    TRUE=":white_check_mark:"
    FALSE=":x:"

def returnEmbedColor(Flag):
    if Flag:
        return EmbedColor.GREEN.value
    else:
        return EmbedColor.RED.value

    #return EmbedColor.GREEN.value if Flag else EmbedColor.RED.value

def returnReactionEmoji(Flag):
    if Flag:
        return reactionEmoji.TRUE.value
    else:
        return reactionEmoji.FALSE.value

    #return reactionEmoji.TRUE.value if Flag else reactionEmoji.FALSE.value


class genshinNotificationBot:
    resin = 0;
    daily = {"task":False,"pickingUpRelics":False}
    weekly = {"boss":{"Dvalin":False,"Andrius":False,"Childe":False},"reputation":{"bounties":0,"requests":0}}

    def getDaily(self):
        embed = discord.Embed(title="デイリー",description=datetime.date.today().strftime("%m/%d")+"日分",color=returnEmbedColor( self.daily["task"] and self.daily["pickingUpRelics"] ))
        embed.add_field(name="樹脂", value= "{}/160(残り時間:{}分 満杯{})".format(self.resin,(160-self.resin)*8,(datetime.datetime.now()+datetime.timedelta(minutes=(160-self.resin)*8)).strftime("%H:%M")), inline=False)
        embed.add_field(name="任務", value= returnReactionEmoji(self.daily["task"]), inline=True)
        embed.add_field(name="聖遺物拾い", value= returnReactionEmoji( self.daily["pickingUpRelics"]), inline=True)
        embed.set_footer(text="更新は5時")
        return embed

    def getWeekly(self):
        messages = [];
        messages.append(discord.Embed(title="ボス", color=returnEmbedColor(self.weekly["boss"]["Dvalin"] and self.weekly["boss"]["Andrius"] and self.weekly["boss"]["Childe"])))
        messages[0].add_field(name="トワリン", value=returnReactionEmoji( self.weekly["boss"]["Dvalin"] ), inline=True)
        messages[0].add_field(name="アンドリウス", value=returnReactionEmoji( self.weekly["boss"]["Andrius"] ), inline=True)
        messages[0].add_field(name="タルタリヤ", value=returnReactionEmoji( self.weekly["boss"]["Childe"] ), inline=True)

        messages.append(discord.Embed(title="評判", color=returnEmbedColor(self.weekly["reputation"]["bounties"] == 3 and self.weekly["reputation"]["requests"] == 3)))
        messages[1].add_field(name="討伐", value="{}/3".format(self.weekly["reputation"]["bounties"]), inline=True)
        messages[1].add_field(name="任務", value="{}/3".format(self.weekly["reputation"]["requests"]), inline=True)

        today = datetime.date.today()
        nextMonday = today+datetime.timedelta(days=6-today.weekday())
        messages.append('*{}まで*'.format( nextMonday.strftime("%m/%d")))

        return messages

    def set(self, *args):
        #すごい雑実装したのであとでなおす
        print(args);
        if(args[0]=="resin"):
            self.resin = int(args[1])
            return self.resin
        elif(args[0]=="daily"):
            self.daily[args[1]] = args[2]
            return self.daily
        elif(args[0]=="weekly"):
            self.weekly[args[1]][args[2]] = args[3]
            return self.weekly

