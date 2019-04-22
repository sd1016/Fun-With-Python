# EXERCISE 22 from:
# http://www.practicepython.org/
# Python 3.5

import json
dict_image = {}
with open ("./temp-files/Training_01.txt") as f:
    for line in f:
        list1 = line.strip().split('/')
        if " ".join(list1[2:(len(list1)-1)]) in dict_image:  #(list1[2:(len(list1)-1)]) <- image category, (list1[len(list1)-1]) <- image
            dict_image[" ".join(list1[2:(len(list1)-1)])] += 1
        else:
            dict_image[" ".join(list1[2:(len(list1)-1)])] = 1
print (json.dumps(dict_image, indent=1))


#provided solution
# counter_dict = {}
# with open('./temp-files/Training_01.txt') as f:
# 	line = f.readline()
# 	while line:
# 		line = line[3:-26]
# 		if line in counter_dict:
# 			counter_dict[line] += 1
# 		else:
# 			counter_dict[line] = 1
# 		line = f.readline()
#
# print(json.dumps(counter_dict,indent=1))
