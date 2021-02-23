def binarysearch(arr, left, right, search):
    if right < left:
        raise Exception('Bounds error.')

    midelement = left + (right - left) // 2
    if arr[midelement] == search:
        return midelement

    elif arr[midelement] < search:
        return binarysearch(arr, midelement, len(arr) - 1, search )

    elif arr[midelement] > search:
        return binarysearch(arr, 0, midelement - 1, search)



if __name__ == "__main__":
    arr = [10,20,30,40,50,60,70,80,90,100]
    search = 30
    result = binarysearch(arr, 0,len(arr)-1, search)
    print(result)