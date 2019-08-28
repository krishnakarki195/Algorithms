"""
author: Krishna Karki
created date: 8/28/2019
description: written in python
"""

def merge(left, right, merged_list):
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

def merge_sort(input_list):
	if len(input_list) <= 1:
		return input_list
	mid = len(input_list) // 2
	left,right = merge_sort(input_list[:mid]),merge_sort(input_list[mid:])
	return merge(left,right,input_list[:])
