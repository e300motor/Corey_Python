# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()
#-------------------------------------------------------------------

books = ['Java', 'Csharp']
books_2 = ['Probability', 'Statistics']

books.append('Python')
books.insert(0, 'C')

books.extend(books_2)  # ['C', 'Java', 'Csharp', 'Python', 'Probability', 'Statistics']

books.remove('C')
popped = books.pop()  # ['Java', 'Csharp', 'Python', 'Probability']

print(popped)

books.sort(reverse=True)  # ['Python', 'Probability', 'Java', 'Csharp']
books.reverse()  # ['Csharp', 'Java', 'Probability', 'Python']

sorted_books = sorted(books, reverse=True)  # reserve origin books , produce a new one

print(books.index('Python'))
print('Math' in books)

print('sorted_books= ', sorted_books)

nums = [5, 9, 2, 0, 4, 1]

print(min(nums), max(nums), sum(nums))

for index, book in enumerate(books, start=1):
    print(index, book)

books_str = ' - '.join(books)  # Csharp - Java - Probability - Python
new_list = books_str.split(' - ')
print(books_str)
print(new_list)

# tuple not modified

t_books = ('Java', 'Csharp')
t_books2 = t_books

print(t_books is t_books2)

# set
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))
print(cs_courses.difference(art_courses))


li = [-6, -5, 1, 2, 3]

s_li = sorted(li, key=abs)  # sort by absolute value
print(s_li)
