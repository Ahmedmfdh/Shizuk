import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["سكران"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b557e5cffeadff7704af9.jpg",
caption=f"""**▷✘ ||𝘼𝘽𝙊𝙈𝘼𝙕𝙀𝙉|| ☬『 مــ ـٰٖمـوِٰلٰ 』 ♯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "CHANNEL", url=f"https://t.me/EE_0B"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "✘ ||𝘼𝘽𝙊𝙈𝘼𝙕𝙀𝙉|| ☬『 مــ ـٰٖمـوِٰلٰ 』", url=f"https://t.me/H_A_S_I_S_A"),
                ],
            ]
        ),
    )
