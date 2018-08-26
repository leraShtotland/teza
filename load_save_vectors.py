def readVecFile():
    vec_dic={}
    counter=0
    with open("vec_data_15.txt") as f:
        vec_data = f.readlines()
    for line in vec_data:
        if (counter%2==0):
            item=int(line)
        else:
            list_item=line.split(' ')
            vec_dic[item]=list_item
        counter+=1
    return vec_dic
