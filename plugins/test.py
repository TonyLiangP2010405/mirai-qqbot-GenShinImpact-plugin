import miraicle


@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if msg.text == "test":
        bot.send_group_msg(group=msg.group, msg='测试成功')

