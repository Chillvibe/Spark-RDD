from pyspark import SparkContext, SparkConf

# Create a SparkConf object
conf = SparkConf().setAppName("PythonWordCount")

# Create a SparkContext object
sc = SparkContext(conf=conf)

# Load a text file into an RDD
text_file = sc.textFile("hdfs://...")

# Split the lines into words
words = text_file.flatMap(lambda line: line.split(" "))

# Count the occurrences of each word
word_counts = words.countByValue()

# Print the counts
for word, count in word_counts.items():
    print(f"{word}: {count}")
