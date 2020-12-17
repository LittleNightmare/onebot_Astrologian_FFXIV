from .config import Config
import nonebot

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event

from .data_source import luck_daily

luck = on_command("luck", aliases={"占卜", "zhanbu"})


@luck.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args == "help":
        await luck.finish("使用命令/luck，/占卜，/zhanbu获得日常占卜结果\n"
                          "对结果不满意，可以在占卜后回复“r”来重抽")
    else:
        await luck.send(await luck_daily(event.user_id))
        # state["redraw"] = False


@luck.receive()
async def ordered_redraw(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if "r" in args:
        await luck.send("开 拓 命 运")
        await luck.finish(await luck_daily(event.user_id, True))

