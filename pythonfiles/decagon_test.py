def say_hello(name=None):
    print(name)
    if name is not None:
        return 'Hello, ' + name + '!'
    else:
        return 'Hello there!'

print(say_hello(name=None))


def laptoprentals(times):
    t = sorted(times, key = lambda x: x[0])
    print(t)
    min_num = 0
    start = []
    end = []
    for i in range(len(t)):
        if t[i][0] < 0:
            print('Time cannot be less than 0')
        if t[i][1] < t[i][0]:
            print('not allowed')
        start.append(t[i][0])
        end.append(t[i][1])
        l2 = t[i]
        for x in range(len(l2)):
            print(l2[x])
        
  
times = [[0,2],[1,4],[4,6],[0,4],[7,8],[9,11],[3,10]]
laptoprentals(times)

'''
You're given a list of time intervals during which students at a school need a laptop. These time intervals are represented by pairs of integers [start, end], where 0 <= start < end. However, start and end don't represent real times; therefore, they may be greater than 24.

No two students can use a laptop at the same time, but immediately after a student is done using a laptop, another student can use that same laptop. For example, if one student rents a laptop during the time interval [0, 2], another student can rent the same laptop during any time interval starting with 2.

Write a function that returns the minimum number of laptops that the school needs to rent such that all students will always have access to a laptop when they need one.

laptopRentals(times)
Parameters
times: Array (of Array (of Integers)) - A 2D array containing the times the student would require a laptop.

Return Value
Integer - Minimum number of laptops the school needs to rent.

Examples
times	Return Value
[[0,2],[1,4],[4,6],[0,4],[7,8],[9,11],[3,10]]	3
[[0,4],[2,3],[2,3],[2,3]]	4
[[1,5],[5,6],[6,7],[7,9]]	1

'''
