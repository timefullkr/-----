
text = "안녕하세요"
with open('data/text1.txt', 'w', encoding='utf-8') as f:
    f.write(text)

text = """
    안녕하세요
    반가워요
"""

with open('data/text2.txt', 'w', encoding='utf-8') as f:
    f.write(text)  

with open('data/text2.txt', 'a') as f:
    f.write('hello1')    
    f.write('hello2')    

text = """
    hello
"""

for char in text:
    print(ord(char))