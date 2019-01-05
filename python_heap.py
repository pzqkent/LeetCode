import heapq
heap = []
data = [1,3,5,7,9,2,4,6,8,0]
for i in data:
	heapq.heappush(heap,i)
print(heap)

lis = []
while heap:
	lis.append(heapq.heappop(heap))
print(lis)


data2 = [1,5,3,2,9,5]
heapq.heapify(data2)
print(data2)

lis2 = []
while data2:
	lis2.append(heapq.heappop(data2))
print(lis2)