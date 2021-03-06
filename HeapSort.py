#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Jesus Maximino Hernandez
CS 2302 Data Structures - Diego Aguirre
TA - Manoj Saha
Lab 5 - Option A 
Program that implements a min Heap and runs heapsort on an Array

@author: JesusMHernandez
"""
from Lab5 import Heap 

h = Heap()
class HeapSort():
    

    def makeHeap(self, lst):
        """
        makes a valid heap out of given numbers
        """
        for i in range(len(lst)):
            h.insert(lst[i])
            
        h.print_lst()
        

    def down_heap(self, node_index, heap_lst, lst_size):
        """
        Gets items in the front and swaps them until valid Heap
        """
        child_index = 2 * node_index + 1
        value = heap_lst[node_index]
        while child_index < lst_size:
            # Find the max among the node and all the node's children
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < lst_size:
                if heap_lst[i + child_index] > max_value:
                    max_value = heap_lst[i + child_index]
                    max_index = i + child_index
                i = i + 1
                                        
            if max_value == value:
                return
    
            # Swap heap_list[node_index] and heap_list[max_index]
            temp = heap_lst[node_index]
            heap_lst[node_index] = heap_lst[max_index]
            heap_lst[max_index] = temp
            
            node_index = max_index
            child_index = 2 * node_index + 1
    
    

    def heap_sort(self, lst):
        """
        Swaps the first and last elements on heap array to sort then uses
        down heap to keep vaid heap 
        """
        # Heapify 
        i = len(lst) // 2 - 1
        while i >= 0:
            self.down_heap(i, lst, len(lst))
            i = i - 1
                    
        i = len(lst) - 1
        while i > 0:
            # Swap function
            temp = lst[0]
            lst[0] = lst[i]
            lst[i] = temp
    
            self.down_heap(0, lst, i)
            i = i - 1
