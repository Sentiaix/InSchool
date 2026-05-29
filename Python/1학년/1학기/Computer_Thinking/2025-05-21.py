# import random
# import time

#     # a는 인자, x는 찾을 수
# def Binary_Search3(a, x) :
# 	start = 0
# 	end = len(a) - 1

# 	while start <= end :
# 		mid = (start + end) // 2
# 		if x == a[mid] :
# 			return mid
# 		elif x > a[mid] :
# 			start = mid + 1
# 		else :
# 			end = mid - 1
# 	return -1

# b = random.sample(range(1, 1000001), 1000000)
# b.sort()

# start = time.time()
# print (Binary_Search3(b, 78))
# print ("time : ", time.time() -start)

################################################ next lect time
import random
import time

def bubble_sort(a) :
	for p in range(len(a)-1, 0, -1) :
		for i in range(p) :
			if a[i] > a[i + 1]:
				a[i], a[i + 1] = a[i + 1], a[i]
	return a

b = random.sample(range(1, 10001), 10000)

bubble_sort(b)

print(b)