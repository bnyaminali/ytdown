from pyrogram import Client, Filters


@Client.on_message(Filters.command(["یارمەتی"]))
async def start(client, message):
    helptxt = f"@bny0minلینکی ڤیدیۆکە بنێرە بەڵام تەنها ١ لینک دوای دابەزاندنی ڤیدیۆکەت ئەوەی تر بنێرە درووستکەر؛ "
    await message.reply_text(helptxt)
