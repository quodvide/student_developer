# Markdown
**Markdown** is a plain text formatting syntax created by John Gruber, aiming to provide a easy-to-read and feasible markup. 


## How to use?
**Strong** : `**Strong**` or `__Strong__` (Command-B)
   
*Emphasize* : `*Emphasize*` or `_Emphasize_` (Command-I)  

**Inline Link** : <http://www.something.com> is `<http://www.something.com>` or  
[Here!](http://www.something.com>) is `[Here!](http://www.something.com>)` like this.  

**Refence style Link** : [like this][arbitrary_id] is `[like this][arbitrary_id]` and anywhere of this file `[arbitrary_id]:http://www.naver.com "title"` or  
[like this][] `[like this][]`, then on it's own line anywhere else in the file:  
`[like this]: http://www.naver.com`  

**Inline Image**
`![Alt Image Text](path/or/url/to.jpg "Optional Title")`  

**Reference style Image**
`![Alt Image Text][image-id]`  
on it's own line elsewhere: 
`[image-id]: path/or/url/to.jpg "Optional Title"`  

**List**  

* Lists must be preceded by a blank line (or block element)  
* Unordered lists start each item with a `*`  
- `-` works too 
	* Indent a level to make a nested list
        1. Ordered lists are supported.   
        2. Start each item (number-period-space) like `1. `  
        42. It doesn't matter what number you use, I will render them sequentially  
        1. So you might want to start each line with `1.` and let me 



```
* Lists must be preceded by a blank line (or block element)
* Unordered lists start each item with a `*`
- `-` works too
	* Indent a level to make a nested list
		1. Ordered lists are supported.
		2. Start each item (number-period-space) like `1. `
		42. It doesn't matter what number you use, I will render them sequentially
		1. So you might want to start each line with `1.` and let me sort it out
```   

And `***` or `___` makes a horizon. 

[arbitrary_id]:http://www.naver.com "title"
[like this]: http://www.naver.com

#Header (Like this header 1)

	#Header1
	##Header2
	###Header3
	####Header4
	#####Header5
	######Header6  
or

	Header1
	=========================  
	Header2
	_________________________
	

