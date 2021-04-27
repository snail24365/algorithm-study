import heapq


def solution(lst):
    left_heap = []
    right_heap = []
    for item in lst:
        median = insert(item, left_heap, right_heap)
        print(median)


def insert(value, left_heap, right_heap):
    left_max = (-1) * left_heap[0] if left_heap else None

    if not left_max or value < left_max:
        heapq.heappush(left_heap, -value)
    else:
        heapq.heappush(right_heap, value)

    if len(left_heap) < len(right_heap):
        heapq.heappush(left_heap, (-1) * heapq.heappop(right_heap))
    if len(left_heap) - 1 > len(right_heap):
        heapq.heappush(right_heap, (-1) * heapq.heappop(left_heap))
    return (-1) * left_heap[0]

#solution([1,2,3,4,5,6,7,8])
print("============================")
solution([3, 1, 20, 40, 5, 8, 33, 100, 300, 400])