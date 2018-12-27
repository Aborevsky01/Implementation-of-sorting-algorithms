# Implementation-of-sorting-algorithms
***
## Introduction 

### What is a Sorting Algorithm? 
***
 It is a final combination of several instructions, describing a process for rearranging list elements according to a comparison operator. The latter I used to set the new order within the data structure. For example, in this particular investigation the final lists will include only non decreasing  order. 
Despite the sorting of information occurred a long time ago, it is essential even nowadays, as long as it provides us with an ability to rearrange the data structures in the way we want. The amount of information flows expands rapidly, so it is necessary to sort them all, in order to make the work with data more convenient, less time consuming and the knowledge more understandable and open for public.

### Real-life applications

  **Commercial computing.**
  
  Government organizations, financial institutions, and commercial enterprises organize much of this information by sorting it. 
                
  **Search for information.** 
  
  Keeping data in sorted order makes it possible to efficiently search through it using the classic binary search algorithm. 
                
  **Different characteristics of sorting.** 
  
  User can change the comparison element, in order to change the sequence (e.g from A-Z, price, date, etc.)

### Most renown Sorting algorithms 

   #### 1. Bubble sort
 ##### Description 
Algorithms consists of repeating cycles along the sorted massive. Every cycle, elements are consequently compared with each other, and, if the order in the pair is not ascending (and, consequently, false), the change of elements is held. The algorithm makes N-1 repetitions, as long as we can accomplish at least on change. During every inner cycle, next biggest element of the massive is put on its place, and the lowest is moved one position back towards to the beginning of the massive.
 
Performance
Worst case: O(n^2) comparisons and O(n^2)  swaps - Perfectly Descending sequence 
Best case: O(n) comparisons and O(1) swaps - Perfectly ascending order
Implementation 
Mostly perceived as impractical, so the only implementation is in studying course before more complex sorting algorithms.
Visualization of works

   ##### 2. Insertion sort
 ##### Descriptiom
Given algorithm consists of consequent cycles along the sorted massive. On each step, one of the massive’s elements is taken, and then its correct position is being found. Lastly, we insert the particular element on its place. After that, we continue to repeat this operation until the entire massive becomes perfectly ascending
Time of working:
Worst case: O(n^2) comparisons and O(n^2) swaps
Best case: O(n) comparisons and O(1) swaps 
Implementation: 
Sorting small massive (up to 10 elements), where it is the most efficient 
A part of several other sorting algorithms, such as Timsort.
Visualization of work:
Quick sort
   Definition
Current algorithm of quick sort is composed out of several simple steps: pivot element, division of the massive into 3 mini-massives, and implementation of recursive algorithm to those mini-massives. It has to be underscored, that, in the first acquired mini-massive, there are only those elements, which are smaller than pivot; in the second only equal to the pivot; in the third - greater than pivot.
Created by:
Year: 
Time of working:
Worst case: O(n^2) - the pivot is either the greatest or the lowest element in massi
Best and Average case: O(nlogn) 
Implementation:
 Mainly, it is used in overwhelming majority of cases, when the huge volumes of data have to be sorted.
Visualization of work:

Classification criteria of sorting algorithms 
Computational complexity 
Definition 
This classification is usually considered the most important. Usually, the worst, average, and best time of the sorting algorithm is estimated, where the best stands for minimal time of the algorithm, accomplishing the sequence from 1 to n in perfectly ascending order. In the same time, the worst time is the greatest time.

Memory usage 
Definition
Memory is an additionally requested costs, depending on the size of the massive


Adaptivity
Definition 
Efficiency of the method when processing already sorted or partially sorted data.

Stability
Definition 
Stable sorting does not change relative sequence of elements, being sorted, if they have the same values.


Serial/parallel 
Definition 
Ability to distribute recursive calls to multiple threads of program execution

Language of Programming: Python

Why this language? 
Python is a high-level programming language with simple and comprehensible syntax. It perfectly suits for learning basics of programming and Computer Science.

Why sorting?
Problems of sorting are the fundamental tasks in Computer Science. Therefore, studying and implementing major algorithms of sorting allows to develop algorithmic thinking and improve programming skills.

Method 
I have:
 Chosen three renown ways of sorting (Bubble, Insertion, Quick)
 Scrutinized the way the work through VisuAlgo
 Created codes for each of the sorting algorithms 
 Tested if they work correctly 
 Written a code to generate a document, in which there would have to be three kinds of sequences (Unordered - the reverse order, descending, Ordered, Random) with different cardinality (10,100,1000,10 000, 100 000)
 Added timer code to all three algorithms 
Conducted several testings, measuring the time of algorithms‘ processing in different “mediums”
Plotted the graphs, built on the data gathered.
<img src='https://github.com/Aborevsky01/Implementation-of-sorting-algorithms/blob/master/ordered.png' style='width: 50%; height: auto;'/>
![](https://github.com/Aborevsky01/Implementation-of-sorting-algorithms/blob/master/ordered.png =250x)
