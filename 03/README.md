# 第三次作业 
       
大家用自己的名字创建文件夹放自己的代码即可      
       
作业要求：

第二题统计字符数量之后，打印出现次数前10的字符

read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''

<!--
思路:

方法一: 考虑排序, 之前排序[]中的每个元素都是一个数字，如果[('a', 50), ('b', 30), ('c', 60)], 想根据每个元素的索引1排序，应该怎么排序?
方法二: 颠倒统计的key:value, 注意key不能重复，value可能重复, 颠倒后统计数字即为新字典的key, 取出所有key 进行排序，取出前N个字符(注意有的value可能包括多个字符，需要自己找前十个)
-->
注意：

有可能第十个数量最多的字符有多个，可以考虑是否从a->z的顺序取出前十个