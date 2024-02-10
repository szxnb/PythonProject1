# import requests

# url = "https://openai.api2d.net/v1/chat/completions"

# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Bearer fk200296-sBkBMgHYav8q4mpxIEm0Yw98mh2ETuxf' # <-- 把 fkxxxxx 替换成你自己的 Forward Key，注意前面的 Bearer 要保留，并且和 Key 中间有一个空格。
# }

# data = {
#   "model": "gpt-3.5-turbo",
#   "messages": [
#     {"role": "system", "content": "你是一个塔罗占卜师，精通塔罗牌的占卜技能。在第一次提问的时候，你会先让我把自己想要占卜的问题发给你，然后你会让我从1-78张牌中任意抽取3张牌，然后根据我抽的牌，你会进行占卜"},
#     {"role": "user", "content": "你好，请问怎么占卜?"}
#   ]
# }

# response = requests.post(url, headers=headers, json=data)

# print("Status Code", response.status_code)
# print("JSON Response ", response.json())


from openai import OpenAI
client = OpenAI(api_key="sk-2YUDwEQLxbb8QptiCc243537CeD94dF4Aa6c2a5c3e8e17E9",                        
                base_url="https://api.aigc369.com/v1")

completion = client.chat.completions.create(
  model='gpt-3.5-turbo-0125',
  messages=[
    {"role": "system", "content": "你是一个塔罗占卜师，精通塔罗牌的占卜技能。在第一次提问的时候，你会先让我把自己想要占卜的问题发给你，然后你会让我从1-78张牌中任意抽取3张牌，然后根据我抽的牌，你会进行占卜"},
    {"role": "user", "content": "你好，请问怎么占卜?"}
  ]
)

print(completion.choices[0].message)