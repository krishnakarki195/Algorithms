"""
author: Krishna Karki
created date: 8/27/2019
description: written in python
"""

def insertion_sort(input_list):
	for i in range(0,len(input_list)):
		cursor = input_list[i]
		position = i
		while position > 0 and input_list[position-1] > cursor:
			input_list[position] = input_list[position-1]
			position  = position - 1
		input_list[position] = cursor
	return input_list


