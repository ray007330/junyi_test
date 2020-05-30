text = 'junyiacademy'

def reverse(s):
	result = ''.join([ s[i] for i in range(len(s)-1, -1, -1) ])
	return result

print(reverse(text))