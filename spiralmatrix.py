def spiral_matrix(n:int,arr:list):
    arr=[[0]*n for _ in range(n)]
    top=0
    bottom=n-1
    left=0
    right=n-1
    num=1

    while num <=n*n:
        #Left to Right
        for i in range(left,right+1):
            arr[top][i]=num
            num+=1
        top+=1
        #Top to bottom
        for i in range(top,bottom+1):
            arr[i][right]=num
            num+=1
        right-=1
        #Right to left
        if top<=bottom:
            for i in range(right,left-1,-1):
                arr[bottom][i]=num
                num+=1
            bottom-=1
        # Bottom to top
        if left<=right:
            for i in range(bottom,top-1,-1):
                arr[i][left]=num
                num+=1
            left+=1
        
    print(arr)
spiral_matrix(3,arr=[])
