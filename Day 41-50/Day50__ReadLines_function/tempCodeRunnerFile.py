lines = ['line1\n', 'line2\n', 'line3\n']
with open("myfile1.txt", "w") as f:
    f.writelines(lines)