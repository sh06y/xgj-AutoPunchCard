import requests
import json
from requests.packages import urllib3

# /applet/notify/feedbackWithOss
def feedback(openId, feedback_text, tid, member_id, select_date):
    url = "https://a.welife001.com/applet/notify/feedbackWithOss"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "imprint": openId,
        "Host": "a.welife001.com",
        "content-type": "application/json",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br"
    }

    postData = json.dumps({
        "feedback_text": feedback_text,
        "id": tid,
        "daka_day": select_date,
        "files": [],
        "submit_type": "submit",
        "networkType": "wifi",
        "member_id": member_id,
        "examdetail": "",
        "op": "add",
        "sub_info": []
    })
    urllib3.disable_warnings()
    reponse = requests.post(url, headers=headers, data=postData, timeout=4, verify=False)

    reponse = json.loads(reponse.text)

    # print(reponse)
    if reponse['code'] == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    pass