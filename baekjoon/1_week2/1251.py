word = input()
word_lst = []

for i in range(len(word)-1):
  for j in range(i+2,len(word)):
    w1 = word[:i+1]
    w2 = word[i+1:j]
    w3 = word[j:]
    new_word = w1[::-1] + w2[::-1] + w3[::-1]
    word_lst.append(new_word)
word_lst.sort()

print(word_lst[0])