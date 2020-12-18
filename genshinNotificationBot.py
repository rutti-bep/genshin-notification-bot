import discord
from enum import Enum

class embedColor(Enum):
    RED=0xc30404
    GREEN=0x31af4b

class genshinNotificationBot:
    daily = {"resin":0,"task":False,"pickingUpRelics":False}
    weekly = {"boss":{"Dvalin":False,"Andrius":False,"Childe":False},"reputation":{"bounties":0,"requests":0}}
