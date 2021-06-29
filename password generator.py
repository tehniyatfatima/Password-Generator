
import random
print("\t","\t","Welcomoe to password Gnenerator")
n=input("enter your name")
s1="ABCDEFGHIJKLMNOPQRST"
s2="abcdefghijklmnopqrstuvwxyz"
s3="!<>#*"
s4="1234567890"
plen=int(input('enter the lenght of Password'))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
f=("".join(s[0:plen]))
print(n,'your password is ',f)

