# AWS Glue CSV to Parquet Data Pipeline

## Project Description
This project converts CSV files into Parquet format using AWS Glue and Amazon S3.

## AWS Services Used
- Amazon S3
- AWS Glue Crawler
- AWS Glue Data Catalog
- AWS Glue ETL Job
- Amazon EventBridge

## Input Data
The input CSV file contains sales information:
- Order ID
- Customer ID
- Product
- Amount
- Region

## Data Processing
1. Read CSV data from Amazon S3.
2. Detect the schema using AWS Glue.
3. Remove rows with null Customer ID.
4. Convert the cleaned data into Parquet format.
5. Store the output in the processed S3 bucket.

## S3 Locations
**Input:** sakthi-raw-sales-data

**Output:** sakthi-processed-sales-data/parquet-output/

## Output Format
Parquet (Snappy Compression)

## Result
Successfully converted CSV data into Parquet format using AWS Glue and PySpark.
