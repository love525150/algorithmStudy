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

def test_sort():
    selection_sort_test_list = [4,66,74,25]
    selection_sort(selection_sort_test_list)
    print("selection sort排序结果：" + str(selection_sort_test_list))


test_sort()
print('finish')