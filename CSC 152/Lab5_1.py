##### Lab 1: Grade Calculator #####

## Write a Program thar Calculates the Letter Grade Based on a List of Scores ##

#create function#
def lab_1():

    num_scores=int(input("Enter the numbers of  tests you took: "))

    #Create Empty List to store scores
    scores_list = []

    #Create Loop to place scores in list
    for i in range(num_scores):
        score= float(input(f"Enter your test score number {i+1}: "))
        scores_list.append(score)         
    print(scores_list)
    average_score = sum(scores_list)/len(scores_list)
    if average_score >=90:
        print("You got an A and your averaeg was", average_score )
    elif average_score >=80 and average_score < 90:
        print("You got a B and your average was", average_score)
    else:
        print("You got an F and your average was", average_score)






lab_1()