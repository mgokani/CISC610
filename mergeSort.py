import sys

count = 0
# The merge function merges two sub-arrays and returns the merged array
def merge(left, right):
    arr = []
    i = 0
    j = 0
    global count

    # Run the loop for size of the sub-arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # Pick the smaller element from the 2 sub-arrays
            arr.append(left[i])
            i = i + 1
        else:
            arr.append(right[j])
            count = count + len(left) - i
            j = j + 1


    # Pick all the remaining elements
    arr = arr + left[i:]
    arr = arr + right[j:]

    # Return the merged array
    return arr


# The mergeSort function takes an array as parameter and splits it into two sub-arrays
def mergeSort(array):
    if len(array) < 2:
        return array
    mid = int(len(array) / 2)

    # Recursive call to mergeSort function
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    # Call merge function
    return merge(left, right)

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

#=======================================================================================================================
# main
#=======================================================================================================================
if __name__ == "__main__":
    if len(sys.argv) == 2:
        a = inputFile()
        # Print the sorted array in an output file
        outfile = open("mergeSort_sorted.txt", "w")
        outfile.write("\n".join(str(i) for i in mergeSort(a)))
        outfile.close()
        print("Number of inversions = ", count)
        print ("mergeSort_sorted.txt is saved in your current working directory!")
    else:
        print("Oops! Something missing\nCorrect Usage is ./mergeSort.py <filename> where <fileName> is the file to be sorted")
