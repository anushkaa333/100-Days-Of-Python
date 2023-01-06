questions = [ 
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    ["fb was made in which language", 'js', 'php', 'java', 'python', 4],
    
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]
midlevels = [4, 9]
midlevels.sort(reverse=True)

price = 0
index =0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for {levels[i]} is {question[0]}")
    print(f"1. {question[1]}              2.{question[2]} ")
    print(f"3. {question[3]}              4.{question[4]} ")
    reply = int(input("Enter option 1-4"))
    if(reply==question[-1]):
        print("Answer is correct")
        if(i==4):
            price = levels[i]
            print(f"*************Amt in acc {price}***********")
        if(i==9):
            price = levels[i]
            print(f"***********Amt in acc {price}**************")
    else:
        print("Answer is wrong")
        # for j in range (0, len(midlevels)):
        #     if midlevels[j]< i:
        #         # index = str(midlevels[j])
        #         # price = str(price[index])
        #         price = str(price[midlevels[j]])
        #         break
        break
    

print(f"You have won {price}")


# Question for 1000 is fb was made in which language
# 1. js              2.php
# 3. java              4.python
# Enter option 1-44
# Answer is correct
# Question for 2000 is fb was made in which language
# 1. js              2.php
# 3. java              4.python
# Enter option 1-44
# Answer is correct
# Question for 3000 is fb was made in which language
# 1. js              2.php
# 3. java              4.python
# Enter option 1-44
# Answer is correct
# Question for 5000 is fb was made in which language
# 1. js              2.php
# 3. java              4.python
# Enter option 1-44
# Answer is correct
# Question for 10000 is fb was made in which language
# 1. js              2.php
# 3. java              4.python
# Enter option 1-44
# Answer is correct
# *************Amt in acc 10000***********
# Question for 20000 is fb was made in which language
# 1. js              2.php
# 3. java              4.python
# Enter option 1-44
# Answer is correct
# Question for 40000 is fb was made in which language
# 1. js              2.php
# 3. java              4.python
# Enter option 1-44
# Answer is correct
# Question for 80000 is fb was made in which language
# 1. js              2.php
# 3. java              4.python
# Enter option 1-42
# Answer is wrong
# You have won 10000
    