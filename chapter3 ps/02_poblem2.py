letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>" , "Harry").replace("<|Date|>" , "17 august 2050"))