from pyspark.sql import SparkSession

def create_spark_session(app_name="Cancer Analysis"):
   spark = ( SparkSession.builder\
    .appName(app_name)\
    .config("spark.sql.shuffle.partitions","8")\
    .getOrCreate()
   )

   return spark
    
