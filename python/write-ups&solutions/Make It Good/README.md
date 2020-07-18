# Make It Good

_Question is extremely long, so you can find it here at [this contest link](https://codeforces.com/contest/1385/problem/C)_

tl;dr: This question involves an array 𐤀 of size n. 𐤀 needs to be made into a _good_ array, where a _good_ array is defined by an array which can be completely made into a non-decreasing array by transferring either the first or last element one by one. Here's an example:

b = [1,2,3,4,4,2,1] . This array is _good_ because we can obtain a non-decreasing array c from it by the following sequence of operations:

take the first element of b, so b=[2,3,4,4,2,1], c=[1]<br/>
take the last element of b, so b=[2,3,4,4,2], c=[1,1]<br/>
take the last element of b, so b=[2,3,4,4], c=[1,1,2]<br/>
take the first element of b, so b=[3,4,4], c=[1,1,2,2]<br/>
take the first element of b, so b=[4,4], c=[1,1,2,2,3]<br/>
take the last element of b, so b=[4], c=[1,1,2,2,3,4]<br/>
take the only element of b, so b=[], c=[1,1,2,2,3,4,4] — c is non-decreasing.

To make 𐤀 into a _good_ array, we can remove a prefix of size 𐡀, where a prefix is defined as a subarray starting from the first element of 𐤀. The task is to find the smallest possible value of 𐡀.

<ins>*Attempt to solve this question for yourself before proceeding*</ins>

## Question Analysis

This question was given in Codeforces Round #656, and I only made it past 3 questions before deciding to sleep. I did find my solution to the 3rd question quite cool, but I'm not really sure if its the most cost-efficient one. I will be going through my thought process and solving method below.

#### Initial Thoughts

Looking at the question at a glance, you can instantly know what this question is actually asking: Find the longest _good_ array ending at the last element of 𐤀. After you've found the length of this array, simply output the index of the beginning element of the _good_ array, which will be the length of the prefix to remove. Here's an example:

b = [4,3,3,8,4,5,2]. This array is not good yet, but we can see that the longest _good_ array ending at the last element 2 is [4,5,2], which gives a resulting non-decreasing array of [2,4,5]. Since the _good_ array starts at element 4 which is at index 4, the length of the prefix we have to remove is 4 (because an array starts from 0).

#### Pattern Recognition

If we find out what defining features a _good_ array has, we can check for those to determine its length. During the actual contest I was extremely stressed (like every other contest), so I usually wouldn't be able to catch such details at a glance. In such cases, it really helps to write out a few simple cases and extrapolate from there.

Listing out a few examples of _good_ arrays:<br/>
```
[1,2,1]
[3,2,2]
[2,2,3]
[2,3,4,4,2,1]
[1,2,3,4,4,3,2,2,1]
[5,25,26,1]
[1,2,4,5]
```

From these examples, it was clear that _good_ arrays were all in the form of a mountain (I made this up this isn't an actual term), where a mountain is defined by some length of non-decreasing elements followed by some other length of non-increasing elements. Note that these lengths can be 0, meaning that the array can be completely non-increasing/non-decreasing. In other words, the array goes up and down, just like a mountain.

Because an array is in this form, it is also symmetrical, meaning that it will still be _good_ if reversed. What that means is that we can traverse from the back of it to the front, instead of traversing from front to back, because the end of the _good_ array is much more well defined than the beginning.

From this analysis, we can identify 2 features of _good_ arrays:
- In mountain form
- Symmetrical

With this knowledge, all we have to do is traverse from the end to the beginning of the array, and find the point where the mountain stops.

## Writing Code

To find a mountain, we have to keep track of the gradient of the array, and the mountain ends when a minimum point is reached. I'll explain more about what this means in the next few lines.

An array's gradient (Once again I'm making this term up) will be defined as the change from the previous element to the current element. For example when traversing an array [3,4,5] the gradient is always +1, while in an array [4,5,3] the gradient goes from +1 (from 4 to 5) to -2 (from 5 to 3). When an array's gradient goes from positive to negative, a maxima is reached, and the mountain reaches its peak. When an array's gradient goes from negative to positive, a minima is reached, and the mountain ends.

To do this, I keep track of the gradient's polarity using a boolean `up`, which turns true when the gradient is positive, false when it's negative, and unchanged when it's 0. To calculate the polarity of the gradient, I traverse the array backwards, keeping track of the previous element, `foot`, and compare it to the current element `v[i]` at every interval. Using the boolean value and the polarity, we can easily identify the minimum point by checking if the mountain is descending and if the gradient is positive. If both are true, the point is minima and we output the current index -1.

I have uploaded 2 files, the `.cpp` one is the one I wrote during the contest, it's uncommented to save time but as a result it's also extremely short. The `.py` one I translated for the purpose of this write-up thing, which has relevant comments and descriptive variable names.
