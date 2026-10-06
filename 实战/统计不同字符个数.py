def count_char_types(s):
    counts = {
        "大写字母": 0,
        "小写字母": 0,
        "数字": 0,
        "空格": 0,
        "其他字符": 0
    }
    for char in s:
        if char.isupper():
            counts["大写字母"] += 1
        elif char.islower():
            counts["小写字母"] += 1
        elif char.isdigit():
            counts["数字"] += 1
        elif char.isspace():
            counts["空格"] += 1
        else:
            counts["其他字符"] += 1
    return counts
x=input()
print(count_char_types(x))