import os
import uuid
import json

from flask import jsonify
from flask import request

from app.API import bp
from app.API.errors import bad_request


a = {
    "HWID": 3664730806,
    "DHWID": "DA6F5AB6",
    "Key": "",
    "pwd": "393817c2-4bce-4ec5-9220-f03d289bc536"
}


@bp.route('/get_pwd', methods=['GET'])
def get_pwd():
    return jsonify({"pwd": uuid.uuid4(), "status_code": 201})


@bp.route('/check_license', methods=['POST'])
def check_license():

    data = request.get_json()
    HWID = data["HWID"]
    DHWID = data["DHWID"]
    LicenseKey = data["key"]
    file = "app/API/lc_keys/" + LicenseKey + ".json"

    if not os.path.exists(file):
        return bad_request("non-existent license key")
    else:
        with open(file, "r") as f:
            d = json.load(f)
        if d["HWID"] == HWID and d["DHWID"] == DHWID:
            return jsonify({"message": "License correct", "status_code": 201})
        else:
            bad_request("License incorrect")


@bp.route('/activate_script', methods=['POST'])
def activate_license():
    data = request.get_json() or {}
    try:
        HWID = data["HWID"]
        DHWID = data["DHWID"]
        LicenseKey = data["key"]
        file = "app/API/lc_keys/" + LicenseKey + ".json"
        if not os.path.exists(file):
            return bad_request("non-existent license key")
        else:
            with open(file, "r") as f:
                d = json.load(f)
                if d["HWID"] != "":
                    bad_request("Bad key")
            if (d["HWID"] == "") and (d["DHWID"] == ""):

                with open(file, "w") as f:

                    d["HWID"] = HWID
                    d["DHWID"] = DHWID

                    json.dump(d, f)
                return {"message": "License activate for " + HWID, "status_code": 201}
            else:
                bad_request("Wrong key")
    except Exception:
        bad_request("Data incorrect")


@bp.route('/get_sounds', methods=['GET'])
def get_sounds():
    filename = str(uuid.uuid4())
    return jsonify({"urlfile": "https://download.mu-manager.space/static/" + filename + ".zip", "filename": filename + ".zip", "status_code": 201})