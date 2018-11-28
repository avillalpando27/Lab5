#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: Main.py
Name: Angel Villalpando
Date: 11/27/2018
Course: CS 2302 - Data Structures
Description: This file contains the program that turns a list of numbers into a Min Heap and then performs Heap sort by
performing root extraction and pushing in into a final array, where the numbers are sorted in ascending order. 
"""

from HeapClass import Heap

def list_to_heap(list):

    heap = Heap()
    for i in range(len(list)):
        heap.insert(list[i])

    return heap

def main():


    testList = [8, 4, 3, 2, 1, 5, 6, 7, 12, 15, 20, 25]
    print("\n\nThe first, original list is: ", testList)
    testHeap = list_to_heap(testList)

    testList2 = [2, 5, 4, 1, 7, 8, 0, 14, 9, 15]
    print("\nThe second, original listt is: ", testList2)
    testHeap2 = list_to_heap(testList2)

    testList3 = [7, 55, 15, 12, 90, 95, 4, 87, 100, 49]
    print("\nThe third, original list is: ", testList3)
    testHeap3 = list_to_heap(testList3)

    print("\nList 1 turned into MinHeap: ")
    testHeap.print_heap()

    print("\nList 2 turned into MinHeap: ")
    testHeap2.print_heap()

    print("\nList 3 turned into MinHeap: ")
    testHeap3.print_heap()



    print("\nHeapSort for first list: ")
    sorted = testHeap.heapSort()
    print(sorted)

    print("\nHeapSort for second list: ")
    sorted2 = testHeap2.heapSort()
    print(sorted2)

    print("\nHeapSort for second list: ")
    sorted3 = testHeap3.heapSort()
    print(sorted3)



main()