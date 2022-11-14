import miraicle


@miraicle.Mirai.receiver('GroupMessage')
def genshin_character_all(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    send_message = ["请输入以下命令选择你要输出的东西", "命令:", "角色名(例如:提纳里)(输出全部信息)", "基础信息+角色名(例如:基础信息提纳里)", "命座信息+角色名(例如:命座信息提纳里)",
                    "故事信息+角色名(例如:故事信息提纳里)", "天赋信息+角色名(例如:天赋信息提纳里)", "语音信息+角色名(例如:语音信息提纳里)"]
    send_message_str = "".join(str(i + "\n") for i in send_message)
    if msg.plain == "原神助手":
        bot.send_group_msg(group=msg.group, msg=miraicle.Plain(send_message_str))
