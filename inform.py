f = open('naych.txt', 'a+')


for i in range(5):
    d1 = input()
    f.write(d1)
    f.write('\n')
f.close()