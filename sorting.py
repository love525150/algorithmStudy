# -*- coding: utf-8 -*-

'''
算法逻辑：找出列表里最小的元素，然后与列表里第一个位置的元素交互位置，如此重复换到第二个位置，直到所有位置的元素确定
'''
def selection_sort(sorting_list):

    for i in range(len(sorting_list)):
        min_element_index = i
        min_element = sorting_list[i]

        for j in range(i+1, len(sorting_list)):
            if sorting_list[j] < min_element:
                min_element_index = j
                min_element = sorting_list[j]
        
        _switch_list_value(sorting_list, i, min_element_index)


def _switch_list_value(list_, p1, p2):
    temp = list_[p1]
    list_[p1] = list_[p2]
    list_[p2] = temp

'''
这个是比较交换的方式排序（其实类似反向冒泡排序）
'''
def insertion_sort(sorting_list):
    for i in range(len(sorting_list)):

        for j in range(i, 0, -1):
            if sorting_list[j] < sorting_list[j - 1]:
                _switch_list_value(sorting_list, j, j-1)
            else :
                break

'''
这个是真按照洗牌的方式插入排序
'''
def insert_sort_improved_version(sorting_list):
    for i in range(len(sorting_list)):
        source_position = i
        target_position = i
        current_element = sorting_list[i]
        
        for j in range(i, 0, -1):
            last_sorted_element = sorting_list[j - 1]
            last_sorted_element_index = j - 1
            if current_element < last_sorted_element:
                target_position = last_sorted_element_index
            else :
                break

        _insert_list_value(sorting_list, source_position, target_position)    
                

def _insert_list_value(_list, source_position, target_position):
    assert source_position >= target_position, "数组元素只允许从后往前插"
    insert_element = _list[source_position]
    
    for i in range(source_position, target_position, -1):
        _list[i] = _list[i - 1]
    
    _list[target_position] = insert_element

'''
算法逻辑：不断进行前后两两比较，位置不对则进行交换，每遍历一次可以排到一个最大的到元素到末尾
'''
def bubble_sort(sorting_list):
    for i in range(0, len(sorting_list) - 1):
        sorted = True
        
        for j in range (0, len(sorting_list) - 1 - i):
            if sorting_list[j] > sorting_list[j + 1]:
                _switch_list_value(sorting_list, j, j + 1)
                sorted = False
        
        if sorted: break


def test_sort():
    # selection_sort_test_list = [4,66,74,25]
    # selection_sort(selection_sort_test_list)
    # print("selection sort排序结果：" + str(selection_sort_test_list))

    # insertion_sort_test_list = [4,66,74,25,125,908,456,9,36]
    # insert_sort_improved_version(insertion_sort_test_list)
    # print("selection sort排序结果：" + str(insertion_sort_test_list))

    bubble_sort_test_list = [4,66,74,25,125,908,456,9,36]
    bubble_sort(bubble_sort_test_list)
    print("selection sort排序结果：" + str(bubble_sort_test_list))


test_sort()
print('finish')
