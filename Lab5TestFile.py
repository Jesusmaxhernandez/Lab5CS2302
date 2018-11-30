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


from HeapSort import HeapSort

hs = HeapSort()

def main():
    #Hard coded  numebrs
    test = [12,3,19, 4, 11, 1 , 2, 5]
    test2 = [12,3,19, 4, 11, 1 , 2, 5, 19,3,29, 49, 101, 15 , 22, 56, 1]
    
    print("Hardcoded Array before being put into Heap:")
    print(test)
    print("Hardcoded Array put into Heap:")
    hs.makeHeap(test)
    #print(test)
    print()
    print("Hardcoded Array sorted using Heapsort")
    hs.heap_sort(test)
    print(test)
    
    print()
    
    print("Hardcoded Array 2 before being put into Heap:")
    print(test2)
    print("Hardcoded Array 2 put into Heap:")
    hs.makeHeap(test2)
    #print(test)
    print()
    print("Hardcoded Array 2 sorted using Heapsort")
    hs.heap_sort(test2)
    print(test2)

main()

