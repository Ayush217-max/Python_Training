def rotate_right(list,n):
    print(list[-n:]+list[:len(list)-n])


rotate_right([1,2,3,4,5],2)