from statistics import mean
n = int(input())
dictionary = dict()
for n in range(0,n):
    main_input = str(input()).split(" ")
    dictionary[str(main_input[0])] = mean(list(map(float,main_input[1:])))
print("{0:.2f}".format(dictionary[str(input())]))