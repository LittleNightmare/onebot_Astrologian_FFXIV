import nonebot
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.log import logger
from nonebot.params import State
from .config import Config
from .data_source import luck_daily

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())
luck = on_command("luck", aliases={"占卜", "zhanbu"}, temp=False, priority=5)
group: bool = True


@luck.handle()
async def ordered_redraw(bot: Bot, event: Event, state: dict=State()):
        await luck.send(message="开拓命运吧", at_sender=group)
        await luck.finish(await luck_daily(user_id=int(event.get_user_id()), redraw=True, group_message=group),
                          at_sender=group)


