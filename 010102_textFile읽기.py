

with open('data/text1.txt', 'r', encoding='utf-8') as f:
    text1=f.read()

f=open('data/text2.txt', 'r', encoding='utf-8')
text2=f.read()

with open('data/text1.txt', 'r', encoding='utf-8') as f:
   lines = f.readlines()

print("="*100)
print( text1)
print("-"*100)
print( text2)
print("-"*100)
print( lines)
print("="*100)

