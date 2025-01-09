from pyspark.sql import SparkSession

def process_data(data_path):
    spark = SparkSession.builder.appName("PortfolioProcessor").getOrCreate()
    df = spark.read.csv(data_path, header=True, inferSchema=True)
    df.show()
    return df