import sys

# Divides the input array w.r.t the pivot and returns the partition index and comparison count
def partition(a, start, end):
    count = 0
    pivot = median(a[start], a[start+1], a[end])    # Calculate median of first,second and last index values
    pivotindex = a.index(pivot)
    pivot = a[pivotindex]
    pindex = start
    a[pivotindex], a[end] = a[end], a[pivotindex]

    for i in range(start, end):
        count += 1
        if a[i] <= pivot:
            a[i], a[pindex] = a[pindex], a[i]
            pindex += 1

    a[pindex], a[end] = a[end], a[pindex]
    return pindex,count

# Partition the array and do quickSort on sub-arrays
def quickSort(a, start, end):
    count = 0
    if start < end:
        pindex,count = partition(a, start, end)
        count += quickSort(a, start, (pindex - 1))
        count += quickSort(a, (pindex + 1), end)
    return count

# Pass file name as argument, read the contents of the file and store it in a array
def inputFile():  
    a = []
    file = sys.argv[1]
    input = open (file,"r")
    for line in input.readlines():
        for i in line.split():
            a.append(int(i))
    input.close()
    return a

# Calculate median of 3 numbers
def median(a,b,c):
    if a > b:
        if a < c:
            med = a
        elif b > c:
            med = b
        else:
            med = c
    else:
        if a > c:
            med = a
        elif b < c:
            med = b
        else:
            med = c
    return med


#=======================================================================================================================
# main
#=======================================================================================================================
if __name__ == "__main__":
    if len(sys.argv) == 2:
        a = inputFile()
        count = quickSort(a,0,len(a)-1)
        print("Comparison count value = ", count)
        # Print the sorted array in an output file
        outfile = open("quickSort_sorted.txt", "w")
        outfile.write("\n".join(str(i)for i in a))
        outfile.close()
        print("quickSort_sorted.txt is saved in your current working directory!")

    else:
        print("Oops! Something missing\nCorrect Usage is ./quickSort.py <filename> where <fileName> is the file to be sorted")
