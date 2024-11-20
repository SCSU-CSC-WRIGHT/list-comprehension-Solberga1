##### Unique List Merger #####

#Ask the user to enter two lists of numbers, each separated by spaces. For example: 1,2,4,6 2,5,7,1
#Combine them into one list.
#Use a loop and conditionals to remove duplicate entries.
#Print the merged list without duplicates


def list_merger():
    user_list1 = input("Please enter a list of numbers: ")
    user_list1 = user_list1.split(" ")


    user_list2 = input("Please enter another list of numbers: ")
    user_list2 = user_list2.split(" ")


    for item in user_list1:
        if item in user_list2:
            user_list2.remove(item)   

    combined_list = user_list1+user_list2


    

    print(combined_list)



list_merger()