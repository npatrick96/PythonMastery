A = [2,1,2,3,4,5,6,7,8,9,10]
print(len(A))
def parking(arr):
    L = 0
    R = len(arr)-1 #right
    while L < R:
        mid  = (L+R)/2
        print (L, mid, R)
        if arr[mid-1] > arr[mid] < arr[mid+1]:
            return arr[mid]
        elif arr[mid-1] > arr[mid] > arr[mid+1]:
            L = mid   # move right
        elif arr[mid-1] < arr[mid] < arr[mid+1]:
            R = mid   # move left
print(parking(A))
    