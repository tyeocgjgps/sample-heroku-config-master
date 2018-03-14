import requests
from handler import handle_message

while True:
    res = requests.get("https://api.telegram.org/bot489180339:AAHrUoOiA2oL--wvEn7ba7r-WUvv0q1ER1M/getUpdates")
    d = res.json()
    print(d)
    for elem in d["result"]:
        text = elem["message"]["text"]
        print(text)
        ans = handle_message(text)

        chat_id = elem["message"]["chat"]["id"]

        requests.post("https://api.telegram.org/bot489180339:AAHrUoOiA2oL--wvEn7ba7r-WUvv0q1ER1M/sendMessage",
                      params={"chat_id": chat_id, "text": text})