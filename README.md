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

rddremovestring:
Creates an RDD of strings, removes any null or empty strings, converts all strings to lowercase, and then counts the occurrences of each string by:
Creating a SparkConf object and a SparkContext object.
Creating an RDD of strings, including some null and empty strings.
Removing null or empty strings from the RDD using the filter transformation.
Converting all strings in the RDD to lowercase using the map transformation.
Counting the occurrences of each string using the countByValue action.
Printing the counts using a Python for loop.

