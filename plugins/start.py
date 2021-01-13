from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("😎Owner😎", url="https://t.me/prob3tor")],
        [InlineKeyboardButton(
            "😊Report Bugs😊", url="https://t.me/hackingUC")],
        [InlineKeyboardButton("💠Channel💠", url="https://t.me/Hub_Channel_Network")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nWelcome to Master Youtube Downloader press /help for More info\n Proudly made in 🇱🇰"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
