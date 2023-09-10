def swap(a,b):
    a,b = b,a

def partition(arr:list, start, end):
    pivot = start
    
    

    while True:
        print("inside while block")
        print(start,end)
        # break
        
        while arr[start] <= arr[pivot]:
            start = start +1
            print(start)
            print("start increased")
        
        while arr[end] > arr[pivot]:
            end = end-1
            print("end decreased")
        print("swapper start and end")
        swap(arr[start], arr[end])
        if start > end:
            print("if block runnin in partition")
            swap(arr[end],arr[pivot])
            break

    return end

def quickSort(arr:list, start, end):

    if start< end:
        p = partition(arr, start, end)
        print("left element sort")
        quickSort(arr, start, p-1)
        print("right elemet sort")
        quickSort(arr,p+1, end )

a = [7,6,10,5,9,2,1,15,7]

quickSort(a,0,len(a)-1)
print(a)
               