##### Even and Odd Counter #####

#Ask the user to enter multiple integers separated by spaces, and store them in a list.
#Use a loop to iterate through each number in the list.
#Use conditionals to determine if a number is even or odd and keep a count of each.
#Print the counts of even and odd numbers.




def create_list():

    user_num=(input("Enter multiple numbers separated by spaces: "))

    user_num = list(user_num)
    user_num.append(" ")
    for i in range(len(user_num)):
        if user_num[i] != " ":
            user_num[i] = int(user_num[i])
        else:
            pass
    
    even_num = 0
    odd_num = 0
    for i in range(len(user_num)):
        if user_num[i] == " ":
            if user_num[i-1]%2==0:
                even_num += 1
            elif user_num[i-1]%2!=0:
                odd_num += 1
    print(f"even numbers = {even_num} odd numbers = {odd_num}")
   
   
   
create_list()