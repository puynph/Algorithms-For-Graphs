
Extract the following files in to the same folder on your computer. 

-CountShortest_dum.py   # This file contains my implementation for the algorithm and is the only
			# code that I've written

-esim1.py  		# Originally from the course moodle "Example graphs and some Python code" folder
-graafi.py		# Originally from the course moodle "Python Code" folder.

Place the following files in to the same folder where you extracted previous files.

-all testgraphs
-all testset


Execute the esim1.py with PyCharm Community Edition 2022.3.2
(You can also use your own python file as long as it has the same function call, import method
and file reader.)

    G = Graph('testgraph_1')
    B = ReadSet('testset_1')
    x = CountShortest(G, B, 1, 10)
    print(x)

You will need to manually add inspections for the simple graphs.