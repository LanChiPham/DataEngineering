from pyspark import SparkConf
from pyspark import SparkContext
sc = SparkContext.getOrCreate(SparkConf().setMaster("local[*]"))

# count by value 
sample_text = "singapore is a safe country singapore passport is powerful singapore is a small country."

rdd_base = sc.parallelize(sample_text.split(","))
print(rdd_base.countByValue())