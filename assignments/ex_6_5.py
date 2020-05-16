# text = "X-DSPAM-Confidence:    0.8475";
# ss=text.find('0')
# s1=text.find('5',ss)
# print(text[ss:s1+1])

text = "X-DSPAM-Confidence:    0.8475";
ss=text.find('0')
s1=text.find('5',ss)
s2=text[ss:s1+1]
print(float(s2))

