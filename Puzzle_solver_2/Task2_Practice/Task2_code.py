import cv2
import numpy

#Teams can add other helper functions
#which can be added here

def puzzle(D1,D2):
    
    #add your code here
        
    return 0

if __name__ == "__main__":
    #code for checking output for single test input
    fo = open("test_inputs/Test_input0.txt", "r")
    D1=[map(int, fo.readline().split())]
    D2=[map(int, fo.readline().split())]
    puzzle (D1,D2)

    #code for checking output for all test inputs
    for file_number in range(0,3):
        file_name = "test_inputs/Test_input"+str(file_number)+".txt"
        fo = open(file_name, "r")
        D1=[map(int, fo.readline().split())]
        D2=[map(int, fo.readline().split())]
        puzzle (D1,D2)
