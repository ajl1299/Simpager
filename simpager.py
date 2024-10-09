""" 
Austin Lee
Operating Systems CSC360
Project 6 simpager
Due April 3rd, 2024
Dr Siming Liu

"""

""" 
 Usage example to run program with input file 'testcase1.txt' :
 
 " python3 simpager.py < testcase1.txt "
 
"""

import sys  #redirect operator usage
import random #RAND algorithm
from collections import deque  #LRU algorithm

""" 
First In First Out

This function iterates through the list of page references with a given number of frames and uses a FIFO
replacement algorithm. The Function simply kicks out the oldest index and appends the newest index when
the frames become full

Return value
-----            number of page faults
int

Params
-----
pageReference    array of ints    simulates page references in memory
numberFrames     int              specifies how many frames our simulation has in memory to handle the page references

"""
def fifo(pageReference, numberFrames):
    frames = []            #initialize 
    page_faults = 0
    
    for page in pageReference:
        if page not in frames:
            if len(frames) < numberFrames: #if empty frames, add page to frame
                frames.append(page)
            else:
                frames.pop(0)          #remove oldest frame
                frames.append(page)
            page_faults += 1
    
    return page_faults

""" 
Least Recently Used

This function iterates through the list of page references with a given number of frames and uses an LRU
replacement algorithm. The function uses a double ended queue to kick out whichever element is least recently used.
When an element is used it is added to the end of the queue.

Return value
-----            number of page faults
int

Params
-----
pageReference    array of ints    simulates page references in memory
numberFrames     int              specifies how many frames our simulation has in memory to handle the page references

"""
def lru(pageReference, numberFrames):
    frames = deque()
    page_faults = 0
    
    for page in pageReference:
        if page not in frames:
            if len(frames) < numberFrames: #if empty frames, add page to frame
                frames.append(page)
            else:
                frames.popleft()  #kick out least recently used
                frames.append(page)  #add new page to frame
            page_faults += 1
        else:
            frames.remove(page)  
            frames.append(page)  #move page to the end to mark as most recently used
    
    return page_faults

""" 
Optimal

This function iterates through the list of page references with a given number of frames and uses an Optimal
replacement algorithm. When the frames are full, the function searches through the array of page references and
finds the page that will be needed furthest in the future, then replaces the frame containing that page. I used
another double ended queue to kick out the specified page that needs replaced and append the current page.

Return value
-----            number of page faults
int

Params
-----
pageReference    array of ints    simulates page references in memory
numberFrames     int              specifies how many frames our simulation has in memory to handle the page references

"""
def optimal(pageReference, numberFrames):
    frames = deque()
    page_faults = 0
    
    for page in pageReference:
        if page not in frames:
            if len(frames) < numberFrames:  #if empty frames, add page to frame
                frames.append(page)
            else:
                max_distance = -1
                page_to_replace = None         
                for frame in frames:
                    if pageReference.index(frame) > max_distance: 
                        max_distance = pageReference.index(frame)    #find page that appears furthest in the future
                        page_to_replace = frame                         
                frames.remove(page_to_replace)       #remove it
                frames.append(page)                  #add current page
            page_faults += 1
    
    return page_faults

""" 
Random

This function iterates through the list of page references with a given number of frames and uses the random function
to randomly select a frame to replace in memory.

Return value
-----            number of page faults
int

Params
-----
pageReference    array of ints    simulates page references in memory
numberFrames     int              specifies how many frames our simulation has in memory to handle the page references

"""
def rand(pageReference, numberFrames):
    frames = []
    page_faults = 0
    
    for page in pageReference:
        if page not in frames:
            if len(frames) < numberFrames:  #if empty frames, add page to frame
                frames.append(page)
            else:
                frames[random.randint(0, numberFrames - 1)] = page  #replace random frame
            page_faults += 1
            
    return page_faults

def main():
    pageReference = list(map(int, input().split())) #grab inputs
    numberFrames = int(input().strip())
    algos = ["FIFO", "LRU", "OPT", "RAND"]
    
    print("Page Reference String:")
    print(" ".join(map(str, pageReference)))
    
    print("Number of Frames:", numberFrames)
    
    
    for line in sys.stdin:          #output according to input
        algo = line.strip()
        
        if algo in algos:
            print(algo + ":", end=" ")
            if algo == "FIFO":
                print(fifo(pageReference, numberFrames))
            elif algo == "LRU":
                print(lru(pageReference, numberFrames))
            elif algo == "OPT":
                print(optimal(pageReference, numberFrames))
            elif algo == "RAND":
                print(rand(pageReference, numberFrames))


if __name__ == "__main__":
    main()
    
    
            
