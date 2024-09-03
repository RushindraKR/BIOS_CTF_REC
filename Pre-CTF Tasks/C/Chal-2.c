#include<stdio.h>
void sortArray(int arr[], int n) 
{
    for(int i = 0; i < n-1; i++) 
    {
        for(int j = 0; j < n-i-1; j++) 
        {
            if(arr[j] > arr[j+1]) 
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int findSecondHighest(int arr[], int n) 
{
    sortArray(arr, n);
    for(int i = n-2; i >= 0; i--) {
        if(arr[i] != arr[n-1]) {
            return arr[i];
        }
    }
    return -1;
}

int main() 
{
    int arr[] = {12, 35, 1, 10, 34, 1};
    int n = sizeof(arr)/sizeof(arr[0]);

    int second_highest = findSecondHighest(arr, n);

    if(second_highest != -1)
        printf("The second highest element is %d\n", second_highest);
    else
        printf("There is no second highest element\n");

    return 0;
}
