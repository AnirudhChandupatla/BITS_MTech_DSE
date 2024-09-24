with open('inputPS9.txt','r') as f : words = f.read().replace(' ','').split('\n')

special_chars = ['^', '$', '#', '@', '!', \
                 '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', \
                 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', \
                 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

char_priority_list = [-1]*125
for k,v in enumerate(special_chars): char_priority_list[ord(v)] = k

class Node:
    '''
    data : stores string word
	count : stores number of occurrences of duplicate words
	left : maintains reference to left node/subtree
	right : maintains reference to right node/subtree 
	length: counts the length of Word while creating Node object , O(w) where w is length of word
    '''
    data = None
    count = None
    left = None
    right = None

    def __init__(self, data) -> None:
        self.data = data
        self.count = 1
        self.length = len(data)

    def less_priority_than(self, against) -> int:
        '''
        compares character by character priority between self.data and word to be compared by passing it as a parameter to this function. 
		If less priority returns 0 else 1
		if shortest word is part of other and has less or same priority for common part then we will check priority based on length.
        has time complexity as O(L), where L is length of largest word
        '''
        i = 0
        while True:
            try:
                c1 = self.data[i]
                c2 = against[i]
                if c1 != c2: return 0 if char_priority_list[ord(c1)] < char_priority_list[ord(c2)] else 1
            except IndexError:
                break
            i += 1
        return -1 if self.length == len(against) else 0 if self.length > len(against) else 1

def insert(track, node):
    '''
    gets priority using  less_priority_than method if more priority then insert into right subtree recursively else insert into left subtree recursively.
    If the word is already (checked by method less_priority_than returning -1) in BST then it increments the ‘count’ attribute of Node
    Insert has time complexity is O(h), where ‘h’ is height of the BST
    '''
    priority = track.less_priority_than(node.data)
    if priority == 1:
        if track.right != None:
            insert(track.right, node)
        else:
            track.right = node
    elif priority == 0:
        if track.left != None:
            insert(track.left, node)
        else:
            track.left = node
    else: track.count += 1

#O(N)
def inorder_traversal_des(track,level = 0, length = None, dup = None):
    '''
    here we visit each node in BST I.e by processing right subtree first then print the current node data finally processing left subtree to print word from highest priority to lowest priority.
    since we are anyhow visiting each and every node once, doing two additional checks
	    Duplicates
	    Largest Word
    Duplicates, are checked by using the ‘count’  which was populated while inserting into BST itself. If count>1 then mark it as duplicate.
    Largest Word, is find by comparing length attribute of node object which was created during object creation and mark it as largest.
    Display Duplicates and Largest Word in next step respectively.
    Overall time complexity is O(h) 
    '''
    global largest_string_length
    largest_string_length = -1 if length == None else length
    global largest_string_level
    global duplicates
    duplicates = [] if dup == None else dup
    if track == None: return
    inorder_traversal_des(track.right, level + 1,largest_string_length,duplicates)
    print('\n'.join([track.data for i in range(track.count)]))
    if track.length > largest_string_length :
        largest_string_length = track.length
        largest_string_level = level
    if track.count > 1:
        duplicates.append({'data':track.data,'count':track.count,'level':level})
    inorder_traversal_des(track.left, level + 1,largest_string_length,duplicates)

#O(N)
def preorder_traversal_des(track):
    '''
    here we visit each node in BST by printing out current node data first then processing left subtree and finally processing right subtree
    '''
    if track == None: return
    print('\n'.join([track.data for i in range(track.count)]))
    preorder_traversal_des(track.left)
    preorder_traversal_des(track.right)


def find(track, data):
    if track == None: return "Not in Tree"
    if track.data == data: return track
    else:
        priority = track.less_priority_than(data)
        return find(track.right, data) if priority == 1 else find(track.left, data)

def findMax(root):
    if root.left == None and root.right == None:
        return  root
    elif root.right != None:
        return findMax(root.right)
    return findMax(root.left)

def delete(root,data):
    if root == None: return root
    prt = root.less_priority_than(data)
    if prt == 0 :
        root.left = delete(root.left,data)
    elif prt == 1:
        root.right = delete(root.right,data)
    else:
        if root.left == None and root.right == None:
            if root.count > 1: root.count -= 1
            else: root = None
        elif root.left == None:
            root = root.right
        elif root.right == None:
            root = root.left
        else:
            root = findMax(root.left)
    return root

import sys
words = [word for word in words if len(word) > 0]
if __name__ == '__main__':
    if len(words) == 0 : sys.exit()
    root = Node(words[0])
    for word in words[1:]: insert(root, Node(word))
    f = open('outputPS9.txt', 'w')
    sys.stdout = f
    len_words = {}
    len_words_len = 0
    print('These are the total of {} nodes in the tree with character count of each node as'.format(len(words)))
    for word in words:
        found = find(root, word)
        if not isinstance(found, str):
            print('{} -- {} characters'.format(found.data, found.length))
            if found.length in len_words.keys(): len_words[found.length].append(found.data)
            else:
                len_words[found.length] = [found.data]
                len_words_len += 1
        else: print(found)

    print('\nThere are total of ',end='')
    flg = 0
    for count in len_words.keys():
        n_nodes = len(len_words[count])
        if n_nodes > 1:
            print(('' if flg == 0 else ' and\n') +'{} nodes with same string count as {}'.format(n_nodes,count))
            flg2 = 1
            for word in len_words[count]:
                print(('' if flg2 == 1 else '\n') +'{} -- {} characters'.format(word,count) ,end= '')
                flg2 = 2
            flg = 1

    print('\nList of input words based on the order of priority (highest to least)…')
    inorder_traversal_des(root)

    print('\nLargest string in all the nodes is with {} as string count and it is at level {} in the BST structure…'.format(largest_string_length,largest_string_level))

    print('\nDuplicate input string in all the nodes are ')
    for dup in duplicates:
        print('"{}" repeated for {} time which is at level {} in the BST'.format(dup['data'],dup['count'],dup['level']))

    print('\nPreorder traversal of the BST is')
    preorder_traversal_des(root)
    f.close()
