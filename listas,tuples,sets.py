 courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Education']
# nums = [1, 5, 2, 4, 3]

# print(len(courses))
# print(courses[1])
# print(courses[-1])
# print(courses[0:2])
# print(courses[2:2])
# print(courses[2:])

# courses.append('Art')
# courses.insert(0, 'Art')
# courses.extend(courses_2)
# courses.remove('Math')
# courses.pop()
# courses.reverse()
# courses.sort()
# nums.sort()
# courses.sort(reverse=True)
# nums.sort(reverse=True)

# sorted_courses = sorted(courses)
# print(sorted_courses)

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# print(courses.index('CompSci'))
# print('Art' in courses)

# for item in courses:
    # print(item)

# for index, item in enumerate(courses):
    # print(index, item)

# for index, item in enumerate(courses, start=1):
    # print(index, item)

# course_str = '-- '.join(courses)
# print(course_str)

# Las tuplas son inmutables, a comparacion de las listas que se pueden modificar
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# print(tuple_1)

# Los sets eliminan los duplicados, solo importa si hay los valores dentro del set dejando de lado el orden.
# cs_courses = {'History', 'Physics', 'Math', 'Physics', 'CompSci'}
# print(cs_courses)
# print('Math' in cs_courses)

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Physics', 'Math', 'Art', 'Design'}
# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))

# empty_list = []
# empty_list = list()
# empty_tuple = ()
# empty_tuple = tuple()
# empty_set = {}
# empty_set = set()

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
    # my_list.append(n)
# print (my_list)


# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
    # my_list.append(n*n)
# print(my_list)


# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
    # if n % 2 == 0:
        # my_list.append(n)
# print(my_list)


# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
    # for num in range(4):
        # my_list.append((letter, num))
# print(my_list)


# Dictionary Comprenhensions
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# my_dict = {name: hero for name, hero in zip(names, heros)}
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)


# Compresion de sets
# nums = [1,2,2,3,3,4,5,6,6,7,7,8,8,9,9,10,10]
# my_set = set()
# for n in nums:
    # my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)
