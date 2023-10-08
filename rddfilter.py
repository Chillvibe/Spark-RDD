from pyspark import SparkContext, SparkConf

# Create a SparkConf object
conf = SparkConf().setAppName("RDDFilter")

# Create a SparkContext object
sc = SparkContext(conf=conf)

# Create an RDD of integers
numbers = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Filter out the even numbers
even_numbers = numbers.filter(lambda x: x % 2 == 0)

# Square each number
squared_numbers = even_numbers.map(lambda x: x ** 2)

# Sum the squared numbers
total = squared_numbers.reduce(lambda x, y: x + y)

# Print the total
print(total)
