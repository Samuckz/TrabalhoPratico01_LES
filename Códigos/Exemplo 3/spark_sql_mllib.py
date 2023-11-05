from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Inicialize uma sessão Spark
spark = SparkSession.builder.appName("SparkSQLMLlib").getOrCreate()

# Carregue um arquivo CSV como um DataFrame usando Spark SQL
data = spark.read.csv("dados.csv", header=True, inferSchema=True)

# Prepare os dados para treinamento do modelo de regressão linear
feature_cols = data.columns[:-1]
vector_assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data = vector_assembler.transform(data)

# Divida os dados em conjuntos de treinamento e teste
train_data, test_data = data.randomSplit([0.7, 0.3])

# Crie e treine um modelo de regressão linear
lr = LinearRegression(featuresCol="features", labelCol="label")
model = lr.fit(train_data)

# Avalie o modelo nos dados de teste
test_results = model.evaluate(test_data)
print("Erro Quadrático Médio (RMSE):", test_results.rootMeanSquaredError)

# Encerre a sessão Spark
spark.stop()
