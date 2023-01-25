
#******************* I] Created a file

# with open("myfile.txt", "w") as f:
#     pass


#******************* II] Opened a file and printed the lines using readline()

# p =  open("myfile.txt", "r")
# while True:
#     line = p.readline()
#     print(line)
#     if not line:
#         break


#o/p
# 89,67,90

# 91,70,73

# 90,95,99



#********************* III] Splited lines futher

# p =  open("myfile.txt", "r")
# i=0
# while True:
#     i = i+1
#     line = p.readline()
#     m1 = line.split(",")[0] #m1,m2,m3 all are string , if want in int - typecast it
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]

#     print(f"Marks of student {i} in Eng is {m1}")
#     print(f"Marks of student {i} in Math is {m2}")
#     print(f"Marks of student {i} in Sci is {m3}")
#     print(line)

#     if not line:
#         break



# Marks of student 1 in Eng is 89
# Marks of student 1 in Math is 67
# Marks of student 1 in Sci is 90

# 89,67,90

# Marks of student 2 in Eng is 91
# Marks of student 2 in Math is 70
# Marks of student 2 in Sci is 73

# 91,70,73

# Marks of student 3 in Eng is 90
# Marks of student 3 in Math is 95
# Marks of student 3 in Sci is 99
# 90,95,99



#************************ IV] Writelines - newline
#writelines does not add content to newline on its own for that use We'll need to add \n at end of item OR Simply follow [V]

# lines = ['line1\n', 'line2\n', 'line3\n']
# with open("myfile1.txt", "w") as f:
#     f.writelines(lines)


#********************* V] Write - newline

lines = ['line3', 'line4', 'line5']
ff = open("myfile2.txt", "w")
for line in lines:
    ff.write(line + '\n')
ff.close()


