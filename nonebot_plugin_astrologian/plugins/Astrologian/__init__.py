from .config import Config
import nonebot

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event

from .data_source import luck_daily

luck = on_command("luck", aliases={"占卜", "zhanbu"}, temp=False, priority=5)


@luck.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip().split()
    state["help"] = False
    state["redraw"] = False
    state["test"] = ""
    if args:
        if "help" in args:
            state["help"] = True
        elif ("r" in args) or ("重抽" in args) or ("redraw" in args):
            state["redraw"] = True
        elif "test" in args:
            state["test"] = args[1]

    else:
        await luck.send(await luck_daily(event.user_id, False), at_sender=True)


@luck.got("redraw")
async def ordered_redraw(bot: Bot, event: Event, state: dict):
    if state["redraw"]:
        await luck.finish(await luck_daily(event.user_id, True), at_sender=True)


@luck.got("help")
async def luck_help(bot: Bot, event: Event, state: dict):
    if state["help"]:
        await luck.finish("使用命令/luck，/占卜，/zhanbu获得日常占卜结果\n"
                          "对结果不满意，可以使用\"/luck r\"来重抽\n"
                          "查看详细: https://github.com/LittleNightmare/onebot_Astrologian_FFXIV/tree/nonebot2")


@luck.got("test", prompt="参数？")
async def luck_test(bot: Bot, event: Event, state: dict):
    if state["test"] != "":
        print("test", ":", state["test"])
        await luck.finish(await luck_daily(int(state["test"]), False), at_sender=True)
