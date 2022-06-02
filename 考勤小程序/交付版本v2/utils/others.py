import pyttsx3
import json
try:
    from utils import setting_utils
except ModuleNotFoundError:
    import setting_utils

set = setting_utils.read_settings()


def voice_read():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # 设置语速
    engine.setProperty('volume', 2.0)  # 设置音量
    return engine


def all_situation():
    """考勤异常的所有情形"""
    return str_to_dict(set['kq_abnormal'])


def dict_to_str(dic):
    """
    将字典按照一定的格式转成字符串
    dict: {"1":"迟到", "2":"请假"}
    str: 1迟到，2请假
    """
    dic_str = json.dumps(dic, separators=('，', ''), ensure_ascii=False)
    return dic_str.replace('"', "").lstrip("{").rstrip("}")


def str_to_dict(s):
    """
    将一定格式的字符串转成字典
    str: '\n1、请假\n2、迟到\n3、早退\n4、旷课\n5、做核酸\n6、备赛\n7、参加学校活动/任务\n8、其他情况\n'
    dict: {'1': '请假', '2': '迟到', '3': '早退', '4': '旷课', '5': '做核酸', '6': '备赛', '7': '参加学校活动/任务', '8': '其他情况'}
    """
    sit_dict = {}
    for i in s.strip("\n").split('\n'):
        if not i.strip():
            continue
        j = i.split('、')
        sit_dict[j[0]] = j[1]
    return sit_dict


def key_info(s):
    """
    获取文件名的关键信息
    s: 2班学生名单.xlsx
    return: 2班
    """
    return s.replace(".xlsx", "") \
        .replace("名单", "") \
        .replace("学生", "") \
        .replace("昌", "") \
        .replace("平", "") \
        .replace("职", "") \
        .replace("北京", "")


if __name__ == '__main__':
    pass
