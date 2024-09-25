from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as ps_sum
import time

spark = SparkSession.builder \
    .appName("query 1 & 2 Spark SQL") \
    .getOrCreate()

hdfs_file_path = "hdfs://localhost:9000/user/anirudh/FlumeData.1711803652109"

df = spark.read.csv(hdfs_file_path, header=True, inferSchema=True)

df.printSchema()

df.show()

print('--- Spark SQL ----')
df.createOrReplaceTempView("bds_retail")
start_time = time.time()
result = spark.sql("SELECT SUM(Price) FROM bds_retail WHERE InvoiceDate LIKE '%2010%'")
end_time = time.time() - start_time

print('total revenue:',result.collect()[0][0])
print('query 1 time:', end_time)
print()
start_time = time.time()
result = spark.sql("SELECT DISTINCT StockCode, SUM(Quantity) FROM bds_retail WHERE InvoiceDate LIKE '%2010%' GROUP BY StockCode ORDER BY StockCode")
end_time = time.time() - start_time
result.show(50)
print('query 2 time:', end_time)

spark.stop()

#print('--- Spark DataFrame ---')

#start_time = time.time()
#filtered_df = df.filter(col("InvoiceDate").like("%2010%"))
#total_revenue = filtered_df.select(ps_sum("Price")).collect()[0][0]
#end_time = time.time() - start_time
#print('total revenue:',total_revenue)
#print('query 1 time:', end_time)
#print()
#start_time = time.time()
#filtered_df = df.filter(col("InvoiceDate").like("%2010%"))
#grp_sum_df = filtered_df.groupBy('StockCode').sum('Quantity')
#grp_sum_df.orderBy(grp_sum_df["StockCode"].asc()).show()
#end_time = time.time() - start_time
#print('query 2 time:', end_time)

#print()
