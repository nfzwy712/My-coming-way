import re
#  ^表示匹配必须以我后面的内容开始，
#  $表示匹配必须以我前面的内容结束，所以'^'写在字符左边，'$'写在字符右边
#   当你想提取中间的内容时（即不包括开头与结束标志时）使用"零宽断言"
#   前向断言：'(?<=...)' 表示前面必须是...
#   后向断言： '(?=...)' 表示后面必须是...

text=('jajsdjakjdgklajkldfjgklajgklhelloajksdhfjkahsdjkend'
      'hellojkasdbfjkhaend')
result=re.findall(r'hello\w+end$',text)
print(result)
print('-'*30)
#注意此时会匹配最外端的hello和end中内容，即贪婪匹配。将\w+后加上一个？即可改为非贪婪匹配
result=re.findall(r'(?<=hello)\w+(?=end)',text)
print(result)
print('-'*30)
#  当?出现在*，+，？，{n，m} 后面时会将默认的贪婪模式修改为非贪婪模式
#    贪婪模式：尽可能多的匹配满足条件的内容
#    非贪婪模式：尽可能少的匹配满足条件的内容，即只要能满足内容就停止
result=re.findall(r'(?<=hello)\w+?(?=end)',text)
print(result)
print('-'*30)
#  \b表示单词边界，\B表示非单词边界。注意：单词边界是指单词字符和非单词字符之间的缝隙。
#  数字，字母,下划线属于单词字符
#  空格和换行以及Tab属于非单词字符
text1='cat 123 category is so123 big'
result=re.findall(r'\b123\b',text1)
print(result)
#注意这里的单词并非自然语言中的单词
text2="sjkdhfjkshdjk 123 uiashfui456sjkdhvvjkh "
result=re.findall(r'\b\d+\b',text2)
print(result)

