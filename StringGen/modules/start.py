from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/ljyrvb.jpg",
        caption=f"""**┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼─── ⏤͟͞●
┆◍ ʜᴇʏ {msg.from_user.mention}
┆◍ ɪ'ᴍ : {me2} 
└──────────────────────•
 ❀ ɪ'ᴍ ᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇ ʙᴏᴛ.
 ✤ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ.
 ❃ 𝛅ᴜᴘᴘᴏʀᴛ - ᴘʏʀᴏɢʀᴀᴍ | ᴛᴇʟᴇᴛʜᴏɴ.
 ✮ ηᴏ ɪᴅ ʟᴏɢ ᴏᴜᴛ ɪssᴜᴇ & ғᴜʟʟ sᴇᴄᴜʀᴇ.
•────────────────────────•
 ❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ  :-  [ꪜ 𝛊 ɭ ɭ ᧘ 𝛊 𝛈](t.me/iamakki001) 
•────────────────────────•**""",
        
        reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="˹ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ˼", callback_data="GenByBots")
        ],
        [
            InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", user_id=OWNER_ID),
            InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/+wPjAlUcObehiZDM1")
        ],
        [
            InlineKeyboardButton("˹ ʙᴀsɪᴄ ɢᴜɪᴅᴇs ˼", callback_data="help")
        ]
    ]
        )
    )
    
