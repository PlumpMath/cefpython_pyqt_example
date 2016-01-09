def multiply(a, b, callback):
	c = a * b
	print 'Multiply result:', c
	callback.Call(c)