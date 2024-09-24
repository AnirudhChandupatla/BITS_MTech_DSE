class Chocolate:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __str__(self):
        return str.format("name: {}, count: {}", self.name, self.count)

with open('inputPS03.txt','r') as f:
    lines = f.read()

line1,line2 = lines.split('\n')
Chocolate_names_str , Chocolate_counts_str = line1[len('Chocolate:'):].split('Number:')
Chocolate_names = Chocolate_names_str.replace(' ','').split('/')
Chocolate_counts = list(map(int, Chocolate_counts_str.replace(' ','').split('/')))

order = line2.split(':')[1].lower().replace(' ','')

input_array = []

for name,count in zip(Chocolate_names,Chocolate_counts):
    input_array.append(Chocolate(name,count))
div_conq_array = input_array.copy()
iter_array = input_array.copy()
linear_array = input_array.copy()

def merge(array, left_index, middle , right_index, comparator):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]
    len_left_copy = len(left_copy)
    len_right_copy = len(right_copy)
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len_left_copy and right_copy_index < len_right_copy:
        if comparator(left_copy[left_copy_index], right_copy[right_copy_index]):
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1

        sorted_index += 1

    while left_copy_index < len_left_copy:
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1

    while right_copy_index < len_right_copy:
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1

#divide and conquer
def merge_sort_divide_and_conquer(array, left_index, right_index, comparator):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort_divide_and_conquer(array, left_index, middle, comparator)
    merge_sort_divide_and_conquer(array, middle + 1, right_index, comparator)
    merge(array, left_index, middle, right_index , comparator)

#non-recursive or iterative 
def merge_sort_iterative(array,comparator):
    width = 1   
    n = len(array)                         
    while (width < n):
        left_index=0
        while (left_index < n):
            right_index = min(left_index+(width*2-1), n-1)        
            middle = min(left_index+width-1,n-1)     
            merge(array, left_index, middle, right_index, comparator)
            left_index += width*2
        width *= 2

if order == 'lowtohigh':
    merge_sort_divide_and_conquer(div_conq_array, 0, len(div_conq_array) -1, lambda ChocolateA, ChocolateB: ChocolateA.count < ChocolateB.count)
elif order == 'hightolow':
    merge_sort_divide_and_conquer(div_conq_array, 0, len(div_conq_array) -1, lambda ChocolateA, ChocolateB: ChocolateA.count > ChocolateB.count)

dqchoco_names = []
dqchoco_count = []
for choco in div_conq_array:
    dqchoco_names.append(choco.name)
    dqchoco_count.append(str(choco.count))



if order == 'lowtohigh':
    merge_sort_iterative(iter_array, lambda ChocolateA, ChocolateB: ChocolateA.count < ChocolateB.count)
elif order == 'hightolow':
    merge_sort_iterative(iter_array, lambda ChocolateA, ChocolateB: ChocolateA.count > ChocolateB.count)

itchoco_names = []
itchoco_count = []
for choco in iter_array:
    itchoco_names.append(choco.name)
    itchoco_count.append(str(choco.count))

import sys
with open('outputPS03.txt', 'w') as f:
    sys.stdout = f
    print('Divide & Conquer:')
    print('Chocolate: ','/'.join(dqchoco_names),'Number: ','/'.join(dqchoco_count))
    print()
    print('Iterative Solution:')
    print('Chocolate: ','/'.join(itchoco_names),'Number: ','/'.join(itchoco_count))


def check_order(order):
    return True if order == 'hightolow' else False

def countingSortForRadix(inputArray, placeValue,order):
    countArray = [0] * 10
    inputSize = len(inputArray)

    for i in range(inputSize): 
        placeElement = (inputArray[i].count // placeValue) % 10
        if check_order(order) : placeElement = 9 - placeElement
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i].count // placeValue) % 10
        if check_order(order) : placeElement = 9 - placeElement
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1
        
    return outputArray

#linear-time
def radixSort(inputArray,order):
    maxEl = -1
    for choco in inputArray:
        if maxEl < choco.count:
            maxEl = choco.count

    D = 1
    while maxEl > 0:
        maxEl //= 10
        D += 1
    
    placeVal = 1
    outputArray = inputArray
    while D > 0:
        outputArray = countingSortForRadix(outputArray, placeVal,order)
        placeVal *= 10  
        D -= 1

    return outputArray

choco_names = []
choco_count = []
for choco in radixSort(linear_array,order):
    choco_names.append(choco.name)
    choco_count.append(str(choco.count))

# print()
# print('Linear-time:')
# print('Chocolate: ','/'.join(choco_names),'Number: ','/'.join(choco_count))