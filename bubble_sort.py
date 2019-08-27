"""
author: Krishna Karki
Created date: 8/27/2019
description: written in python
"""

def bubble_sort(input_list):
	for i in range(0,len(input_list)):
		for j in range(i,len(input_list)):
			if input_list[i] > input_list[j]:
				input_list[i], input_list[j] = input_list[j], input_list[i]
	return input_list


