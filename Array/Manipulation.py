a4,b4 = map(int, input().split())

arr=[0 for j in range(a4)]

for i in range(b4):
    a,b,k = map(int, input().split()) 
    for i in range(a-1,b):   
            arr[i]= arr[i]+k

def heapify(arr, n, i): 
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2      

    if l < n and arr[i] < arr[l]: 
        largest = l 

    if r < n and arr[largest] < arr[r]: 
        largest = r 

    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] 

        heapify(arr, n, largest) 

def heapSort(arr): 
    n = len(arr)  

    for i in range(n, -1, -1): 
        heapify(arr, n, i) 

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 

heapSort(arr) 
n = len(arr)  

print(arr[a4-1])
    
