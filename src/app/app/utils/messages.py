from app.utils import bot


async def send_message_to_chat(peer_id: int, text: str) -> None:
    await bot.send_message(peer_id, text)
