

def partition(arr,low,high):
    pivot = low
    start = low+1
    end = high
    
        
    while True:          
        while start <=end and arr[start] <= arr[pivot]:
            start+=1
        while start <=end and arr[end] > arr[pivot]:                
            end-=1

        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
        else:
            break
        print(f"{start}, {end} swapped")

    arr[end],arr[pivot] = arr[pivot],arr[end]

    print(f"{pivot}, {end} swapped")
    return end

def quickSort(arr,start,end):

    if end ==start:
        return
    


    if start<end:
        p = partition(arr,start,end)
       
   
       
        print(p,"P value")
        quickSort(arr,start,end = p-1)




        print(p,"P value")

        quickSort(arr,start = p+1,end = end)

       


a = [7,6,10,5,9,2,1,15,7 ]
b=quickSort(a,0,len(a)-1)
print(a)
print(b)