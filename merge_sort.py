"""
author: Krishna Karki
created date: 8/28/2019
description: written in python
"""

class MergeSort(object):
	def merge_sort(self, input_list):
		if len(input_list) <= 1:
			return input_list
		mid = len(input_list) // 2
		left, right = self.merge_sort(input_list[:mid]), self.merge_sort(input_list[mid:])
		return self.merge(left,right,input_list[:])
	
	def merge(self, left, right, merged_list):
		left_cursor,right_cursor = 0,0
		while left_cursor < len(left) and right_cursor < len(right):
			if left[left_cursor] <= right[right_cursor]:
				merged_list[left_cursor+right_cursor] = left[left_cursor]
				left_cursor += 1
			else:
				merged_list[left_cursor+right_cursor] = right[right_cursor]
				right_cursor += 1
		while left_cursor < len(left):
			merged_list[left_cursor+right_cursor] = left[left_cursor]
			left_cursor += 1
		while right_cursor < len(right):
			merged_list[left_cursor+right_cursor] = right[right_cursor]
			right_cursor += 1
		return merged_list

my_obj = MergeSort()
my_list = [2,4,5,2,1,7,8,9,5,6]
print("Befor sorting: ", my_list)
my_list = my_obj.merge_sort(my_list)
print("After sorting: ", my_list)
