# By @TroJanzHEX
import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Help", callback_data="help_data"),
                        InlineKeyboardButton("Bot ගැන", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Developer ගැන", url="https://t.me/Zitron_Kenway")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="start_data"),
                        InlineKeyboardButton("About", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Developer ගැන", url="https://t.me/Zitron_Kenway")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="help_data"),
                        InlineKeyboardButton("START", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Developer ගැන", url="https:t.me/zitron_Kenway")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
