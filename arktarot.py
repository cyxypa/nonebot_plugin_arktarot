from nonebot import on_fullmatch,on_keyword
from nonebot.adapters.onebot.v11 import Message, MessageSegment,Bot,GroupMessageEvent
from nonebot.exception import MatcherException
from nonebot.rule import to_me
from random import sample, randint, choice
from pathlib import Path
ARCANA_DIR=Path(r"C:\Users\Administrator\Desktop\bot\data\arcana")
spread = [
    [
        "四要素牌阵",
        [
            "第1张牌「火，象征行动，行动上的建议」",
            "第2张牌「气，象征言语，言语上的对策」",
            "第3张牌「水，象征感情，感情上的态度」",
            "第4张牌「土，象征物质，物质上的准备」",
        ],
    ],
    [
        "六芒星牌阵",
        [
            "第1张牌「过去」",
            "第2张牌「现在」",
            "第3张牌「未来」",
            "第4张牌「对策」",
            "第5张牌「环境」",
            "第6张牌「态度」",
            "切牌「预测结果」",
        ],
    ],
    [
        "吉普赛十字阵",
        [
            "第1张牌「对方的想法」",
            "第2张牌「你的想法」",
            "第3张牌「相处中存在的问题」",
            "第4张牌「二人目前的环境」",
            "第5张牌「关系发展的结果」",
        ],
    ],
    ["圣三角牌阵", ["第1张牌「处境」", "第2张牌「行动」", "第3张牌「结果」"]],
    ["时间之流牌阵", ["第1张牌「过去」", "第2张牌「现在」", "切牌「未来」"]],
    [
        "沙迪若之星牌阵",
        [
            "第1张牌「问卜者的感受」",
            "第2张牌「问卜者的问题」",
            "第3张牌「问题下的影响因素」",
            "第4张牌「将问卜者与问题纠缠在一起的往事」",
            "第5张牌「需要注意/考虑的」",
            "切牌「可能的结果」",
        ],
    ],
    [
        "平安扇牌阵",
        [
            "第1张牌「人际关系现状」",
            "第2张牌「与对方结识的因缘」",
            "第3张牌「双方关系的发展」",
            "第4张牌「双方关系的结论」",
        ],
    ],
]
arcana = [
    ["新的开始、冒险、自信、乐观、好的时机", "时机不对、鲁莽、轻信、承担风险", "愚者"],
    [
        "创造力、主见、激情、发展潜力",
        "缺乏创造力、优柔寡断、才能平庸、计划不周",
        "魔术师",
    ],
    ["潜意识、洞察力、知性、研究精神", "自我封闭、内向、神经质、缺乏理性", "女祭司"],
    [
        "母性、女性特质、生命力、接纳",
        "生育问题、不安全感、敏感、困扰于细枝末节",
        "皇后",
    ],
    ["控制、意志、领导力、权力、影响力", "混乱、固执、暴政、管理不善、不务实", "皇帝"],
    ["值得信赖的、顺从、遵守规则", "失去信赖、固步自封、质疑权威、恶意的规劝", "教皇"],
    [
        "爱、肉体的连接、新的关系、美好时光、互相支持",
        "纵欲过度、不忠、违背诺言、情感的抉择",
        "恋人",
    ],
    [
        "高效率、把握先机、坚韧、决心、力量、克服障碍",
        "失控、挫折、诉诸暴力、 冲动",
        "战车",
    ],
    ["勇气、决断、克服阻碍、胆识过人", "恐惧、精力不足、自我怀疑、懦弱", "力量"],
    ["内省、审视自我、探索内心、平", "孤独、孤立、过分慎重、逃避", "隐士"],
    [
        "把握时机、新的机会、幸运降临、即将迎来改变",
        "厄运、时机未到、计划泡汤",
        "命运之轮",
    ],
    ["公平、正直、诚实、正义、表里如一", "失衡、偏见、不诚实、表里不一", "正义"],
    [
        "进退两难、接受考验、因祸得福、舍弃行动追求顿悟",
        "无畏的牺牲、利己主义、内心抗拒、缺乏远见",
        "倒吊者",
    ],
    ["失去、舍弃、离别、死亡、新生事物的来临", "起死回生、回心转意、逃避现实", "死亡"],
    ["平衡、和谐、治愈、节制", "失衡、失谐、沉溺愉悦、过度放纵", "节制"],
    [
        "负面影响、贪婪的欲望、物质主义、固执己见",
        "逃离束缚、拒绝诱惑、治愈病痛、直面现实",
        "恶魔",
    ],
    [
        "急剧的转变、突然的动荡、毁灭后的重生、政权更迭",
        "悬崖勒马、害怕转变、发生内讧、风暴前的寂静",
        "塔",
    ],
    ["希望、前途光明、曙光出现", "好高骛远、异想天开、事与愿违、失去目标", "星星"],
    ["虚幻、不安与动摇、迷惘、欺骗", "状况逐渐好转、疑虑渐消、排解恐惧", "月亮"],
    ["活力充沛、生机、远景明朗、积极", "意志消沉、情绪低落、无助、消极", "太阳"],
    [
        "命运好转、复活的喜悦、恢复健康",
        "一蹶不振、尚未开始便已结束、自我怀疑、不予理睬",
        "审判",
    ],
    [
        "愿望达成、获得成功、到达目的地",
        "无法投入、不安现状、半途而废、盲目接受",
        "世界",
    ],
]

divine=on_fullmatch(("占卜"),rule=to_me())

@divine.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    spread_name,spread_list=choice(spread)#牌阵名，牌阵卡牌描述
    await divine.send(f"【典开】{spread_name}")#回应
    nodes=[]
    spread_list_card=sample(range(0,22),len(spread_list))#抽n张不重复的塔罗牌的序号
    for i in range(len(spread_list)):
        phase = randint(0, 1)
        nodes.append(MessageSegment.node_custom(user_id=bot.self_id,nickname="休比·多拉",content=MessageSegment.text(f"{spread_list[i]}\n『{arcana[spread_list_card[i]][-1]}{'正位' if phase == 0 else '逆位'}』，{arcana[spread_list_card[i]][phase]}")+MessageSegment.image(file=ARCANA_DIR / f"{spread_list_card[i]}.png")))
    try:
        await bot.send_group_forward_msg(group_id=event.group_id, messages=nodes)
    except:
        await divine.send("发生未知错误")

