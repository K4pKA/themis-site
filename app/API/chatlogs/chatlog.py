# -*- coding: utf-8 -*-
import os.path
import datetime


class Chatlog:

    def __init__(self, date):
        self.file = f"app/API/chatlogs/{date}.txt"
        self.ll_file = "app/API/chatlogs/ll.txt"

    def check_chatlog(self):
        if not os.path.exists(self.file):
            with open(self.file, "a") as f:
                timestamp = datetime.datetime.now().strftime("%H-%M-%S")
                f.write(u"{19ff19}[" + timestamp + "] Start of chatlog\n")

    def add_line(self, content):
        self.check_chatlog()
        f = open(self.file, "a")
        cont = "{0}\n".format(content)
        f.write(cont)
        p = open(self.ll_file, "w")
        p.write(content)
        return cont

    def add_line_nickname(self, nickname, content):
        self.check_chatlog()
        f = open(self.file, "a")
        cont = "{0}: {1}\n".format(nickname, content)
        f.write(cont)
        p = open(self.ll_file, "w")
        p.write(content)
        return content

    def get_last_line(self):
        self.check_chatlog()
        f_read = open(self.file, "r")
        last_line = f_read.readlines()[-1]
        return last_line

    def get_number_last_line(self):
        num_lines = sum(1 for line in open(self.file))
        return num_lines

    def text_to_html(self, content):
        symbols_ru_upper = {"А": "&#1040;", "Б": "&#1041;", "В": "&#1042;", "Г": "&#1043;", "Д": "&#1044;",
                            "Е": "&#1045;", "Ё": "&#1025;", "Ж": "&#1046;", "З": "&#1047;", "И": "&#1048;",
                            "Й": "&#1049;", "К": "&#1050;", "Л": "&#1051;", "М": "&#1052;", "Н": "&#1053;",
                            "О": "&#1054;", "П": "&#1055;", "Р": "&#1056;", "С": "&#1057;", "Т": "&#1058;",
                            "У": "&#1059;", "Ф": "&#1060;", "Х": "&#1061;", "Ц": "&#1062;", "Ч": "&#1063;",
                            "Ш": "&#1064;", "Щ": "&#1065;", "Ъ": "&#1066;", "Ы": "&#1067;", "Ь": "&#1068;",
                            "Э": "&#1069;", "Ю": "&#1070;", "Я": "&#1071;"}
        symbols_ru_lower = {"а": "&#1072;", "б": "&#1073;", "в": "&#1074;", "г": "&#1075;", "д": "&#1076;",
                            "е": "&#1077;", "ё": "&#1105;", "ж": "&#1078;", "з": "&#1079;", "и": "&#1080;",
                            "й": "&#1081;", "к": "&#1082;", "л": "&#1083;", "м": "&#1084;", "н": "&#1085;",
                            "о": "&#1086;", "п": "&#1087;", "р": "&#1088;", "с": "&#1089;", "т": "&#1090;",
                            "у": "&#1091;", "ф": "&#1092;", "х": "&#1093;", "ц": "&#1094;", "ч": "&#1095;",
                            "ш": "&#1096;", "щ": "&#1097;", "ъ": "&#1098;", "ы": "&#1099;", "ь": "&#1100;",
                            "э": "&#1101;", "ю": "&#1102;", "я": "&#1103;"}
        sst = ""
        for i in content:
            if i in symbols_ru_lower:
                sst += symbols_ru_lower[i]
            elif i in symbols_ru_upper:
                sst += symbols_ru_upper[i]
            else:
                sst += i
        return sst