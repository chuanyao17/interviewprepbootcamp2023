# https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder:

    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]

    def addNum(self, num: int) -> None:
        heappush(self.minHeap,num)
        heappush(self.maxHeap,heappop(self.minHeap)*-1)
        
        if len(self.maxHeap)-len(self.minHeap)>1:
            heappush(self.minHeap,heappop(self.maxHeap)*-1)
            
        

    def findMedian(self) -> float:
        if len(self.minHeap)==len(self.maxHeap):
            return float((-self.maxHeap[0]+self.minHeap[0])/2)
        return float(-self.maxHeap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()