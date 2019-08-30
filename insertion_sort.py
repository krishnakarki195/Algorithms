"""
author: Krishna Karki
created date: 8/27/2019
description: insertion sort written in python
"""

class InsertionSort(object):
	def insertion_sort(self, input_list):
		for i in range(0,len(input_list)):
			cursor = input_list[i]
			position = i
			while position > 0 and input_list[position-1] > cursor:
				input_list[position] = input_list[position-1]
				position  = position - 1
			input_list[position] = cursor
		return input_list

	
my_obj = InsertionSort()
my_list = [2,4,5,2,1,7,8,9,5,6]
print("Befor sorting: ", my_list)
my_list = my_obj.insertion_sort(my_list)
print("After sorting: ", my_list)
