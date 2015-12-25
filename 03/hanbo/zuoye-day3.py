#!/usr/bin/env python
#coding:utf-8
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''


count_dict = {}
for ch in read_me:
  count_dict.setdefault(ch,0)
  count_dict[ch] = count_dict[ch] + 1
#字典转化为列表
count_list = count_dict.items()
#冒泡,取top 10

count = len(count_list) - 1
if count > 10:
  count = 10

for y in range(count):
  for x in range(len(count_list) - 1 - y):
    if count_list[x][1] < count_list[x+1][1]:
      count_list[x],count_list[x+1] = count_list[x+1],count_list[x]
#print count_list
print "top_10 is bellow:"
for i in count_list[:10]:
  print   "%s:%s" %i 

