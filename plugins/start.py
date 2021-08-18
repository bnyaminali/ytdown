from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["دەستپێکردن"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/mad_tk")],
             [InlineKeyboardButton("Snapchat", url="https://snapchat.com/add/bnyaminali")],
        [InlineKeyboardButton(
            "ریپۆرت دان لە بۆت 😊", url="https://t.me/bny0min")]
    ])
    welcomed = f"سڵاو <b>{message.from_user.first_name}</b>\n/help کلیک بکە بۆ جۆنییەتی کارکردن"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
