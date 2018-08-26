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



def getDics(vec_dic):
    with open("Output.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    # print("content")
    # print(content)
    list_images=[]
    list_labels=[]
    counter=0
    for item in content:
        img=int(item[:-4])
        if img in vec_dic:
            if (counter<4160):
              list_images.append(item)
              list_labels.append(vec_dic[img])
            counter+=1
    print("list_images")
    print(list_images)
    print("list_labels")
    print(list_labels)
    print("counter_all")
    print(counter)
    print("len_images")
    print(len(list_images))
    print("len(labels)")
    print(len(list_labels))
    return list_images, list_labels

def readVecFile_users():
    vec_dic={}
    counter=0
    with open("vec_data_user_100.txt") as f:
        vec_data = f.readlines()
    for line in vec_data:
        if (counter%2==0):
            item=int(line)
        else:
            list_item=line.split(' ')
            vec_dic[item]=list_item
        counter+=1
    return vec_dic
