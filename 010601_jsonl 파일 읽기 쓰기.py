import jsonlines
# JSONL 파일 쓰기
with jsonlines.open('output.jsonl', mode='w') as f:
    f.write({'name': '재돌이', 'age': 30})
    f.write({'name': '재순이', 'age': 25})

# JSONL 파일 추가
with jsonlines.open('output.jsonl', mode='a') as f:
    f.write({'name': '홍순이', 'age': 30})
    f.write({'name': '홍돌이', 'age': 30})
    
# JSONL 파일 읽기

with jsonlines.open('output.jsonl') as reader:
    
    for line in reader:
        print(line)

    print("-"*100)
    for line in reader:
        print(line["name"], line["age"])    
    print("="*100)

# reader 값을 가저와서 출력하기 
