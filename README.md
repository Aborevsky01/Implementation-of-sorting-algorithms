# Implementation-of-sorting-algorithms
***
## Introduction 

### What is a Sorting Algorithm? 
***
 It is a final combination of several instructions, describing a process for rearranging list elements according to a comparison operator. The latter I used to set the new order within the data structure. For example, in this particular investigation the final lists will include only non decreasing  order. 
Despite the sorting of information occurred a long time ago, it is essential even nowadays, as long as it provides us with an ability to rearrange the data structures in the way we want. The amount of information flows expands rapidly, so it is necessary to sort them all, in order to make the work with data more convenient, less time consuming and the knowledge more understandable and open for public.

### Real-life applications
***
  **Commercial computing.**
  
  Government organizations, financial institutions, and commercial enterprises organize much of this information by sorting it. 
                
  **Search for information.** 
  
  Keeping data in sorted order makes it possible to efficiently search through it using the classic binary search algorithm. 
                
  **Different characteristics of sorting.** 
  
  User can change the comparison element, in order to change the sequence (e.g from A-Z, price, date, etc.)

### Most renown Sorting algorithms 
***
   #### 1. Bubble sort
 ##### Description 
Algorithms consists of repeating cycles along the sorted massive. Every cycle, elements are consequently compared with each other, and, if the order in the pair is not ascending (and, consequently, false), the change of elements is held. The algorithm makes N-1 repetitions, as long as we can accomplish at least on change. During every inner cycle, next biggest element of the massive is put on its place, and the lowest is moved one position back towards to the beginning of the massive.
 
 ##### Performance
###### Worst case: 
O(n^2) comparisons and O(n^2)  swaps - Perfectly Descending sequence 

###### Best case:
O(n) comparisons and O(1) swaps - Perfectly ascending order

 ##### Implementation 
Mostly perceived as impractical, so the only implementation is in studying course before more complex sorting algorithms.
Visualization of works

   #### 2. Insertion sort
 ##### Description
Given algorithm consists of consequent cycles along the sorted massive. On each step, one of the massive’s elements is taken, and then its correct position is being found. Lastly, we insert the particular element on its place. After that, we continue to repeat this operation until the entire massive becomes perfectly ascending

 ##### Perfomance
###### Worst case: 
O(n^2) comparisons and O(n^2) swaps

###### Best case: 
O(n) comparisons and O(1) swaps 

 ##### Implementation
Sorting small massive (up to 10 elements), where it is the most efficient 
A part of several other sorting algorithms, such as Timsort.

   #### Quick sort
 ##### Definition
Current algorithm of quick sort is composed out of several simple steps: pivot element, division of the massive into 3 mini-massives, and implementation of recursive algorithm to those mini-massives. It has to be underscored, that, in the first acquired mini-massive, there are only those elements, which are smaller than pivot; in the second only equal to the pivot; in the third - greater than pivot.

 ##### Perfomance
###### Worst case:
time is approximately equal to O(n^2) - the pivot is either the greatest or the lowest element in massi
###### Best and Average case:
O(nlogn) 

 ##### Implementation
 Mainly, it is used in overwhelming majority of cases, when the huge volumes of data have to be sorted.


### Classification criterias of sorting algorithms 
***
   #### Computational complexity 
##### Definition
This classification is usually considered the most important. Usually, the worst, average, and best time of the sorting algorithm is estimated, where the best stands for minimal time of the algorithm, accomplishing the sequence from 1 to n in perfectly ascending order. In the same time, the worst time is the greatest time.

   #### Memory usage 
##### Definition
Memory is an additionally requested costs, depending on the size of the massive


   #### Adaptivity
##### Definition
Efficiency of the method when processing already sorted or partially sorted data.

   #### Stability
##### Definition
Stable sorting does not change relative sequence of elements, being sorted, if they have the same values.

   #### Serial/parallel 
##### Definition
Ability to distribute recursive calls to multiple threads of program execution

### Language of Programming: Python
***
   #### Why this language? 
Python is a high-level programming language with simple and comprehensible syntax. It perfectly suits for learning basics of programming and Computer Science.

   #### Why sorting?
Problems of sorting are the fundamental tasks in Computer Science. Therefore, studying and implementing major algorithms of sorting allows to develop algorithmic thinking and improve programming skills.

## Method 

We have:
1. Chosen three renown ways of sorting (Bubble, Insertion, Quick)
2. Scrutinized the way they work through VisuAlgo
3. Created codes for each of the sorting algorithms 
4. Tested, if they work correctly 
5. Written a code to generate a document, in which there would have to be three kinds of sequences (Unordered - the reverse order, descending, Ordered, Random) with different cardinality (10,100,1000,10 000, 100 000)
6. Added timer code to all three algorithms 
7. Conducted several testings, measuring the time of algorithms‘ processing in different “mediums”
8. Plotted the graphs, built on the data gathered.

## Results
 ### GRAPH 1. Ordered massives.
<img src='https://github.com/Aborevsky01/Implementation-of-sorting-algorithms/blob/master/ordered.png' style='width: 50%; height: auto;'/>

  #### Commentary
As it can be seen in this coordinate system, bubble sort proves to be one of the fastest sorting algorithms when it comes to the ordered arrays, whatever the number of items is (however, there is a low increase of the blue line's angle, showing the higher efficiency of this particular method on a "small scale"). At the same time, insertion sort, which holds the second place in our sample, also has a significant advantage over quick sort in time. 

Summarazing the descirption, we need to admit that the aforementioned quadtratic sorting algorithms are not only highly rapid in the case when no raplaces have to be done, but also take a superior position to quick sort.

 ### GRAPH 2. Unordered massives.
<img src='https://github.com/Aborevsky01/Implementation-of-sorting-algorithms/blob/master/unordered.png' style='width: 50%; height: auto;'/>

  #### Commentary
This particular graph presents a totally different results: both quadratic sorting algorithms (insertion and bubble), having an approximately equal results with an insignificant edge of the former over the latter. However, both methods are lagged behind the quick sort, which perfectly deals with any size of unordered array in compare with its "rivals".

 ### GRAPH 3. Random massives.
<img src='https://github.com/Aborevsky01/Implementation-of-sorting-algorithms/blob/master/random.png' style='width: 50%; height: auto;'/>

  #### Commentary
Last graph in our research provides a great explanation of why quick sort is mych more popular than insertion and bubble sorting algorithms together. Quadratic sorts' lines form almost a right angle with the x-axis, which means horrible time results when working with large arrays of random elements. On the contrary, quick sort perfoms excellent results without any changes in compare with the previous graph.

## Inference
1. Bubble sort and Insertion sort always have relatively same results, which confirms the properties of both graphs listed in the Introduction. 
2. Quadratic functions have terrible results when it comes to time, except to the two cases: a) insignificant quantity of items within the array b) ordered array.
3. Despite being the worst algorithm in one out of the three cases, quick sort always completes the task for approximately the same amount of time no matter what type of array.

***
### Continue Exploring

Of course, my study did not sum up the entire topic, and much more can be attemted:
1. Add other various types of sorting algorithms and conduct the same research over them.
2. Increase the number of algorithms' charachteristics checked.
3. Work with different realizations of the same methods.

I am highly intrested in proceeding my research, as it is not only expands my knowledge in this particular area of study, but also improves my skills of programming. I hope this work was useful for you! If you found any mistakes/errors/inconsistents, feel free to contact me.
The entire exploration was done under the supervision of Maxim Suvorovtsev.
