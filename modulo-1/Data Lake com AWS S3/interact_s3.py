import boto3
import pandas as pd

# Script para validar conexão boto3 com AWS S3 que retornará todos os nomes dos buckets existentes
# s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)


# Criar um cliente que interage com AWS S3
s3_client = boto3.client('s3')

# Download de arquivo usando boto3
s3_client.download_file('datalake-mbruno5-igti-edc',
                        'data/dimensao_mesorregioes_mg-1.csv',
                        'dimensao_mesorregioes_mg-1.csv')

# Lendo o arquivo baixado com a lib pandas
df = pd.read_csv("dimensao_mesorregioes_mg-1.csv", sep=";")
print(df)

# Upload de arquivo para AWS S3 bucket usando boto3
s3_client.upload_file(r'C:\Users\sobm9\Mbruno\bootcamps\bootcamp-edc-igti\modulo-1\Data Lake com AWS S3\mockaroo_funcionario.csv',
                       'datalake-mbruno5-igti-edc',
                       'data/mockaroo_funcionario.csv')
                    