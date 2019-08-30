"""
author: Krishna Karki
created date: 8/27/2019
description: written in python
"""

class SelectionSort(object):
	def selection_sort(self, input_list):
		for i in range(len(input_list)):
			minimum = i
			for j in range(i+1,len(input_list)):
				if input_list[j] < input_list[minimum]:
					minimum = j
			input_list[minimum], input_list[i] = input_list[i], input_list[minimum]
		return input_list


my_obj = SelectionSort()
my_list = [2,4,5,2,1,7,8,9,5,6]
print("Befor sorting: ", my_list)
my_list = my_obj.selection_sort(my_list)
print("After sorting: ", my_list)
