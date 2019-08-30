"""
author: Krishna Karki
created date: 8/27/2019
description: bubble sort written in python
"""

class BubbleSort(object):
	def bubble_sort(self, input_list):
		for i in range(0,len(input_list)):
			for j in range(i,len(input_list)):
				if input_list[i] > input_list[j]:
					input_list[i], input_list[j] = input_list[j], input_list[i]
		return input_list


my_obj = BubbleSort()
my_list = [2,4,5,2,1,7,8,9,5,6]
print("Befor sorting: ", my_list)
my_list = my_obj.bubble_sort(my_list)
print("After sorting: ", my_list)
