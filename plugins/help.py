from pyrogram import Client, Filters


@Client.on_message(Filters.command(["یارمەتی"]))
async def start(client, message):
    helptxt = f" bnyaminali;سناپچات @bny0minبۆ دابەزاندنی ڤییدیۆ و گۆرینی بۆ دەنگ تەنها بە ناردنی لینکی ڤیدیۆکە ڤیدیۆکەت بۆ دادەبەزێت درووستکراوە لە لایەن؛ "
    await message.reply_text(helptxt)
