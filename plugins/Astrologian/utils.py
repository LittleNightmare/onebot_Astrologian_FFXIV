import csv
import datetime
import hashlib
import random
from pathlib import Path

PATH_Astrologian = Path(__file__).parent.absolute()
# TODO 写子项目
EVENT_LIST = ["诸事", "优雷卡", "刷外观", "找CP", "偷情", "抓奸",
              "开荒", "挂机", "挖宝", "采集", "钓鱼王", "PVP", "逛RP店",
              "日随", "装修", "蹲房", "练级", "拍照", "刷危命",
              "炒股", "渡劫", "出警", "刷坐骑", "刷幻化", "幻卡", "喷风",
              "跳跳乐", "赛鸟", "天宫死宫", "快刀一闪", "无"]

war, magic, land, hand, stains = [], [], [], [], []


async def initialization():
    global war, magic, land, hand, stains
    # create unchange vars
    war, magic, land, hand = await get_jobs()
    stains = await get_stain()
    print("占星术士成功拿到卡牌")


# 读取职业列表，计划返回4组list
async def get_jobs():
    war_jobs = []
    magic_jobs = []
    land_jobs = []
    hand_jobs = []
    with open(PATH_Astrologian / "data/ClassJob.csv", mode="r", encoding="utf-8") as f:
        jobs_csv = csv.reader(f)
        for job in jobs_csv:
            if job[4] == "战斗精英":
                if job[1] == job[39].split("之")[0]:
                    # print(job[1])
                    war_jobs.append(job[1])
            elif job[4] == "魔法导师":
                if job[1] == job[39].split("之")[0]:
                    # print(job[1])
                    magic_jobs.append(job[1])
            elif job[4] == "能工巧匠":
                hand_jobs.append(job[1])
            elif job[4] == "大地使者":
                land_jobs.append(job[1])
    return war_jobs, magic_jobs, land_jobs, hand_jobs


# 读取染剂列表
async def get_stain():
    stains = []
    with open(PATH_Astrologian / "data" / "StainTransient.csv", mode="r", encoding="utf-8") as f:
        stains_csv = csv.reader(f)
        for stain in stains_csv:
            if "染剂" in stain[1]:
                # print(stain[1])
                stains.append(stain[1])
    return stains


# 特殊职业创建特殊语句
async def sub_event(key):
    if key == "舞者":
        partner = war + magic
        return key + "-->舞伴: " + random.choice(partner)
    else:
        return key


# copy from https://github.com/Bluefissure/OtterBot
# 针对每个qq用户，通过QQ号和日期生成一个种子
async def get_seed(QQnum):
    today = datetime.date.today()
    formatted_today = int(today.strftime('%y%m%d'))
    strnum = str(formatted_today * QQnum)

    md5 = hashlib.md5()
    md5.update(strnum.encode('utf-8'))
    res = md5.hexdigest()

    return int(res.upper(), 16) % 100 + 1


async def get_hint(luck_number, luck_job, luck_event, unlucky_event, stain):
    # TODO 写个switch
    luck_number = int(luck_number)
    if luck_number > 95:
        return "是欧皇(*′▽｀)ノノ"
    elif luck_number < 5:
        return "是非酋︿(￣︶￣)︿"
    elif luck_event == "诸事":
        return "萨纳兰今天也是艳阳高照啊(￣︶￣)"
    elif unlucky_event == "诸事":
        return "今天是摸鱼的一天！"
    else:
        return "诶诶，咱没有料到呢？肯定是笨蛋梦魇偷懒了[○･｀Д´･ ○]"
