from pyrogram import Client, Filters


@Client.on_message(Filters.command(["یارمەتی"]))
async def start(client, message):
    helptxt = f"@bny0minلینکی ڤیدیۆکە بنێرە یاخوود لە یوتیوب شەیری بکە بۆ ئەم بۆت ؛"
    await message.reply_text(helptxt)
