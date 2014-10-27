
N = raw_input()
try:
	N = int(N)
except ValueError:
	print "Invalid input, Quitting."

d = dict()
while (N>0):
	N-=1
	item = raw_input()
	if (item in d):
		d[item] += 1
	else:
		d[item] = 1

while True:
	K = raw_input()
	try:
		K = int(K)
		break
	except ValueError:
		print "Invalid input, Try again."

#print d
pairs = [(v, k) for (k, v) in d.iteritems()]

#print pairs

pairs_temp = sorted(pairs,key=lambda pair: pair[1])

#print pairs_temp

final_list = sorted(pairs_temp,key=lambda pair: pair[0], reverse = True)

#print final_list

i = 0
while (i < K):
	print final_list[i][1]
	i+=1
