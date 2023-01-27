import re
#s = 'fenkfnaeasdf=5;iwantthis123jasdefnlnaelifnk'
#s = s+s+s
#start = 'asdf=5;'
#end = '123jasd'
#
#result = re.search('%s(.*)%s' % (start, end), s).group(1)
#print(result)
#
#



text_1 = 'I want to find a string_1 between two substrings'
text_2 = 'I want to find a string_2 between two substrings'
s = text_1 + text_2
start = 'find a '
end = 'between two'

# Output: 'string'
#print(text[text.index(left)+len(left):text.index(right)])


print(re.search(re.escape(start)+"(.*)"+re.escape(end),s).group(1))






https://www.google.com/search?client\x3dfirefox-b-e\x26amp;ie\x3dUTF-8\x26amp;ei\x3dzanQY9rBLbyNhbIPl9aM-Ac\x26amp;q\x3dWhat\x27s+the+meaning+behind+Hello?\x26amp;sa\x3dX\x26amp;ved\x3d2ahUKEwia3P6X6-H8AhW8RkEAHRcrA38Qzmd6BAgBEAc\x22\x3e
