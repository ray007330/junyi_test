input_num = input('Enter a number:')
print('Input:',input_num)

input_num = int(input_num)

def solve(num):
	result = []
	for i in range(1, num+1):
		if i % 15 == 0:
			result.append(i)
		else:
			if i%3 != 0 and i%5 != 0: 
				result.append(i)
	#print(result)
	return len(result)

print(solve(input_num))