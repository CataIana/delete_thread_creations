from disnake import Intents, Status, MessageType, Game, Message, Client
from disnake.errors import HTTPException, NotFound, Forbidden

TOKEN = ""

class NoThreadCreationMessages(Client):
    def __init__(self):
        intents = Intents.none()
        intents.guilds = True  # To ensure guild cache is up to date
        intents.messages = True  # Obvious
        super().__init__(intents=intents, activity=Game(name="removing thread messages"))

    async def on_message(self, message: Message):
        if message.type == MessageType.thread_created:
            try:
                await message.delete()
                print(f"Deleted a thread creation message in {message.guild} :)")
            except HTTPException:
                pass
            except NotFound:
                pass
            except Forbidden:
                pass

    async def close(self):
        print("Shutting down...")
        await self.change_presence(status=Status.invisible)
        await super().close()

    async def on_ready(self):
        print(f"Logged in as\n{self.user.name}\n{self.user.id}\n" + "-"*6)


bot = NoThreadCreationMessages()
bot.run(TOKEN)
