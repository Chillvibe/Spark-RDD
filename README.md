# Information
Run this in your spark core environment. Change the file path.

rddspark:
This python code performs a simple word count operation. It also shows how to use Spark's RDD (Resilient Distributed Dataset):

It creates a SparkConf object with the name of the application.
It creates a SparkContext object, which is the entry point to any Spark functionality.
It loads a text file into an RDD using the textFile method of the SparkContext object.
It splits the lines of the text file into words using the flatMap method of the RDD.
It counts the occurrences of each word using the countByValue method of the RDD.
It prints the counts.

rddfilter:
Creates an RDD of integers, performs a series of transformations to filter, maps, and reduces the data, and then perform an action to collect the results by:
Creating a SparkConf object and a SparkContext object.
Creating an RDD of integers.
Filtering out the even numbers from the RDD using the filter transformation.
Squaring each number in the filtered RDD using the map transformation.
Summing the squared numbers using the reduce transformation.
Printing the total using a Python print statement.
