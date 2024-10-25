import asyncio
from telethon import TelegramClient

# Your API credentials
api_id = 28960121
api_hash = '080b29f6fc08bc69f233ca471b259103'
phone_number = '+96176696385'
channels = ['C_Military1', 'almayadeen']

async def get_messages():
    client = TelegramClient('session_name', api_id, api_hash)

    await client.start(phone=phone_number)

    all_messages = []
    for channel in channels:
        # Get the last 10 messages from the channel
        async for message in client.iter_messages(channel, limit=10):
            all_messages.append({
                'title': message.sender_id,  # you can customize this
                'message': message.message
            })

    await client.disconnect()
    return all_messages

def fetch_telegram_messages():
    # Ensure the async function runs in an event loop
    return asyncio.run(get_messages())
