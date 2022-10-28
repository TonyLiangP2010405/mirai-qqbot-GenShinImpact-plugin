import miraicle
from plugins import *

qq = 703382890  # 你登录的机器人 QQ 号
verify_key = '1234567890'  # 你在 setting.yml 中设置的 verifyKey
port = 8080  # 你在 setting.yml 中设置的 port (http)
bot = miraicle.Mirai(qq=qq, verify_key=verify_key, port=port)
bot.set_filter(miraicle.GroupSwitchFilter(r'config\group_switch.json'))
bot.run()
