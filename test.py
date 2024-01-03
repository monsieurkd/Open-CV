
def duplicateZeros( arr) :
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_position = []

        for i in range(len(arr)):
            print(i)
            if arr[i] == 0:
                  zero_position.append(i)
        c = 0
           
        for z in zero_position:
            arr.insert(z+c, 0)
            arr.pop(-1)
            c+=1
        print(zero_position)

            
                
                
                
                
        return arr
arr = [1,2,0,3,0,4,8,5]
print(duplicateZeros(arr))
