#include<iostream>
using namespace std;

int partition(int arr[], int start, int end)
{
    int pivot = start;
    while(1==1)
    {        
        while(( start <= end )&&(arr[start] <= arr[pivot]))
        {
            start++;
        }

        while(( start <= end )&&arr[end] > arr[pivot])
        {
            end--;
        }
        if (start < end)
        {
            swap(arr[start], arr[end]);
        }
        else
        {
            break;
        }        
    }
    swap(arr[end],arr[pivot]);
    return end;
}

void quickSort(int arr[], int start, int end)
{
    if(start < end)
    {
        int p = partition( arr,  start,  end);
        quickSort(arr, start, p-1);
        quickSort(arr, p+1, end );
    }

}

int main()
{
    int a[] = {7,6,7,5,9,2,1,15,10} ;
    quickSort( a , 0, 8);
    for(int i =0; i < 9;i++)
    {
        cout << a[i] <<' ';
    }
    return 0;
}