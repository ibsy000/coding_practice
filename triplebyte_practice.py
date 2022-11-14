def breadth_first_search(root_node, fn):
    # Returns the first node for which fn(node) is truthy
    queue = deque([root_node]) # Python queue object
    while len(queue) > 0:
        node = queue.popleft() # Grab the first element in queue
        if fn(node.value):
            return node
        else:
            queue.extend(node.children)
    return None

# Breadth-first search is an algorithm for finding an element in a tree or graph. 
# BFS starts by checking the root node, then it checks all of the elements that 
# are 1 edge away from the root node, then all of the elements 2 edges away, and 
# so on until the desired element is found or the entire graph is traversed. It 
# accomplishes this by building a first-in first-out queue of elements to check. 
# As each element is checked, its children are added to the end of the queue so 
# that the entire graph is traversed layer by layer.



def modify(elems):
    elems.append("foo")
    elems = ["bar", "baz"]

array = ["qux"]
modify(array)
print(array)

# In Python, like in Java, Javascript, and many other popular languages, objects 
# are passed to functions by reference. This means that when a list is passed as 
# a parameter to a function, the parameter still refers to the original list 
# (and any modification to the list will be visible outside the function). Thus, 
# inside the function "modify", elems.append("foo") adds "foo" to the list in 
# the outer scope. However, variable assignment (elems = ["bar", "baz"]) simply 
# points the local reference elems to a new object, and has no impact on the 
# outer list.



matrix = []
row = [0, 0]
for i in range(2):
    matrix.append(row)
matrix[1][1] = 1
print(matrix)

# The bug here is that "matrix" contains two references to the same object, so 
# a change to one row shows up in both rows. The programmer likely wanted 
# references to two different objects. The solution here is to append a copy of 
# row to matrix, with something like matrix.append(copy.copy(row)). More compactly 
# in Python, a 2D array can be initialized with 
# matrix = [[0 for _ in range(width)] for _ in range(height)].



def factory():
    values = []
    def widget(value):
        values.append(value)
        return values
    return widget

worker = factory()
worker(1)
worker(2)
print(worker(4))

# This question demonstrates a closure - a function that references one or more 
# variables in its parent's scope. Here, the child function widget references 
# the variable values, which was defined in the parent function factory. Even 
# though factory has returned, the widget function still holds a reference to 
# values and can read and write to it. We say that widget closes over values 
# because it retains a reference to the values variable. This technique is 
# valuable because it allows functions to have private state without objects or 
# Object Oriented Programming. For example, we can use closures to create 
# generator function (e.g., primeGenerator) or capture a partial function 
# application (e.g., makeAdder).



def int_to_base(num, base):
    # Converts a non-negative integer to an arbitrary base
    # Returns an array, e.g. int_to_base(6, 2) => [1, 1, 0]
    if num == 0:
        return []
    quotient = num // base # Integer division
    remainder = num % base
    return int_to_base(quotient, base) + [remainder]

print(int_to_base(6,2))

# This recursive function calculates the digits of a number in a given base 
# from right to left. To see how this works, consider the number 12345. Notice 
# that 12345 % 10 = 5, and 12345 // 10 = 1234. In effect, these two operations 
# allow us to pop the rightmost digit off of a number in base 10. We can do +
# these same operations in any other base by changing the 10 in those expressions 
# to an arbitrary integer. Applying these operations recursively gives a 
# wonderfully simple base conversion.


def merge(list1, list2):
    # Takes two sorted lists and merges them in sorted order
    i1 = i2 = 0
    out_list = []
    while i1 < len(list1) or i2 < len(list2):
        elem1 = list1[i1] if i1 < len(list1) else None
        elem2 = list2[i2] if i2 < len(list2) else None
        if elem1 is None or (elem2 is not None and elem2 < elem1):
            out_list.append(elem2)
            i2 += 1
        else:
            out_list.append(elem1)
            i1 += 1
    return out_list

# This merge routine is very useful in sorting algorithms, most famously in merge 
# sort. The key idea is to take the smallest element in each list, add the smaller 
# of those two values to an output list, and discard that element from further 
# consideration. The real genius is that, because the two lists are already sorted, 
# we can merge them together in linear time. We can compare the first element of 
# each list, pop off the smaller value, and add it to an output list, continuing 
# until both lists are empty. This approach works well for merging 2 lists, but 
# does not extend well to larger numbers of lists. However, a heap data structure 
# is able to merge k lists with n total items in O(k log n) time.


# What does the following code do?
b = bytearray([0xd9, 0x83, 0xd9, 0x84, 0xd8, 0xa8])
message = b.decode('utf-8')

# Computers store all data as bytes, not text. To interpret bytes as text (characters), 
# we rely on arbitrary mappings. For example, in ASCII (a popular but old mapping) 
# the byte 01000001 means 'A'. One problem with ASCII is that it only support 
# English characters (and a few other European languages). To solve this problem, 
# Unicode was created. Unicode is like ASCII, but larger. It supports 1,114,112 
# different symbols (more than enough for all human languages, plus some fun 
# stuff like Emoji 😱). However, because Unicode is so much larger than ASCII, 
# it takes more than 1 byte to encode each character. To make common text smaller, 
# UTF-8 was created. It is a way to encode Unicode characters, that uses a 
# variable-width encoding scheme so that common English characters take less memory. 
# When the above byte array is decoded with the UTF-8 encoding, we get three Unicode 
# code points, u'\u0643\u0644\u0628', which is rendered as كلب.



# Which of the following regular expressions will match blabber but not babel?
# Answer: ^([^b]*b[^b]*){3}$

# Regular expressions are a concise way to express pattern matching over strings. 
# The correct answer above matches strings that have exactly three "b"s. We won't 
# go into the details of regular expression syntax here, but you can look that up 
# online. Interestingly, regular expressions come from theoretical computer science 
# (they are equivalent to finite state automata). And implementing a regular 
# expression engine involves simulating a finite state automaton! They didn't 
# become popular with programmers until 1968, when Ken Thompson used regular 
# expressions as a pattern matching syntax in the QED editor.




# Which of the following statements about threads and processes is true?
# Answer: Threads in a process share the same address space, but have their own call stacks

# In modern operating systems, processes are independent instances of program 
# execution and are made up of one or more threads. Processes are largely independent 
# of each other and only interact through inter-process communication channels. 
# In comparison, threads in the same process share almost all resources, including 
# memory space and file descriptors. As a result, threads are generally faster 
# to create and destroy and can communicate between each other more quickly than 
# processes can. Because threads execute concurrently, each thread needs to 
# maintain independent call stack with information about the current state of 
# execution. The call stack holds local variables, the return address, and the 
# enclosing context of the current operation. But because they share memory with 
# other threads in the same process, threads must synchronize access to shared 
# data to maintain data integrity.



# The following code seems to work, but it wouldn't pass a security review. 
# Which vulnerability is it exposed to?

def login(request, cursor):
    cursor.execute("SELECT * FROM users WHERE email = '" \
        + request.params["email"] + "' AND password = '" \
        + request.params["password"] + "'")

# Answer: SQL injection from malicious user input

# All four answers are real attacks, but this SQL statement is particularly 
# vulnerable to a SQL injection. If an attacker submitted a request with the 
# email parameter set to "admin@example.com" and the password set to "password' 
# OR '1'='1", the database would execute the following query:

# SELECT * FROM users WHERE email = 'admin@example.com'
#     AND password = 'password' OR '1'='1'

# This would bypass the password verification and let the attacker login as the 
# admin. The key part of the attack is the single quote after "password", which 
# allows the attacker to break out of the string comparison and modify the intent 
# of the query. One solution here is to sanitize or escape user inputs instead 
# of directly interpolating them into SQL statements. However this can be fragile 
# and error-prone, so the best practice is generally to use prepared statements, 
# which lets the database itself protect against SQL injections.



# The following function seems to work, but it wouldn't pass a security review. 
# Which vulnerability is this code most exposed to?

def secure_hash_comparison(user_submitted_hash, database_hash):
    if len(user_submitted_hash) != len(database_hash):
        return False
    for i in range(len(user_submitted_hash)):
        if user_submitted_hash[i] != database_hash[i]:
          return False
    return True

# Answer: Timing attacks on the string comparison
# While all four answers are legitimate attacks on cryptographic hash functions, 
# this function specifically is most vulnerable to timing attacks. The key 
# observation is that the loop that compares the two strings will loop more 
# times (and take longer) if the two hashes share a common prefix. This allows 
# an attacker to go through the hash from beginning to end, and at each character 
# position try all 256 possible bytes. When they guess the correct byte, the 
# comparison will take slightly longer. They can then go on to the next character 
# position, and in short order they'll have extracted the correct hash.





# It's possible to use the binary search algorithm to find an element in a sorted 
# array in O(log n) time. Binary search trees have this same search performance. 
# Why, then, do we ever use more complicated binary search trees rather than sorted lists?

# Answer: BSTs are faster for inserting and deleting items

# Self-balancing Binary Search Trees take O(log n) worst-case time to insert or 
# delete an item, even when it requires a rebalance operation. In comparison, 
# sorted arrays take worst-case O(n) time to add or remove an item, which can be 
# prohibitively expensive for large data structures. While arrays and trees both 
# require O(n) memory, the constant factor of a tree is much greater because of 
# the memory required for child pointers. Additionally, B-trees and B+ trees can 
# be optimized on modern hardware, minimizing cache misses and disk reads to 
# increase real-world performance.





# The year is 20XX. The United Earth Federation has created a network of warp 
# stations between distant star systems. Your mission, should you choose to 
# accept it, is to hop across the galaxy and man the battlestation at the 
# TRAPPIST-1 system. Your computer has a map of UEF warp stations and the 
# routes that connect them. Which algorithm will help you get to your destination 
# in the fewest number of warps?

# Answer: Breadth first search will find the shortest path to the battlestation, 
# even if the network contains cycles

# Breadth-first search and depth-first search are the two most basic graph traversal 
# algorithms. BFS explores nodes in expanding circles of distance from its start 
# location, and thus will find the shortest path between two nodes (or star systems). 
# DFS makes no such guarantee (indeed, it often finds pretty crazy, winding paths). 
# One advantage of DFS, however, is that it uses much less memory. BFS must store 
# a queue of nodes to visit, and this queue can grow to (order) the size of the 
# entire graph. If you need to find the shortest path through a graph, but don't 
# want to use linear memory, a cool algorithm is iterative deepening search. It's 
# just like depth-first search, but takes a parameter that limits how deep to look. 
# If we limit the depth to 5, say, it will do a depth-first exploration of all paths 
# up to length 5. Imagine what happens, now, if we run the search multiple times, 
# starting with a depth limit of 1, then 2, then 3, etc. Because this explores 
# all paths of length N before it explores any of length N+1, it is guaranteed to 
# find shortest paths. And because it's using depth-first traversal, it only uses 
# O(log n) memory! This sounds really slow, you might think (it seems to be 
# duplicating a lot of searching). However, consider the case of a roughly balanced 
# binary tree. Half of all nodes will be found in the leaf level of the tree. And 
# these nodes are only explored once. If we calculate the total number of times 
# that nodes are traversed, we get N + N/2 + N/4... This sequence sums to 2N. 
# Thus, iterative deepening search still takes linear time.





# Warp drives, as advanced as they are, don't allow teleportation. Your computer 
# has just downloaded information on the travel time between connected warp 
# stations. Which algorithm will find the path with the shortest travel time from 
# Earth to TRAPPIST-1?

# Answer: Dijkstra's algorithm extends BFS to weighted graphs

# BFS finds the shortest path on an unweighted graph, because it always explores 
# the path with the fewest steps before it expends to paths with more steps. 
# However, in a weighted graph, a path with more steps might be shorter than one 
# with fewer. Dijkstra's algorithm fixes this problem. It's a best-first graph 
# traversal. It looks a lot like BFS, but in place of a queue, it uses a priority 
# queue. When a node is pushed onto the queue, it's given a priority equal to 
# the length of the path to that node. Thus when a node is dequeued, the path 
# that node represents will be the shortest unexplored path. If you want to get 
# even more advanced, you can view the A graph search algorithm as an extension 
# of Dijkstra's. It's just like Dijkstra's, but rather than using the path length 
# alone as the priority in the best-first queue, it adds a heuristic that estimates 
# how far a given node might be from the destination. As long as this heuristic 
# satisfies certain constraints, A is still guaranteed to find the shortest path.