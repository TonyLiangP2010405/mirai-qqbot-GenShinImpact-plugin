import miraicle


my_qq = 1287663323           # 你的 QQ 号


@miraicle.Mirai.filter('GroupSwitchFilter')
def group_switch(bot: miraicle.Mirai, msg: miraicle.GroupMessage, flt: miraicle.GroupSwitchFilter):
    if msg.sender == my_qq:
        if msg.plain == '启用所有组件':
            flt.enable_all(group=msg.group)
            bot.send_group_msg(group=msg.group, msg='已在群内启用所有组件', quote=msg.id)
        elif msg.plain == '禁用所有组件':
            flt.disable_all(group=msg.group)
            bot.send_group_msg(group=msg.group, msg='已在群内禁用所有组件', quote=msg.id)