from pyrogram import Client, filters

api_id: int = your api id
api_hash: str = "your api hash"
token: str = "bot token"
Client = Client("unpinbot", api_id, api_hash, bot_token=token)


@Client.on_message(filters.linked_channel)
async def autopin(Client, Message):
    await Message.unpin()


@Client.on_message(filters.private)
async def privatemsg(client, Message):
    await Message.reply("text")


Client.run()
