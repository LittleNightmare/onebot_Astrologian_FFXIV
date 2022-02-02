import nonebot
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.log import logger

from .config import Config
from .data_source import luck_daily

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())
luck = on_command("luck", aliases={"占卜", "zhanbu"}, temp=False, priority=5)
group: bool = True


@luck.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    # 通过是否为group判读信息结构
    global group
    group = True if event.get_event_name().find("group") != -1 else plugin_config.same_message_structure
    args: list = str(event.get_message()).strip().split()
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
        await luck.send(await luck_daily(user_id=int(event.get_user_id()), redraw=False, group_message=group),
                        at_sender=group)


@luck.got("redraw")
async def ordered_redraw(bot: Bot, event: Event, state: dict):
    if state["redraw"]:
        await luck.send(message="开拓命运吧", at_sender=group)
        await luck.finish(await luck_daily(user_id=int(event.get_user_id()), redraw=True, group_message=group),
                          at_sender=group)


@luck.got("help")
async def luck_help(bot: Bot, event: Event, state: dict):
    if state["help"]:
        await luck.finish("使用命令/luck，/占卜，/zhanbu获得日常占卜结果\n"
                          "对结果不满意，可以使用\"/luck r\"来重抽\n"
                          "插件名：onebot_Astrologian_FFXIV 当前支持版本：nb2.0.0a9")


@luck.got("test", prompt="参数？")
async def luck_test(bot: Bot, event: Event, state: dict):
    if state["test"] != "":
        test_id = state["test"]
        logger.debug("test" + ": " + test_id)
        await luck.finish(await luck_daily(user_id=int(test_id), redraw=False, group_message=group),
                          at_sender=group)
