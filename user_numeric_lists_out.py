Task 3. Numeric List
Lists:
list1:
 [194, 190, 185, 180, 173, 162, 157, 144, 141, 139, 131, 131, 126, 122, 117, 116, 114, 114, 111, 102, 101, 98, 97, 94, 93, 93, 89, 87, 87, 83, 74, 70, 66, 65, 65, 62, 61, 55, 52, 50, 48, 46, 29, 27, 27, 24, 23, 21, 19, 5].

listx:
 [94, 109, 143, 69, 167, 69, 186, 136, 54, 21].

listy:
 [1, 5, 4, 7, 9, 13, 20, 45, 50, 70].

**********List 1: List Statistics**********
1. The mean, median and mode of list1 are 93.20,93.00 and 65.00 respectively.
2. The standard deviation and variance of list1 is 49.63 and 2462.78 respectively.

**********List 2: Lists - Correlation and Prediction**********
1. The correlationxy of listx and listy is -0.47
2. The slope and intercept of listx and listy are -0.21 and 44.74
3. x has been set to 15 for a future time
4. When setting the future value for x to 15, the new y value is equal to 41.54

**********Lists 3. Lists - Using Python Built-in Functions**********
1. The min of list1 is 5.
2. The max of list1 is 194.
3. The length of list1 is 50.
4. The sum of list1 is 4660.
5. The average of list1 is 93.20.

6. The following is a set which has been created from list1:
{131, 5, 139, 141, 144, 19, 21, 23, 24, 27, 157, 29, 162, 173, 46, 48, 50, 180, 52, 55, 185, 61, 62, 190, 65, 194, 66, 70, 74, 83, 87, 89, 93, 94, 97, 98, 101, 102, 111, 114, 116, 117, 122, 126}.

7. The following is list1 after it has been sorted:
[5, 19, 21, 23, 24, 27, 27, 29, 46, 48, 50, 52, 55, 61, 62, 65, 65, 66, 70, 74, 83, 87, 87, 89, 93, 93, 94, 97, 98, 101, 102, 111, 114, 114, 116, 117, 122, 126, 131, 131, 139, 141, 144, 157, 162, 173, 180, 185, 190, 194].      

8. The following is list1 after the list has been sorted in reverse order:
[194, 190, 185, 180, 173, 162, 157, 144, 141, 139, 131, 131, 126, 122, 117, 116, 114, 114, 111, 102, 101, 98, 97, 94, 93, 93, 89, 87, 87, 83, 74, 70, 66, 65, 65, 62, 61, 55, 52, 50, 48, 46, 29, 27, 27, 24, 23, 21, 19, 5].      

**********Lists 4. List Methods**********
Randomly generated a new short list:
[20, 18, 16, 20, 14, 13, 3, 19, 20, 15, 17, 19, 2, 16, 15].

1. Appended the single value of 43 to the list:
[20, 18, 16, 20, 14, 13, 3, 19, 20, 15, 17, 19, 2, 16, 15, 43].

2. Extended the list with 9, 11, 13 and 16:
[20, 18, 16, 20, 14, 13, 3, 19, 20, 15, 17, 19, 2, 16, 15, 9, 11, 13, 16].

3. Inserted the number 56 at index 10:
[20, 18, 16, 20, 14, 13, 3, 19, 20, 15, 56, 17, 19, 2, 16, 15, 9, 11, 13, 16].

4. The updated list:
There are no changes as 5 was not in the prior list.

5. The number 2 appears in the list 1 time.

6. Sorted the list using .sort() to reflect ascending order:
[2, 3, 9, 11, 13, 13, 14, 15, 15, 16, 16, 16, 17, 18, 19, 19, 20, 20, 20, 56]

7. Sorted the list using .sort(reverse=True) to reflect descending order:
[56, 20, 20, 20, 19, 19, 18, 17, 16, 16, 16, 15, 15, 14, 13, 13, 11, 9, 3, 2]

8. Copied the list using .copy():
[56, 20, 20, 20, 19, 19, 18, 17, 16, 16, 16, 15, 15, 14, 13, 13, 11, 9, 3, 2]

9. Utilized pop() to remove the first item off the top of the list /stack:
[56, 20, 20, 20, 19, 19, 18, 17, 16, 16, 16, 15, 15, 14, 13, 13, 11, 9, 3]

10. Utilized pop() to remove the last time off the bottom of the list/stack:
[56, 20, 20, 20, 19, 19, 18, 17, 16, 16, 16, 15, 15, 14, 13, 13, 11, 9]

**********Lists 5. List Transformations - Using filter() and map()**********
1. Used filter() to filter to only the even numbers in the list:
[56, 20, 20, 20, 18, 16, 16, 16, 14].

2. Used map() to map each x to the cuberoot of x in the list:
[3.825862365544778, 2.7144176165949063, 2.7144176165949063, 2.7144176165949063, 2.668401648721945, 2.668401648721945, 2.6207413942088964, 2.571281590658235, 2.5198420997897464, 2.5198420997897464, 2.5198420997897464, 2.46621207433047, 2.46621207433047, 2.4101422641752297, 2.3513346877207573, 2.3513346877207573, 2.2239800905693152, 2.080083823051904].

3. Used map() to map calculate the volume of a cube with a side equal to the value in the list:
[175616, 8000, 8000, 8000, 6859, 6859, 5832, 4913, 4096, 4096, 4096, 3375, 3375, 2744, 2197, 2197, 1331, 729].

**********List 6. List Transformations - Using List Comprehension**********
1. Used a list comprehension to filter x for each x in list1 that is less than 50:
[48, 46, 29, 27, 27, 24, 23, 21, 19, 5].

2. Used a list comprehension to triple each value in list1:
[7301384, 6859000, 6331625, 5832000, 5177717, 4251528, 3869893, 2985984, 2803221, 2685619, 2248091, 2248091, 2000376, 1815848, 1601613, 1560896, 1481544, 1481544, 1367631, 1061208, 1030301, 941192, 912673, 830584, 804357, 804357, 704969, 658503, 658503, 571787, 405224, 343000, 287496, 274625, 274625, 238328, 226981, 166375, 140608, 125000, 110592, 97336, 24389, 19683, 19683, 13824, 12167, 9261, 6859, 125].

3. Used a list comprehension to divide each value in list1 by 2.5:[77.6, 76.0, 74.0, 72.0, 69.2, 64.8, 62.8, 57.6, 56.4, 55.6, 52.4, 52.4, 50.4, 48.8, 46.8, 46.4, 45.6, 45.6, 44.4, 40.8, 40.4, 39.2, 38.8, 37.6, 37.2, 37.2, 35.6, 34.8, 34.8, 33.2, 29.6, 28.0, 26.4, 26.0, 26.0, 24.8, 24.4, 22.0, 20.8, 20.0, 19.2, 18.4, 11.6, 10.8, 10.8, 9.6, 9.2, 8.4, 7.6, 2.0].