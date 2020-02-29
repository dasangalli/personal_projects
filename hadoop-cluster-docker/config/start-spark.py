with open("/root/.bashrc","a") as file:
	file.write("export SPARK_HOME=~/spark-2.4.4-bin-hadoop2.7\n")
	file.write("export PATH=$PATH:$SPARK_HOME/bin\n")
	file.write("export PYSPARK_PYTHON=python3.6\n")
	file.write("export PATH=$PATH:$JAVA_HOME/jre/bin")

file.close()