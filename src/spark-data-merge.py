import pyspark as ps
from pyspark.sql.types import *
import pyspark.sql.functions as F
import sys
import pandas as pd
import numpy as np
import json

def create_session():
    spark = ps.sql.SparkSession.builder \
                .master("local") \
                .appName("capstoneDF") \
                .getOrCreate()
    sc = spark.sparkContext
    df_artist_features = spark.read.csv('/home/luke/Documents/dsi/Capstone1/data/data_by_artist.csv',header=True).cache()
    df_artist_features.printSchema()
    print("line count: {}".format(df_artist_features.count()))
    df_artist_features.show()








if __name__ == '__main__':
    print(create_session())
