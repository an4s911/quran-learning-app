# Quran Learning App

\**The code hasn't been documented properly yet.*

## Requirements

It should work well Python 3.6x+ but they are untested. Its built using Python 3.10. It only uses one library `pickle` which is used for saving the data dictionary as a binary file. 

## Installation

- Clone this repository, or download the zip file and unzip it.
- Open a terminal in the project directory. The current working directory should be `quran-learning-app/`. And then enter:
```bash
$ python . 
```
and the program runs

## How it works?

The way it helps in revising Quran memorization is using something called a spaced-repitition algorithm[^1]. It is not the perfect implementation of it, but is it something that works. And I built it to be simple and easy to use, and with not a lot of complications, which might lead to problems later on that can interrupt my revision process. It specifically uses somewhat of a modified version of something called as a Leitner-System[^2], which uses three boxes to arrange your learning "cards". 

Its very simple, there are 4 boxes namely *Today Schedule*, *Urgent*, *Normal* and *Less Urgent*. The first one is only to represent what you will revise today. The other three are frequency boxes, where *Urgent* is the most often repeated, *Normal* being less often and *Less Urgent* being the least often[^3] (<-- please do read the footnote). 

When you first run the code, it gives you menu of functions this program offers:
```
Quran Memoriation
=====MENU=====
1. Today
2. Next
3. Restack
4. Add
5. Lists
6. Latest
0. Exit
--------------
9.advanced
: _
```

You can type one of those numbers and press enter to select one[^4][^5]. The details for each item:
- Today - it shows you a list which has all the items you need to revise today
- Next - shows you the next item you need revise, and this removes the item from the today's list, and also asks you which frequency list do you wanna place it in after revising (urgent, normal or less urgent). So you pick one of them based on how well you've memorized it, where urgent stands for less proficient, all the way to less urgent which stands for very fluent and you've memorized it well. 
- Restack - This restacks the today's list, it removes items from the frequency list, and then fill up the today list. (Keep in mind that today list can only hold upto 3 items[^6]). It takes more urgent items than normal, and more normal than less urgent. 
- Add - add new items for revising. It asks you what is the value (or name) you want it to hold, and which frequency list you wanna add it to[^7].
- Lists - shows a list of all the lists (today's list and the frequency lists) and items it contains. 
- Latest - shows you the most recently added item that you added using number *4*.
- Advanced - currently it only has one extra option, that is to remove any items. (Keep in mind, currently it only removes the item from the lists and if that was the latest item, it does not reflect on it). More options like move items around are planned for implementation.

[^1]: https://en.m.wikipedia.org/wiki/Spaced_repetition
[^2]: https://en.m.wikipedia.org/wiki/Leitner_system
[^3]: You can change how often they are repeated by modifying some numbers in the code. But it will only work if you do it at first before you ever run the code. A feature to change those values easily is planned to be implemented. But as of now, you can only change those values if you know python and know how to use the `pickle` library. If you already know python, then its not that hard.
[^4]: I am planning on implementing a feature which lets you just type the keyword instead of the numbers.
[^5]: Error handling in the input hasn't been implemented yet. So, it can only take inputs that it expects, and any other input like anything other than an integer will give errors and quit the program. So be careful with that. But as of now, I haven't seen any data being compromised due to this exit, so for now its okay. But a fix is coming soon. As it is a personal project, I am not making it too much fail-safe too early, but I need to soon. 
[^6]: As mentioned in footnote number 3[^3], this also can be changed, but not very easy after you've first run your program. But soon the features are gonna be implemented. 
[^7]: Usually you add an item after you've revised it or memorized it. So based on how fluent you think you are, you can select a frequency list.
