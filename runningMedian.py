# Code to find the running median of numbers using heaps
# Author: Mirav Gokani

# Import heapq to call functions heappop, heappush and heappushpop
import heapq

class runningMedian:
    # Constructor to initialize min heap, max heap and heap size
    def __init__(self):
        self.minHeap, self.maxHeap = [], []
        self.N = 0

    # Function to insert the array numbers into either min heap or max heap
    def insert(self, num):
        if self.N % 2 == 0:
            heapq.heappush(self.maxHeap, -1 * num)
            self.N += 1
            if len(self.minHeap) == 0:
                return
            # Swap numbers if root of max heap greater than root of min heap
            if -1 * self.maxHeap[0] > self.minHeap[0]:
                min = -1 * heapq.heappop(self.maxHeap)
                max = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1 * max)
                heapq.heappush(self.minHeap, min)
        else:
            min = -1 * heapq.heappushpop(self.maxHeap, -1 * num)
            heapq.heappush(self.minHeap, min)
            self.N += 1

    # Function to calculate median using root values of min heap and max heap
    def getMedian(self):
        if self.N % 2 == 0:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return -1 * self.maxHeap[0]

def main():
    rm = runningMedian()
    a = [1,2,56,6,29]
    for i in range(0,len(a)):
        rm.insert(a[i])
    print("Median for original array of numbers = ", rm.getMedian())

    # User input numbers
    print ("Input your numbers")

    a = [int(x) for x in input().split()]
    for i in range(len(a), ):
        rm.insert(a[i])
    print("Median after adding numbers = ", rm.getMedian())


if __name__ == "__main__":
    main()