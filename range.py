def myrange(start, stop=None, step=1):
	if stop is None:
		stop = start
		start = 0;
	while start < stop:
		yield start
		start += step

print ([ x for x in myrange(9)])
