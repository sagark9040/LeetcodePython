import sys
import heapq

class Solution:
    def kClosest(self, points, K):
        closest = []

        for x, y in points:
            dist = x*x + y*y

            if len(closest) < K:
                heapq.heappush(closest, (-dist, x, y))
            else:
                heapq.heappushpop(closest, (-dist, x, y))
        return [[b,c] for a, b, c in closest]


s = Solution()
for x, y in s.kClosest([[1,1],[2,2]], 1):
    print (x, y)


#	clever way to insert a distance, x, y co-ordinate in heap is to insert all three of them in the heap
#   I was trying to put x, ys in an somehow didn't corelate that with the distance which was the ACTUAL max heap parameter