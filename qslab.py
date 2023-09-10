def swap(arr,a,b):
    arr[a],arr[b] = arr[b],arr[a]

def partition(arr,start,end):
    if start==end:
        
        return 0
   
    else:
        pivot = start
        while True:
           
            if start >end:
                break          
            while start <=end and arr[start] <= arr[pivot]:
                start+=1
            while start <=end and arr[end] > arr[pivot]:                
                end-=1

            if start <= end:
                arr[start], arr[end] = arr[end], arr[start]
            else:
                break
            # print(f"{start}, {end} swapped")
        swap(arr,end,pivot)
        # print(f"{pivot}, {end} swapped")
    return end

def quickSort(arr,s,e):

    if e ==s:
        return
    


    if s<e:
        p = partition(arr,s,e)
       
   
       
        # print(p,"P value")
        quickSort(arr,s,e = p-1)




        # print(p,"P value")

        quickSort(arr,s = p+1,e = e)

       


a = [7,6,10,5,9,2,1,15,7 ]
b=quickSort(a,0,len(a)-1)
print(a)
print(b)