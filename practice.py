size = int(input())

region = []
check_list = []
max_list = []
max_region = 0
regions = 0

for i in range(size):
	region.append([])
	check_list.append([])
	temp = list(map(int, input().split()))
	for j in range(size):
		check_list[i].append(False)
		region[i].append(temp[j])
# 입력완료 
# 알고리즘 시작

def ToRain(N,M, reg, chk):
	for i in range(M):
		for j in range(M):
			if reg[i][j] <= M:
				chk[i][j] = False
			else:
				chk[i][j] = True

for i in range(size):
	max_list.append(max(region[i]))
rain = max(max_list)

for i in range(rain):
	ToRain(i, size, region, check_list)
	regions = 0
	for j in range(size):
		for k in range(size):
			print(check_list[j][k], end="")
		print()

	for j in range(size):
		for k in range(size):
			if check_list[j][k] == False:
				continue
			if j != 0:
				if check_list[j-1][k] == True:
					continue
			if k != 0:
				if check_list[j][k-1] == True:
					continue
			if j != size-1:
				if check_list[j+1][k] == True:
					continue	
			if k != size-1:
				if check_list[j][k+1] == True:
					continue
			regions += 1			
	if max_region < regions:
		max_region = regions
	print("rain = %d, regions = %d" % (i, regions)) 

print(max_region)


# 확인용 출력
for i in range(size):
	for j in range(size):
		print(region[i][j], end="")
	print()

		
