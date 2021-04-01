#tiaoguo 7 he 7 de beishus
a = 10

for x in range(1,101):
	if x%7 == 0 or x%10 ==7 or int(x/10) == 7:
		continue
	else:
		print(x)
