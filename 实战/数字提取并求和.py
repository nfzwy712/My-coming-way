import re
text="23shuh273jbwq73h273suuhb37hw2398h0b238hw92ush38ns923iikhsdbf"
request=re.findall(r'\d+',text)
total=sum(map(int,request))
print(request)
print(total)