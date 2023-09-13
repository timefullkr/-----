
text = "안녕하세요"
with open('text_file1.txt', 'w', encoding='utf-8') as f:
    f.write(text)

text = """
    안녕하세요
    반가워요
"""
with open('text_file2.txt', 'w', encoding='utf-8') as f:
    f.write(text)    
    
