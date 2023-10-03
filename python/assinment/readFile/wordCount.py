search_words =  ["Python", "C", "OOP", "Hello", "Java"]
word_count = {}
x = open("input.txt","r")
lines = x.readlines()
x.close()
nlines = []

for word in search_words:
      word_count[word.lower()] = 0

for line in lines:
    nlines.append(line.replace('\n', '').lower())

for line in nlines:
      try:
            word_count[line] += 1
      except: pass
      
for key,val in word_count.items():
        print(key.capitalize(),"->",val)

