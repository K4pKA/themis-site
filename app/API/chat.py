# -*- coding: utf-8 -*-
import datetime
import codecs
import chardet

from flask import jsonify
from flask import request

from app.API import bp
from app.API.chatlogs.chatlog import Chatlog
from app.API.errors import bad_request


@bp.route('/get_last_line', methods=['GET'])
def get_last_line():
    chat = Chatlog(datetime.datetime.now().strftime("%d-%m-%Y"))
    return jsonify({"message": chat.text_to_html(chat.get_last_line()),"status_code": 201})


@bp.route('/send_chat', methods=['POST'])
def send_chat():
    data = request.get_json() or {}
    if data["client"] == "ahk":
        content = str(data["content"].encode("iso-8859-1"), "cp1251")
    else:
        content = data["content"]

    if "content" not in data:
        return bad_request("Incorrect data")
    if len(content) > 70:
        return bad_request("Message limit exceeded")

    chat = Chatlog(datetime.datetime.now().strftime("%d-%m-%Y"))

    r = ""
    response = {}
    if data["nickname"]:
        nickname = data["nickname"]
        r = chat.add_line_nickname(nickname, content)
    else:
        r = chat.add_line(content)
    nickname = data["nickname"]
    response = {
        "message": chat.text_to_html(r),
        "status_code": 201
    }
    return jsonify(response)