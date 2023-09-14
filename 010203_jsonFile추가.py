import json
# 기존 JSON 파일 읽기
with open('data/message.json', 'r', encoding='utf-8') as f:
    message = json.load(f)

# 새로운 메시지 추가
message.append({"role": "user", "content": "어느 학교 다녀"})
message.append({"role": "assistant", "content": "제주과학고 1학년이야"})

# 수정된 메시지를 다시 JSON 파일로 저장
with open('data/message.json', 'w', encoding='utf-8') as f:
    json.dump(message, f, ensure_ascii=False, indent=4)