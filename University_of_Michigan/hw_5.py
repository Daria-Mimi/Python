text = "X-DSPAM-Confidence:    0.8475"
res = text.find('0.8475')
res2 = text[res:]
print(float(res2))



