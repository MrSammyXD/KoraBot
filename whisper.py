# © Made By KoraTeam
# Join Official Channel @KoraTeam
from Modules.utils import *
from Modules.cmdhelp import CmdHelp


@kora.on(admin_cmd(pattern="whisper ?(.*)"))
@kora.on(sudo_cmd(pattern="whisper ?(.*)", allow_sudo=True))
async def whisper(event):
    if event.fwd_from:
        return
    korawspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, korawspr)
    await tap[0].click(event.chat_id)
    await event.delete()

CmdHelp("whisper").add_command(
  "whisper", "<your message> <reciver username>", "Sends a whisper message to a particular person!"
).add()
