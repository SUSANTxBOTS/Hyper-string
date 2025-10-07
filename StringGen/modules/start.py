from pyrogram import filters, enums
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/6ofgj0.jpg",
        caption=f"""<b>┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼─── ⏤͟͞●
┆◍ ʜᴇʏ ㅤ-</b> {message.from_user.first_name}
<b>┆◍ ɪ'ᴍ :</b>  {Anony.mention},
<b>└──────────────────────•
 ❀ ɪ'ᴍ ᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇ ʙᴏᴛ.
 ✤ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ.
 ❃ 𝛅ᴜᴘᴘᴏʀᴛ - ᴘʏʀᴏɢʀᴀᴍ | ᴛᴇʟᴇᴛʜᴏɴ.
 ✮ ηᴏ ɪᴅ ʟᴏɢ ᴏᴜᴛ ɪssᴜᴇ & ғᴜʟʟ sᴇᴄᴜʀᴇ.
•────────────────────────•
 ❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ  :-  <a href="https://t.me/ThronexCodex">𝗧𝗵𝗿𝗼𝗻𝗲𝘅 𝗖𝗼𝗱𝗲𝘅</a>
•────────────────────────•</b>""",
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.HTML
    )
    await add_served_user(message.from_user.id)
