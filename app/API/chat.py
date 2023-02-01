from flask import url_for
from flask import request
from flask import jsonify
from api import bp
from api.errors import bad_request


@bp.route('/get_chat/<int:id>', methods=['GET'])
def get_chat(id):
    return jsonify({"message_id": id,"status_code": 201})


send_chat_ex = {
    "nickname": "Alexsandr_Degtyarev",
    "content": "Привет, мир!",
    "timestamp": "11:06:30"
}


@bp.route('/send_chat', methods=['POST'])
def send_chat():
    data = request.get_json() or {}
    print(data)

    if "nickname" not in data or "content" not in data:
        return bad_request("Incorrect data")
    if len(data["content"]) > 70:
        return bad_request("Message limit exceeded")

    response = {
        "message_id": 0,
        "data": {
            "content": data["content"],
            "nickname": data["nickname"],
            "timestamp": data["timestamp"]
        },
        "status_code": 201
    }
    return jsonify(response)