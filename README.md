# Spark-RDD
Run this in your spark core environment. Change the file path.


This python code performs a simple word count operation. It also shows how to use Spark's RDD (Resilient Distributed Dataset):

It creates a SparkConf object with the name of the application.
It creates a SparkContext object, which is the entry point to any Spark functionality.
It loads a text file into an RDD using the textFile method of the SparkContext object.
It splits the lines of the text file into words using the flatMap method of the RDD.
It counts the occurrences of each word using the countByValue method of the RDD.
It prints the counts.

