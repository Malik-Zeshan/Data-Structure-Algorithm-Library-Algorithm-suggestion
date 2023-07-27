from collections import deque
from typing import List, Dict
from queue import PriorityQueue # essentially a binary heap
from collections import defaultdict

# NOTE: Stack -----------------------------------------------------------------------------------------------------
class Stack:
    def __init__ (self):
        self.container = deque()
    def top(self):
        return self.container[-1]

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def __len__(self):
        return len(self.container)

    def reverse(self):
        while len(self.container) != 0:
            print (self.container.pop(), end='')

    def is_empty(self):
        if len(self.container)==0:
            return True

    def is_balance(self, eq):
        self.eq = eq
        closing = {")":"(","}":"{","]":"["}
        opening =['(','{','[']
        try:
            for i in eq:
                if i in opening:
                    self.push(i)
                elif (i in closing) and (closing[i] == self.container[-1]):
                    self.pop()
        except:
            return False
        else:
            if len(self.container) == 0:
                return True
            else:
                return False


# NOTE: Queue ----------------------------------------------------------------------------------------------------
class Queue:
    def __init__(self):
        self.list=[]
    def enqueue(self,val):
        self.list.insert(0, val)
    def dequeue(self):
        return self.list.pop()
    def display(self):
        return self.list
    def is_empty(self):
        return len(self.list) == 0
    def front(self):
        return self.list[-1]
    def rear(self):
        return self.list[0]


# NOTE: Circular Queue -----------------------------------------------------------------------------------------
class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front = self.rear = -1
    def enqueue(self,item):
        if((self.rear+1)%self.size)==self.front:
            print("queue is full")
        elif(self.front==-1):
            #queue is empty
            self.front=0
            self.rear=0
            self.queue[self.rear]=item
        else:
            #place data on next position to rear
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=item

    def dequeue(self):
        if self.front==-1:
            #queue is empty
            print("empty")
        elif(self.front==self.rear):
            #only one element is placed in queue
            value=self.queue[self.front]
            self.queue[self.front]=None
            self.rear=self.front=-1
            print(value)
        else:
            value=self.queue[self.front]
            self.queue[self.front]=None
            self.front=(self.front+1)%self.size
            print(value)

    def display(self):
        l=[]
        for i in self.queue:
            if i is not None:
                l.append(i)
        print(l)


# NOTE: Linked List ----------------------------------------------------------------------------------------------
class L_Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class Linked_list:
    def __init__(self):
        self.head=None

    def display(self):
        node=self.head
        if node == None:
            print("Linked List is Empty")
        else:
            linkedlist=[]
            while node.next is not None:
                linkedlist.append(node.data)
                node=node.next
            linkedlist.append(node.data)
            print("linked List",linkedlist)
            return linkedlist

    def insert_last(self,data):
        if self.head is None:
            self.head = L_Node(data)
        else:
            new=L_Node(data)
            node=self.head
            while node.next is not None:
                node=node.next
            node.next=new

    def insert_first(self,data):
        if self.head is None:
            self.head = L_Node(data)
        else:
            new=L_Node(data)
            new.next=self.head
            self.head=new

    def insert_position(self, index, data):
        if index == 0:
            self.insert_first(data)
        elif index == (self.count()-1):
            self.insert_last(data)
        elif index >0 and index < (self.count()-1):
            node=self.head
            i=0
            while node.next is not None:
                i=i+1
                if i==index:
                    new=L_Node(data)
                    new.next=node.next
                    node.next=new
                    break
                else:
                    node=node.next
            else:
                print("Invalid index")

    def delete_position(self,index):
        if index == 0:
            self.delete_first()
        elif index == (self.count() -1):
            self.delete_last()
        elif index > 0 and index < (self.count() -1):
            node=self.head
            i=0
            while node.next is not None:
                prev=node
                node=node.next
                i=i+1
                if i==index:
                    prev.next=node.next
                    break
        else:
            print("Invalid Index")

    def delete_data(self,data):
        if self.head is None:
            print("Linked List is Empty")
        else:
            nod=self.head
            while nod is not None:
                if nod.data == data:
                    break
                prev= nod
                nod = nod.next
            prev.next = nod.next
            node = None

    def delete_all(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            self.head = None
        print("all nodes has been deleted")

    def delete_last(self):
        node=self.head
        if node == None:
            print("Linked List is Empty")
        else:
            while node.next.next is not None:
                node=node.next
            node.next=None

    def delete_first(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            node=self.head.next
            self.head=node

    def traverse(self):
        node=self.head
        if node==None:
            print("Linked List is Empty")
        else:
            linkedlist=[]
            while node.next is not None:
                linkedlist.append(node.data)
                node=node.next
            linkedlist.append(node.data)
            print(linkedlist)

    def count(self):
        node=self.head
        if node==None:
            print("Linked List is Empty")
        else:
            count=0
            while node.next is not None:
                count=count+1
                node=node.next
            return count+1

    def find(self,data):
        node=self.head
        if node==None:
            print("Linked List is Empty")
        else:
            x=''
            index=0
            while node is not None:
                if node.data==data:
                    print("founded")
                    x="founded"
                    break
                node=node.next
                index=index+1
            if x == "founded":
                print("value given is at index",index)
            else:
                print(x)
                print("not founded (:")

    def merge(self):
        node=self.head
        linkedlist=[]
        list2=[]
        while node is not None:
            linkedlist.append(node.data)
            node=node.next
        while True:
            x=int(input("enter elemnts of second linked list"))
            list2.append(x)
            n = int(input("press 0 if you want to enter more elements,press 1 to stop entering: "))
            if n == 1:
                break
        merged=linkedlist+list2
        for i in list2:
            self.insert_last(i)
        self.display()

    def divide_odd(self):
        node=self.head
        if node==None:
            print("Linked List is Empty")
        else:
            print(" seperating odd nodes")

            odd=[]
            while node is not None:
                if node.data%2!=0:
                    odd.append(node.data)
                node=node.next
            print("odd nodes data are",odd)


    def divide_even(self):
        node=self.head
        if node==None:
            print("Linked List is Empty")
        else:
            print(" seperating even nodes")
            even=[]
            while node is not None:
                if node.data%2==0:
                    even.append(node.data)
                node=node.next
            print("even nodes data are",even)


# NOTE: Double linked list --------------------------------------------------------------------------------------
class D_Node:
    def __init__(self,data= None):
        self.data=data
        self.next=None
        self.prev=None

class Double_Linked_list:
    def __init__(self):
        self.head=None
        # self.tail=None

    def display(self):
        node=self.head
        if node ==None:
            print("Linked List is Empty")
        else:
            l=[]
            while node is not None:
                l.append(node.data)
                node=node.next
            print("doubly linked list is",l)
            return l

    def insert_first(self,data):
        node=D_Node(data)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node

    def insert_last(self,data):
        node = self.head
        if node ==None:
            self.head = D_Node(data)
        else:
            new = D_Node(data)
            node=self.head
            while node.next is not None:
                node=node.next
            node.next=new
            new.prev=node

    def insert_position(self,index,data):
        if index == 0:
            self.insert_first(data)
        elif index == (self.count()-1):
            self.insert_last(data)
        elif index > 0 and index < (self.count()):
            new_node = D_Node(data)
            cur = self.head
            i = 1
            while True:
                previous = cur
                cur = cur.next
                if i == index:
                    new_node.next = previous.next
                    new_node.previous = previous
                    previous.next = new_node
                    return
                i += 1
        else:
            print("Invalid Index")

    def delete_first(self):
        if self.head ==None:
            print("Linked List is Empty")
        elif self.count() == 1:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def delete_last(self):
        node=self.head
        if node ==None:
            print("Linked List is Empty")
        elif self.count() == 1:
            self.head = None
        else:
            while node.next is not None:
                node=node.next
            node=node.prev
            node.next=None

    def delete_position(self,index):
        if index == 0:
            self.delete_first(data)
        elif index == (self.count()-1):
            self.insert_last(data)
        elif index > 0 and index < (self.count()-1):
            cur = self.head
            i = 0
            while True:
                if i == index:
                    previous.next = cur.next
                    cur = cur.next
                    cur.previous = previous
                    return
                previous = cur
                cur = cur.next
                i += 1
        else:
            print("Invalid Index")

    def delete_all(self):
        if self.head ==None:
            print("Linked List is Empty")
        else:
            self.head = None

    def traverse(self):
        node=self.head
        if node ==None:
            print("Linked List is Empty")
        else:
            l=[]
            while node is not None:
                l.append(node.data)
                node=node.next
            print(l)

    def count(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            node=self.head
            count=0
            while node is not None:
                count=count+1
                node=node.next
            return count


    def find(self,data):
        node=self.head
        if node ==None:
            print("Invalid")
        else:
            x=''
            index=0
            while node is not None:
                if node.data==data:
                    print("founded")
                    x="founded"
                    break
                node=node.next
                index=index+1
            if x == "founded":
                print("value given is at position",index)
            else:
                print("not founded (:")


    def divide_odd(self):
        node=self.head
        if node ==None:
            print("Linked List is Empty")
        else:
            odd=[]
            while node is not None:
                if node.data%2!=0:
                    odd.append(node.data)
                node=node.next
            print("odd nodes data are",odd)


    def divide_even(self):
        node=self.head
        if node ==None:
            print("Invalid")
        else:
            even=[]
            while node is not None:
                if node.data%2==0:
                    even.append(node.data)
                node=node.next
            print("even nodes data are",even)


    def merge(self):
        node=self.head
        Dlinkedlist=[]
        list2=[]
        while node is not None:
            Dlinkedlist.append(node.data)
            node=node.next
        while True:
            x=int(input("enter elemnts of second linked list"))
            list2.append(x)
            n = int(input("press 0 if you want to enter more elements,press 1 to stop entering: "))
            if n == 1:
                break
        merged=Dlinkedlist+list2
        for i in list2:
            self.insert_last(i)
        self.display()


# NOTE: Binary Search Tree ------------------------------------------------------------------------------------
class B_Node:
	def __init__(self, data = None):
		self.data = data
		self.right = self.left = None


class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def __insert(cur_node, data):
        	if cur_node == None:
        		return B_Node(data)
        	elif data < cur_node.data:
        		cur_node.left =__insert(cur_node.left, data)
        	else:
        		cur_node.right = __insert(cur_node.right, data)
        	return cur_node
        self.root = __insert(self.root, data)

    def display(self, cur_node ):	# NOTE: Preorder traversal is used (root-left-right)
    	if cur_node is not None:
    		print(cur_node.data, end=' -> ')
    		self.display(cur_node.left)
    		self.display(cur_node.right)
    	return

    def find(self, value, node, path=''):
    	if node is None:
    		print('\n',value, ' does not exits')
    	elif value == node.data:
    		path += (str(node.data)+'->')
    		print('\nValue Found')
    		if node.left == None and node.right == None: #checking the leaf node.
    			path += 'None'												#put None at the end of path if leaf node
    		print(f'path of {value} is: {path}')
    		return
    	else:
    		if value < node.data:
    			path += (str(node.data)+'->')
    			self.find(value, node.left, path)
    		else:
    			path += (str(node.data)+'->')
    			self.find(value, node.right, path)

    def level(self, value):	# NOTE: finding the level of the perticular node
    	def _level(value, node, ctr = -1):
    		if node is None:
    			print(value, ' does not exist')
    		elif node.data == value:
    			ctr += 1
    			print(f'level of the {value} is ',ctr)
    		elif value < node.data:
    			ctr += 1
    			return _level(value, node.left, ctr)
    		elif value > node.data:
    			ctr += 1
    			return _level(value,node.right, ctr)

    	if self.root is None:
    		print('Tree is empty')
    	else:
    		return _level(value, self.root)

    def tree_depth(self, node):	# NOTE: finding the height of the whole tree
    	if node is None:
    		return 0
    	leftsubtree = self.tree_depth(node.left)
    	rightsubtree = self.tree_depth(node.right)
    	return max(leftsubtree, rightsubtree) + 1


# NOTE: Sorting Algorithm----------------------------------------------------------------------------------------------------
def Bubble_Sorting(arr, order = 0):
    if order == 0:
        n=len(arr)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
    elif order == 1:
        n=len(arr)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
    else:
        print('Invalid order')
    return arr

def Selection_Sorting(arr, order = 0):
    if order == 0:
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    elif order == 1:
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] < arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    else:
        print('Invalid order')
    return arr

def Insertion_Sorting(arr, order = 0):
    if order == 0:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        print(arr)
    elif order == 1:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j <= 0 and key >arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        print(arr)
    else:
        print("Invalid order")
    return arr

def Merge_Sorting(arr, order = 0):
    def _merge_sort(list):
        list_length = len(list)

        if list_length == 1:
            return list

        mid_point = list_length // 2

        left_half = _merge_sort(list[:mid_point])
        right_half = _merge_sort(list[mid_point:])

        return _merge(left_half, right_half)
    def _merge(left, right):
        output = []
        i = j = 0
        if order == 0:
            while (i < len(left) and j < len(right)):
                if left[i] <right[j]:
                    output.append(left[i])
                    i +=1
                else:
                    output.append(right[j])
                    j +=1
        else:
            while (i < len(left) and j < len(right)):
                if left[i] >right[j]:
                    output.append(left[i])
                    i +=1
                else:
                    output.append(right[j])
                    j +=1
        output.extend(left[i:])
        output.extend(right[j:])
        return output
    sorted_arr= _merge_sort(arr)
    print(sorted_arr)
    return sorted_arr

# NOTE: Kruskal Algorithm -------------------------------------------------------------------------------------
class Kruskal_Algorithm:
    def __init__(self, wighted_nodes, no_nodes):
        ipt= wighted_nodes
        n =no_nodes
        answer=[]
        ipt = sorted(ipt,key= lambda ipt:ipt[2])
        graph = [-1]*(n+1)
        for u,v,d in ipt:
            self.union(graph,u,v,answer)
        for item in answer:
            print(item)

    def find(self,graph,node):
        if graph[node]<0:
            return node
        else:
            temp = self.find(graph,graph[node])
            graph[node] = temp
            return temp

    def union(self,graph,a,b,answer):
        ta = a
        tb = b
        a = self.find(graph,a)
        b = self.find(graph,b)
        if a==b:
            pass
        else:
            answer.append([ta,tb])
            if graph[a]<graph[b]:
                graph[a]=graph[a]+graph[b]
                graph[b]=a
            else:
                graph[b]= graph[a]+graph[b]
                graph[a]=b

# NOTE: Prims Algorithm ----------------------------------------------------------------------------------------
class P_Node :
    def __init__(self, arg_id) :
        self._id = arg_id

class Prims :

    def __init__(self, source : int, adj_list : Dict[int, List[int]]) :
        self.source = source
        self.adjlist = adj_list

    def PrimsMST (self) -> int :
        priority_queue = { P_Node(self.source) : 0 }
        added = [False] * len(self.adjlist)
        min_span_tree_cost = 0

        while priority_queue :
            # Choose the adjacent node with the least edge cost
            node = min (priority_queue, key=priority_queue.get)
            cost = priority_queue[node]

            # Remove the node from the priority queue
            del priority_queue[node]

            if added[node._id] == False :
                min_span_tree_cost += cost
                added[node._id] = True
                print("Added Node : " + str(node._id) + ", Distance : "+str(min_span_tree_cost))

                for item in self.adjlist[node._id] :
                    adjnode = item[0]
                    adjcost = item[1]
                    if added[adjnode] == False :
                        priority_queue[P_Node(adjnode)] = adjcost

        return min_span_tree_cost


# NOTE: Dijkstra's Algorithm -----------------------------------------------------------------------------------
class Dijkstras:
    def dijkstra(self,G, start, goal):
        """ Uniform-cost search / dijkstra """
        visited = set()
        cost = {start: 0}
        parent = {start: None}
        todo = PriorityQueue()

        todo.put((0, start))
        while todo:
            while not todo.empty():
                _, vertex = todo.get() # finds lowest cost vertex
                # loop until we get a fresh vertex
                if vertex not in visited: break
            else: # if todo ran out
                break # quit main loop
            visited.add(vertex)
            if vertex == goal:
                break
            for neighbor, distance in G[vertex]:
                if neighbor in visited: continue # skip these to save time
                old_cost = cost.get(neighbor, float('inf')) # default to infinity
                new_cost = cost[vertex] + distance
                if new_cost < old_cost:
                    todo.put((new_cost, neighbor))
                    cost[neighbor] = new_cost
                    parent[neighbor] = vertex
        return parent

    def make_path(self,parent, goal):
        if goal not in parent:
            return None
        v = goal
        path = []
        while v is not None: # root has null parent
            path.append(v)
            v = parent[v]
        return path[::-1]
