"""
author: Krishna Karki
Created date: 8/27/2019
description: written in python
"""

def selection_sort(input_list):
	for i in range(len(input_list)):
		minimum = i
		for j in range(i+1,len(input_list)):
			if input_list[j] < input_list[minimum]:
				minimum = j
		input_list[minimum], input_list[i] = input_list[i], input_list[minimum]
	return input_list

