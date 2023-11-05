from pyspark.sql import SparkSession

# Inicialize uma sessão Spark
spark = SparkSession.builder.appName("ProcessamentoLote").getOrCreate()

# Carregue o arquivo de dados
data = spark.read.csv("dados.txt", header=False, inferSchema=True)

# Execute uma operação simples, como contar as linhas
count = data.count()
print(f"Total de linhas: {count}")

# Encerre a sessão Spark
spark.stop()
