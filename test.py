
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
import re
def generate_hashtag(s):
    #your code here
    if len(s) >140 or len(s) == 0:
        return False
#     word_list = re.split(r'\s+', s) 
    word_list = s.split(' ')
    word_list = [a for a in word_list if a != '']
    print(word_list)
    word = '#'
    for i in range(len(word_list)):
        
        word_list[i] = word_list[i][0].upper() + word_list[i].lower()[1:]

        
        word = word + word_list[i]
        
    return word

print(generate_hashtag('CoDeWaRs is    niCe'))
print(len('ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq'))