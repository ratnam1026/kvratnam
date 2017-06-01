with open('ini5.txt', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0:
            print (line)
            
