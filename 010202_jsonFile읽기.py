import json
with open('data/message.json', 'r', encoding='utf-8') as f:
   message=json.load(f)


print("="*100)
print( message)
print("-"*100)

for item in message:
   print( item["role"] +" >> " + item["content"] )

print("="*100)
# message.json 에 다음 내용을 추가 하여 저장 해보자 
# {"role": "user","content": "어느 학교 다녀"}
# {"role": "assistant","content": "제주과학고 1학년이야"}