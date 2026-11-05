import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

input_path = "s3://sakthi-raw-sales-data/"
output_path = "s3://sakthi-processed-sales-data/parquet-output/"

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(input_path)

clean_df = df.dropna(subset=["customer_id"])

clean_df.write \
    .mode("overwrite") \
    .parquet(output_path)

print("CSV to Parquet conversion completed successfully!")

spark.stop()
