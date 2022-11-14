import json
import re
from pathlib import Path
import miraicle

import requests

p = Path('character.json')


def get_character_information():
    character_dict = {}
    genshin_url = "https://sg-wiki-api.hoyolab.com/hoyowiki/wapi/get_entry_page_list"
    sess = requests.Session()
    payload = {
        "filters": [],
        "menu_id": "2",
        "page_num": 1,
        "page_size": 100,
        "use_es": True,

    }

    header = {
        "authority": "sg-wiki-api.hoyolab.com",
        "method": "POST",
        "path": "/hoyowiki/wapi/get_entry_page_list",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "origin": "https://wiki.hoyolab.com",
        "referer": "https://wiki.hoyolab.com/",
        "x-rpc-language": "zh-cn",
    }

    response = sess.post(genshin_url, json=payload, headers=header)
    data = response.text
    json_object = json.loads(data)
    for character_information in json_object['data']['list']:
        x = character_information['name']
        y = character_information['entry_page_id']
        character_dict[x] = y
    p.write_text(str(character_dict).replace("'", '"'), encoding='utf8')


def get_character_detail(character_id):
    base_character_url = "https://sg-wiki-api-static.hoyolab.com/hoyowiki/wapi/entry_page?entry_page_id="
    character_url = base_character_url + character_id
    sess = requests.Session()
    header = {
        "authority": "sg-wiki-api.hoyolab.com",
        "method": "GET",
        "path": "/hoyowiki/wapi/entry_page?entry_page=" + character_id,
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "origin": "https://wiki.hoyolab.com",
        "referer": "https://wiki.hoyolab.com/",
        "x-rpc-language": "zh-cn",
    }
    response = sess.get(character_url, headers=header)
    data = response.text
    Path(character_id).write_text(data, encoding='utf8')


def solve_character_content_mingzhizuo(character_id):
    character_information_list = []
    character_detail = Path(character_id).read_text(encoding='utf8')
    character_detail_json = json.loads(character_detail)
    character_information_list.append(character_detail_json['data']['page']['modules'][4]['name'])
    character_modules_json = json.loads(character_detail_json['data']['page']['modules'][4]['components'][0]['data'])
    for character_modules_object in character_modules_json['list']:
        character_information_list.append(character_modules_object['name'])
        character_information_list.append(character_modules_object['desc'])
    return character_information_list


@miraicle.Mirai.receiver('GroupMessage')
def genshin_character_basic_information(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if Path('character.json').exists():
        character_all = Path('character.json').read_text(encoding='utf8')
        character_json = json.loads(character_all)
        if msg.text[:4] == "命座信息":
            input_message = msg.text[4:]
            if input_message in character_json:
                reduce_html_process = re.compile(r'<[^>]+>', re.S)
                if not Path(character_json[input_message]).exists():
                    get_character_detail(character_json[input_message])
                message4 = solve_character_content_mingzhizuo(character_json[input_message])
                for i in range(len(message4)):
                    send_message4_str_reduceHtml = reduce_html_process.sub('', message4[i])
                    bot.send_group_msg(group=msg.group, msg=send_message4_str_reduceHtml)
    else:
        get_character_information()
        bot.send_group_msg(group=msg.group, msg=miraicle.Plain('正在爬取信息，请重新输入一次'))
