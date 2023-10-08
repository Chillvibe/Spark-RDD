from pyspark import SparkContext, SparkConf

# Create a SparkConf object
conf = SparkConf().setAppName("PythonComplexAggregationExample")

# Create a SparkContext object
sc = SparkContext(conf=conf)

# Create an RDD of tuples
grades = sc.parallelize([
    ("student1", "2023-01-01", 90),
    ("student2", "2023-01-02", 85),
    ("student1", "2023-01-03", 88),
    ("student3", "2023-01-04", 92),
    ("student2", "2023-01-05", 95),
    ("student1", "2023-01-06", 89)
])

# Filter out the tuples with a null or empty student ID
non_empty_grades = grades.filter(lambda x: x[0] is not None and x[0] != "")

# Group the data by student ID
grouped_grades = non_empty_grades.groupBy(lambda x: x[0])

# Calculate the average score for each student
average_grades = grouped_grades.mapValues(lambda scores: (len(scores), sum(score[2] for score in scores)))

# Calculate the average score for each student
final_average_grades = average_grades.mapValues(lambda x: x[1] / x[0])

# Sort the students by their average score
sorted_average_grades = final_average_grades.sortBy(lambda x: x[1])

# Collect the results
results = sorted_average_grades.collect()

# Print the results
for student_id, average_grade in results:
    print(f"{student_id}: {average_grade}")
