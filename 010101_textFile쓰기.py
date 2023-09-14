
text="1.안녕하세요\n"
with open('data/text1.txt', 'w', encoding='utf-8') as f:
  f.write( "1.안녕하세요.\n" )
  f.write( "2.안녕하세요.\n" )


text ="""
1.안녕하세요
2.반가워요
"""

with open('data/text2.txt', 'w', encoding='utf-8') as f:
    f.write(text)  

print("완료!")