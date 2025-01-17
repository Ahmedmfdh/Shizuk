#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(text="قناة السورس 📣", url="https://t.me/EE_0B"), 
            ],[
            InlineKeyboardButton(text="مطور السورس 📢", url="https://t.me/H_A_S_I_S_A"), 
            ],[
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            )
            ],
    ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ],[
        InlineKeyboardButton(text="قناة السورس 📣", url="https://t.me/EE_0B"),
            InlineKeyboardButton(text="مطور السورس 📢", url="https://t.me/H_A_S_I_S_A"),
            ],[
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            )
            ],[
                    InlineKeyboardButton(
                        text=_["S_B_7"], user_id=OWNER
                    ),
            ],[
        InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")
        ]
    ]
    return buttons
