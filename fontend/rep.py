# import re
#
# '''
#   第一题
# '''
# def emailIsIvalid(strs):
#   username=r'([a-z0-9][a-z0-9.\-_]+)'
#   servername=r'([a-z0-9][a-z0-9.\-_]*[a-z0-9]\.)*([a-z]{2,3}$)'
#   pattern=re.compile(username+'@'+servername,re.I)
#   isvalid=re.match(pattern,strs)
#   if isvalid:
#     print('Valid')
#   else:
#     print('Invalid')
# '''
#   第二题
# '''
# def fun2():
#   txt= '<p> class="item">You are very good!.<a href="www.baidu.com">Update you</a>or <a href="www.baidu.com">Update you</a>' \
#        'install Google chrome </p>'
#   ls=re.findall(r'>.+<?',txt)
#   print(ls)
#   for x  in ls:
#     print(x[1:-1],end=' ')
#
# def fun3(txt):
#   # help,asap,urgent
#   befor=re.match(r'([A-Z]+[^\w]*)*$|.*!{3,}',txt) #前两种情况
#   pattern=re.compile(r'(.*h+\W*e+\W*l+\W*p+\W*.*)|(.*a+\W*s+\W*a+\W*p+\W*.*)|(.*u+\W*r+\W*g+\W*e+\W*n+\W*t+\W*.*)',re.I)
#   after=re.match(pattern,txt)
#   if befor or after:
#     print('urgent')
#   else:
#     print('normal')
#
# if __name__=='__main__':
#   while True:
#     email=input('Enter an email:')
#     if email:
#       fun3(email)
#     else:
#       break
#
#
#
#
import re
import random
text='''Help, I need somebody.
Help, not just anybody.
Help, you know I need someone, help.

When I was younger so much younger than today,
I never needed anybody's help in any way.
But now these days are gone, I'm not so self assured.
Now I find I've changed my mind and opened up the doors.

Help me if you can, I'm feeling down.
And I do appreciate you being round.
Help me get my feet back on the ground.
Won't you please, please help me.

And now my life has changed in oh so many ways.
My independence seems to vanish in the haze.
But every now and then I feel so insecure.
I know that I just need you like I've never done before.

Help me if you can, I'm feeling down.
And I do appreciate you being round.
Help me get my feet back on the ground.
Won't you please, please help me.

When I was younger so much younger than today.
I never needed anybody's help in any way.
But now these days are gone, I'm not so self assured.
Now I find I've changed my mind and opened up the doors.

Help me if you can, I'm feeling down.
And I do appreciate you being round.
Help me, get my feet back on the ground.
Won't you please, please help me, help me, help me, ooh...'''
markov_dicts={'':[]}
sentence_sep='.?!'
kaitou=re.compile(r'[A-Z]\w*\b')
jiewei=re.compile(r'\b\w+[.?!]$')
kaitoulst=kaitou.findall(text)
print(kaitoulst)
markov_dicts['']=kaitoulst
wordlist = re.split(r'\s+', text)
for i in range(len(wordlist)-1):
    if jiewei.findall(wordlist[i]) ==[]:
        markov_dicts.setdefault(wordlist[i],[]).append(wordlist[i+1])
print(markov_dicts)
