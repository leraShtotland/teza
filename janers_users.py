import csv
#The code make dictinary of users, for each user there is another dicitinary with all joures, and for each jouaner all the movies that the 
#user saw in this janears
#use this code for cycle gan 
def load_data(data_path):
    '''
    As for bpr experiment, all ratings are removed.
    '''
    user_ratings = {}
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if (row[0]!="userId"):
                u=int(row[0])
                i=int(row[1])
                if u not in user_ratings:
                    user_ratings[u]=[]
                user_ratings[u].append(i)
    return user_ratings

data_path=('ratings.csv')
user_ratings = load_data(data_path)

path2="movies.csv"
def load_data_movies(path2):
    janaer_dic = {}
    janer_list = []
    movis_names={}
    with open(path2, 'r', encoding="utf8") as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if (row[0]!="movieId"):
                movie=int(row[0])
                movie_name=row[1]
                movis_names[movie]=movie_name
                janer=row[2]
                janerInOne=janer.split('|')
                #janaer_dic[movie] = janer
                janaer_dic[movie] = janerInOne
                for j in janerInOne:
                    if j not in janer_list:
                        janer_list.append(j)
    return janaer_dic, janer_list ,movis_names

janaer_dic, janer_list ,movis_names=load_data_movies(path2)
#print(janaer_dic)

def dic_by_janers(user_ratings,janaer_dic,janer_list):
    conter = 0
    user_janers={}
    for key in user_ratings:
        user_janers[key]={}
        for janer in janer_list:
            user_janers[key][janer]=[]
        for item in user_ratings[key]:
            if (item==7502 or item==108583 or item==162376 or item==94466 or item==77658 or item==108979 or item==108548 or item==150856):
                continue
            janers_movie=janaer_dic[item]
            for j in janers_movie:
                user_janers[key][j].append(item)
                conter+=1
    return user_janers


user_janers=dic_by_janers(user_ratings,janaer_dic,janer_list)
print(user_janers)

#
# for user in user_janers:
#     print(user)
