text = 'flipped class room is important'

def reverse(s):
	result = ''.join([ s[i] for i in range(len(s)-1, -1, -1) ])
	return result

def reverse_word(s):
	words = s.split(' ')
	result = []
	for word in words:
		result.append(reverse(word))
	result = ' '.join(result)
	return result

print(reverse_word(text))