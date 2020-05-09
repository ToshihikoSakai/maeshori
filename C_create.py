import codecs


with codecs.open("./all_maeshori.txt", "r", "utf-8") as f:
    text = f.read().splitlines()
        
for sen in text:
  temp = sen.split()
  print(temp[0],end='')
  print(' ',end='')
  for w in temp[1:]:
    print(w,end='')
    print(' ',end='')
    print(temp[0],end='')
    print(' ',end='')
  print()

      

  
