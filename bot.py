from pyrogram import Client, filters
import asyncio


api_id = your api id
api_hash = 'your api hash'
token = "bot token"



Client = Client("unpinbot", api_id, api_hash, bot_token=token)


@Client.on_message(filters.linked_channel)
async def autopin(Client, Message):
    await Client.unpin_chat_message(
    Message.chat.id
    )
    
    
    
@Client.on_message(filters.private)
async def privatemsg(client, Message):
  await  Message.reply("""text""")

    



Client.run()
