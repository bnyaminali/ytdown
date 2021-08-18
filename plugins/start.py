from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["دەستپێکردن"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("چەناڵ", url="https://t.me/mad_tk")],
        [InlineKeyboardButton(
            "درووستکەر", url="https://t.me/bny0min")]
    ])
    welcomed = f"سڵاو! <b>{message.from_user.first_name}</b>\n /help بەخێربێی بۆ چۆنیەتی کارپێکردن کلیک لەمە بکە "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
