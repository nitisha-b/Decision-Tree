# Lab 4
# Name: Nitisha Bhandari

import csv
import math

# This function reads in a .csv file and creates a list of dictionaries with
# one line per dictionary and the features as keys. This assumes the first
# line of the file is a header row with the feature names.

def read_data(filename):
    with open(filename,'r') as f:
        column_labels = f.readline().strip().split(',')
        reader = csv.reader(f)
        data = []
        for line in reader:
            row = {}
            for col in range(len(column_labels)):
                row[column_labels[col]] = line[col]
            data.append(row)

    #print(data)
    return data

# This function takes in one feature and the list of dictionaries (data)
# and calculates the entropy for that particular feature. 
# This assumes that a feature only has 2 different values 

def get_entropy(feature, data): 

    # Get the list of values for a particular key from all dictionaries in the list
    valueList = [d[feature] for d in data]

    value1 = valueList[0]			#one value of the feature
    n = len(valueList)
    a = valueList.count(value1)		#no. of occurances of the first feature
    b = n-a							#no. of occurances of the second feature

    ent = -(float(a)/n) * math.log(float(a)/n, 2) - (float(b)/n) * math.log(float(b)/n, 2)

    return ent

# This function takes in the list of dictionaries of all the features and 
# their values, a list of the features, and the main feature to calculate the 
# entropy of the main feature and of the individual features and calculate 
# the information gain. It returns the feature with the highest information gain

def find_most_informative_feature(data, feature_list, main_feature):

    # Entropy of our main feature 'Buys computer'
    main_entropy = get_entropy(main_feature, data)
    print('Main feature entropy:', main_entropy)

    ageGroup0, ageGroup1, ageGroup2 = ([] for i in range(3))
    incomeHigh, incomeMedium, incomeLow = ([] for i in range(3))
    studentYes, studentNo = ([] for i in range(2))
    crExcellent, crFair = ([] for i in range(2))
    
    #Make separate lists for different values of each feature
    for d in data:
        
        #Age
        if(d['Age'] == '<=30'):
            ageGroup0.append(d)
        
        elif(d['Age'] == '31-40'):
            ageGroup1.append(d)

        elif(d['Age'] == '>40'):
            ageGroup2.append(d)

        #Income
        if(d['Income'] == 'High'):
            incomeHigh.append(d)    
        
        elif(d['Income'] == 'Medium'):
            incomeMedium.append(d)

        elif(d['Income'] == 'Low'):
            incomeLow.append(d)

        #Student?
        if(d['Student'] == 'Yes'):
            studentYes.append(d) 

        elif(d['Student'] == 'No'):
            studentNo.append(d) 

        #Credit Rating
        if(d['Credit rating'] == 'Excellent'):
            crExcellent.append(d) 

        elif(d['Credit rating'] == 'Fair'):
            crFair.append(d)

    #print(ageGroup1) 

    n = float(len(data))        #total number of people 

    #Combined entropy of age
    ent_age = (len(ageGroup0)/n) * get_entropy(main_feature, ageGroup0) + (len(ageGroup2)/n) * get_entropy(main_feature, ageGroup2) + (len(ageGroup1)/n) * 0 #+ get_entropy(main_feature, ageGroup1) -- gets math domain error
    print('Age Entropy: ', ent_age)

    #Combined entropy of income
    ent_income = (len(incomeHigh)/n) * get_entropy(main_feature, incomeHigh) + (len(incomeMedium)/n) * get_entropy(main_feature, incomeMedium) + (len(incomeLow)/n) * get_entropy(main_feature, incomeLow)
    print('Income Entropy: ', ent_income)

    #Combined entropy of Student
    ent_student = (len(studentYes)/n) * get_entropy(main_feature, studentYes) + (len(studentNo)/n) * get_entropy(main_feature, studentNo) 
    print('Student Entropy: ', ent_student)

    #Combined entropy of Student
    ent_cr = (len(crExcellent)/n) * get_entropy(main_feature, crExcellent) + (len(crFair)/n) * get_entropy(main_feature, crFair)
    print('Credit Rating Entropy: ', ent_cr)

    # Calculate information gain for each feature and store them in a dictionary with the feature as key
    infoGainDict = {} 

    info_age = main_entropy - ent_age
    infoGainDict.update({'Age': info_age})
    print('Age info gain: ', info_age)

    info_income = main_entropy - ent_income
    infoGainDict.update({'Income': info_income})
    print('Income info gain: ', info_income)

    info_student = main_entropy - ent_student
    infoGainDict.update({'Student': info_student})
    print('Student info gain: ', info_student)

    info_cr = main_entropy - ent_cr
    infoGainDict.update({'Credit rating': info_cr})
    print('Credit Rating info gain: ', info_cr)
    
    # Get the max information gain
    max_gain = max(infoGainDict.values())

    # Get the most informative feature from the max information gain
    mvf = infoGainDict.keys()[infoGainDict.values().index(max_gain)]
    print('Most valuable feature: ', mvf)
   
    return mvf   

def demo():
    
    mydata = read_data('computer.csv')
    features = mydata[0].keys()
    mainfeature = 'Buys computer'
    mvf = find_most_informative_feature(mydata, features, mainfeature)

    #print(features)

if __name__ == '__main__':
    demo()

