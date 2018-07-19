# -*- coding: utf-8 -*-


def selection_sort(sorting_list):
    """算法逻辑：找出列表里最小的元素，然后与列表里第一个位置的元素交互位置，如此重复换到第二个位置，直到所有位置的元素确定"""

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


def insertion_sort(sorting_list):
    """这个是比较交换的方式排序（其实类似反向冒泡排序）"""

    for i in range(len(sorting_list)):

        for j in range(i, 0, -1):
            if sorting_list[j] < sorting_list[j - 1]:
                _switch_list_value(sorting_list, j, j-1)
            else:
                break


def insert_sort_improved_version(sorting_list):
    """这个是真按照洗牌的方式插入排序"""

    for i in range(len(sorting_list)):
        source_position = i
        target_position = i
        current_element = sorting_list[i]

        for j in range(i, 0, -1):
            last_sort_flag_element = sorting_list[j - 1]
            last_sort_flag_element_index = j - 1
            if current_element < last_sort_flag_element:
                target_position = last_sort_flag_element_index
            else:
                break

        _insert_list_value(sorting_list, source_position, target_position)


def _insert_list_value(_list, source_position, target_position):
    assert source_position >= target_position, "数组元素只允许从后往前插"
    insert_element = _list[source_position]

    for i in range(source_position, target_position, -1):
        _list[i] = _list[i - 1]

    _list[target_position] = insert_element


def bubble_sort(sorting_list):
    """算法逻辑：不断进行前后两两比较，位置不对则进行交换，每遍历一次可以排到一个最大的到元素到末尾"""
    for i in range(0, len(sorting_list) - 1):
        sort_flag = True

        for j in range(0, len(sorting_list) - 1 - i):
            if sorting_list[j] > sorting_list[j + 1]:
                _switch_list_value(sorting_list, j, j + 1)
                sort_flag = False

        if sort_flag:
            break


def merge_sort(sorting_list):
    """归并排序"""
    sort_result = _recrusive_merge_sort(sorting_list, 0, len(sorting_list))
    for i in range(0, len(sorting_list)):
        sorting_list[i] = sort_result[i]


def _recrusive_merge_sort(list_, left, right):
    if left < right:
        mid = int((left + right) / 2)
        llist = _recrusive_merge_sort(list_, left, mid)
        rlist = _recrusive_merge_sort(list_, mid + 1, right)
        return _merge(llist, rlist)

    else:
        return list_[left: left+1]


def _merge(list1, list2):
    index1 = 0
    index2 = 0
    temp_list = []
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            temp_list.append(list1[index1])
            index1 += 1
        else:
            temp_list.append(list2[index2])
            index2 += 1

    if index1 < len(list1):
        temp_list.extend(list1[index1: len(list1)])

    if index2 < len(list2):
        temp_list.extend(list2[index2: len(list2)])

    return temp_list


def quick_sort(sorting_list):
    """快速排序"""
    _recrusive_quick_sort(sorting_list, 0, len(sorting_list) - 1)


def _recrusive_quick_sort(sorting_list, left, right):
    if left == right:
        return
    
    partition_index = _partition(sorting_list, left, right)
    
    _recrusive_quick_sort(sorting_list, left, partition_index - 1)
    _recrusive_quick_sort(sorting_list, partition_index, right)


def _partition(sorting_list, left, right):
    """快速排序的核心，
    通过一次scan将数组分成两部分，前半部分都是小于等于基值（数组第一个元素）的元素，后半部分都是大于等于基值的元素，
    返回值是后半部分第一个元素的索引值（切分位置，用于后面递归调用partition）
    """
    base = sorting_list[left]
    left_scan = left + 1
    right_scan = right
    while True:
        while left_scan < right_scan:
            if sorting_list[left_scan] > base:
                break
            else:
                left_scan += 1

        while right_scan > left_scan:
            if sorting_list[right_scan] < base:
                break
            else:
                right_scan -= 1

        if left_scan == right_scan:
            if base > sorting_list[left_scan]:
                _switch_list_value(sorting_list, left, left_scan)
            break
        else:
            _switch_list_value(sorting_list, left_scan, right_scan)
    
    return left_scan


def test_sort():
    # selection_sort_test_list = [4,66,74,25]
    # selection_sort(selection_sort_test_list)
    # print("selection sort排序结果：" + str(selection_sort_test_list))

    # insertion_sort_test_list = [4,66,74,25,125,908,456,9,36]
    # insert_sort_improved_version(insertion_sort_test_list)
    # print("插入排序结果：" + str(insertion_sort_test_list))

    # bubble_sort_test_list = [4,66,74,25,125,908,456,9,36]
    # bubble_sort(bubble_sort_test_list)
    # print("冒泡排序结果：" + str(bubble_sort_test_list))

    # merge_sort_test_list = [4, 66, 74, 25, 125, 908, 456, 9, 36]
    # merge_sort(merge_sort_test_list)
    # print("归并排序结果：" + str(merge_sort_test_list))

    quick_sort_test_list = [4, 66, 74, 25, 125, 908, 456, 9, 36]
    quick_sort(quick_sort_test_list)
    print("快速排序结果：" + str(quick_sort_test_list))


test_sort()
print('finish')
