from telethon import TelegramClient, events
import asyncio

api_id = 24860776
api_hash = 'ef3e75795eb1a2f4026227bd21a98af3'
source_channel = -1002317190002  # только username, без ссылки
target_chat = -1002667546912

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        await client.send_message(target_chat, event.message)
        print(f"Переслано: {event.message.text[:50]}")
    except Exception as e:
        print(f"Ошибка: {e}")

async def main():
    await client.start()
    print("Бот запущен. Ждём новые сообщения...")
    await asyncio.Future()

client.loop.run_until_complete(main())
