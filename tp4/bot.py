# Un bot est un logiciel informatique qui est créé à partir d'une application et qui peut être vu comme un utilisateur à part entière
# Le logging est la gestion des logs, et les logs sont les fichiers qui vont garder un historique des activités des événements

from distutils.cmd import Command
from email.policy import default
from discord import Client
import discord

# on charge les variables de notre fichier config
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="config")


class MyBot(Client):

    def __init__(self):

        intents = discord.Intents.default()
        intents.presences = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)
    # Créer un événement

    async def on_ready(self):
        print("Le bot est prêt !")
        print(f"{self.user.display_name} est connecté au serveur")

    async def on_message(ctx, message):
        if message.content == "Ping":
            await message.channel.send("Pong")  # commentaire

    # Reagi quand les membres qui arrivent et souhaite bienvenue aux nouveaux arrivants
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Salut le jeuns {0.mention} dans {1.name}!'.format(
                member, guild)
            await guild.system_channel.send(to_send)


bot = MyBot()  # instance = appel de fonction
bot.run(os.getenv("TOKEN"))
