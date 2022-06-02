import re
import math
result = []
with open("EventRecords.txt",'r') as f:
    content = f.readlines()

    if content:
        index_of_whitespace = [0]
        index_of_whitespace.extend([i for i in range(len(content)) if content[i]== '\n'])



        result = [content[index_of_whitespace[i]:index_of_whitespace[i+1]]
                  for i in range(len(index_of_whitespace)-1)]



        # B.extend(['X'] * (len(A)-len(B)))

        max_length = 0
        for j in result:
            max_length = max(max_length, len(j))

        for i in result:
           i += ['\n'] * (max_length - len(i))

        

    

        
        # print(index_of_whitespace)
        # print(result)
        print(result)
        for k in result:
            print (len(k))
        
    else:
        print("nothing to read")

#     print[data[x:x+10] for x in xrange(0, len(data), 10)]
# print[data[10*i:10*(i+1)] for i in range(len(data)/10 + 1)]
