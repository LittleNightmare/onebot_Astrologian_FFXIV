import random

from nonebot import on_command, CommandSession, MessageSegment
from nonebot.permission import *

from . import utils


# on_command 装饰器将函数声明为一个命令处理器
@on_command('luck', aliases=('占卜', 'zhanbu'), permission=EVERYBODY)
async def luck(session: CommandSession):
    if len(utils.war or utils.magic or utils.land or utils.hand or utils.stains) == 0:
        await utils.initialization()
    # 拿到命令使用者的qq号
    caller_qq_number = session.ctx['user_id']
    # 生成当天种子
    r = random.Random(await utils.get_seed(caller_qq_number))
    # content
    at = MessageSegment(type_="at", data={"qq": caller_qq_number})
    luck_number = str(r.randint(1, 100))
    luck_job = await utils.sub_event(str(r.choice(utils.war + utils.magic + utils.land + utils.hand)))
    luck_event = r.choice(utils.EVENT_LIST)
    unlucky_event = utils.EVENT_LIST.copy()
    unlucky_event.remove(luck_event)
    unlucky_event = r.choice(unlucky_event)
    stain = r.choice(utils.stains)
    hint = await utils.get_hint(luck_number, luck_job, luck_event, unlucky_event, stain)

    message = at + "\n运势: " + luck_number + "% 幸运职业: " \
              + luck_job + "\n宜: " + luck_event + " 忌: " + unlucky_event + "幸运油漆: " + stain + "\n" + hint
    # print(r.randint(0, len(EVENT_LIST) - 2))
    await session.send(message)


# luck.args_parser 装饰器将函数声明为 luck 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@luck.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['luck'] = stripped_arg
        return

    # if not stripped_arg:
    #     # 用户没有发送有效的订阅（而是发送了空白字符），则提示重新输入
    #     # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
    #     session.pause(
    #         '输入不能为空！')

    # 如果当前正在向用户询问更多信息，且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg
