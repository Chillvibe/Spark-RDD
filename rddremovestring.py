from pyspark import SparkContext, SparkConf

# Create a SparkConf object
conf = SparkConf().setAppName("PythonDataCleaningExample")

# Create a SparkContext object
sc = SparkContext(conf=conf)

# Create an RDD of strings
strings = sc.parallelize(["Spark", "is", "awesome!", None, "", "Spark", "is", "awesome!"])

# Remove null or empty strings
non_empty_strings = strings.filter(lambda s: s is not None and s != "")

# Convert all strings to lowercase
lowercase_strings = non_empty_strings.map(lambda s: s.lower())

# Count the occurrences of each string
string_counts = lowercase_strings.countByValue()

# Print the counts
for string, count in string_counts.items():
    print(f"{string}: {count}")
