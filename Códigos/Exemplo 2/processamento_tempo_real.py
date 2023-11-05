from pyspark.streaming import StreamingContext

# Inicialize o StreamingContext com intervalo de 1 segundo
ssc = StreamingContext(sparkContext, 1)

# Crie um DStream a partir de uma fonte de dados em tempo real, como Kafka ou soquetes
# Neste exemplo, usaremos uma fonte de teste
dstream = ssc.socketTextStream("localhost", 9999)

# Execute uma operação simples, como contar as palavras
word_counts = dstream.flatMap(lambda line: line.split(" ")).countByValue()

# Imprima os resultados em tempo real
word_counts.pprint()

# Inicie o StreamingContext
ssc.start()

# Aguarde a terminação (Ctrl+C para encerrar)
ssc.awaitTermination()