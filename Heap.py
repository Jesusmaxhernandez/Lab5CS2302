#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:31:37 2018

@author: JesusMHernandez
"""

class Heap:
    
    def __init__(self):
        self.heap_array = []
    def insert(self, k):
        """
        Method to insert into the Heap 
        """
        self.heap_array.append(k)
        self.up_heap()
        
    def up_heap(self):
        """
        Gets new items and places them into Heap
        """
        newItem = len(self.heap_array) - 1 #gets index of new Item 
              
        while(self.heap_array[newItem] < self.heap_array[(newItem - 1)//2]):
            parent = ((newItem - 1)//2)
            
            temp = self.heap_array[newItem]
            self.heap_array[newItem] = self.heap_array[(newItem - 1)//2]
            self.heap_array[(newItem - 1)//2] = self.heap_array[newItem]
            
            newItem = parent
            
    def down_heap(self):
        """
        Gets items in the front and swaps them until valid Heap
        """
        
        
        
    #TODO: Complete implentation
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array.append[0]
        return min_elem
    
    def is_empty(self):
        return len(self.heap_array) == 0
    
def heap_sort(lst):
    heap = Heap()
    result = [] 
    for elem in lst:
        heap.insert(elem)
    while not heap.is_empty():
        result.append(heap.extract_min())
    return result
