col, row = map(int, input('please insert col, row.\n').split()) # column, row input
print('please insert mine location.')
matrix = []
for i in range(row):
    matrix.append(list(input())) # matrix input

print('Mine Map')
count = 0
for i in range(row):
	for j in range(col):
		if matrix[i][j] != '*': # count the adjacent mine
			count = 0 
			if i == 0: # first row
				if j == 0: # first column
					if matrix[i][j+1] == '*':
						count += 1
					if matrix[i+1][j] == '*':
						count += 1
					if matrix[i+1][j+1] == '*':
						count += 1
				elif j == col-1: # last column
					if matrix[i][j-1] == '*':
						count += 1
					if matrix[i+1][j-1] == '*':
						count += 1
					if matrix[i+1][j] == '*':
						count += 1
				else: # middle column
					if matrix[i][j-1] == '*':
						count += 1
					if matrix[i+1][j-1] == '*':
						count += 1
					if matrix[i+1][j] == '*':
						count += 1
					if matrix[i+1][j+1] == '*':
						count += 1
					if matrix[i][j+1] == '*':
						count += 1
			elif i == row-1: # last row
				if j == 0: # first column
					if matrix[i][j+1] == '*':
						count += 1
					if matrix[i-1][j] == '*':
						count += 1
					if matrix[i-1][j+1] == '*':
						count += 1
				elif j == col-1: # last column
					if matrix[i][j-1] == '*':
						count += 1
					if matrix[i-1][j-1] == '*':
						count += 1
					if matrix[i-1][j] == '*':
						count += 1
				else: # middle column
					if matrix[i][j-1] == '*':
						count += 1
					if matrix[i-1][j-1] == '*':
						count += 1
					if matrix[i-1][j] == '*':
						count += 1
					if matrix[i-1][j+1] == '*':
						count += 1
					if matrix[i][j+1] == '*':
						count += 1
			else: # middle row
				if j == 0: # first column
					if matrix[i][j+1] == '*':
						count += 1
					if matrix[i+1][j] == '*':
						count += 1
					if matrix[i+1][j+1] == '*':
						count += 1
					if matrix[i-1][j] == '*':
						count += 1
					if matrix[i-1][j+1] == '*':
						count += 1
				elif j == col-1: # last column
					if matrix[i][j-1] == '*':
						count += 1
					if matrix[i-1][j-1] == '*':
						count += 1
					if matrix[i-1][j] == '*':
						count += 1
					if matrix[i+1][j-1] == '*':
						count += 1
					if matrix[i+1][j] == '*':
						count += 1
				else: # middle column
					if matrix[i][j-1] == '*':
						count += 1
					if matrix[i+1][j-1] == '*':
						count += 1
					if matrix[i+1][j] == '*':
						count += 1
					if matrix[i+1][j+1] == '*':
						count += 1
					if matrix[i-1][j-1] == '*':
						count += 1
					if matrix[i-1][j] == '*':
						count += 1
					if matrix[i-1][j+1] == '*':
						count += 1
					if matrix[i][j+1] == '*':
						count += 1
			matrix[i][j] = count
		else: # mine location
			pass

for i in range(row): # print matrix
	for j in range(col):
		print(matrix[i][j], end='')
	print()
