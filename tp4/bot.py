# Un bot est un logiciel informatique qui est créé à partir d'une application et qui peut être vu comme un utilisateur à part entière
# Le logging est la gestion des logs, et les logs sont les fichiers qui vont garder un historique des activités des événements

from discord import Client
import discord


class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.run("OTU4NjkxMzU3NzYzOTg1NDQ4.YkRA5w.cZbbPlnBSfvTHjilWINvEwq2pbE")

   #
    # Créer un événement
    async def on_ready(self):
        print("Le bot est prêt !")

    async def on_message(ctx, message):
        if message.content == "Ping":
            await message.channel.send("Pong")


bot = MyBot()  # instance = appel de fonction
