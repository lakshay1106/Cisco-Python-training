import re
s = 'data1:data2,data3-data4(data5)data6'
print(re.findall('[^a-zA-Z0-9]',s))  #matching all the specialchars
print(re.sub('[^a-zA-Z0-9]','|',s))  #replace all the specialchars ->|
print(re.split('[^a-zA-Z0-9]',s))#split->multiple values Vs s.split(SingleChar)
