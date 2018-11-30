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
              
        while(self.heap_array[newItem] < self.heap_array[(newItem - 1)//2] and newItem >0):
            parent = ((newItem - 1)//2)
            
            temp = self.heap_array[newItem]
            self.heap_array[newItem] = self.heap_array[(newItem - 1)//2]
            self.heap_array[(newItem - 1)//2] = temp
            
            newItem = parent
               
    def extract_min(self):
        """
        Extract minimum from Heap
        """
        if self.is_empty():
            return None
        min_elem = self.heap_array.pop(0)
        
        return min_elem
    
    def is_empty(self):
        
        return len(self.heap_array) == 0
    
    def print_lst(self):
        """
        Prints the heap 
        """
        list1 = []
        for item in self.heap_array:
            print(item, end='' + " ")

    

