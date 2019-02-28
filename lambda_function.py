import Algorithmia

def lambda_handler(event, context):
    algorithmia_client_key = #Insert your client key as a string
    input = 12.33
    client = Algorithmia.client(algorithmia_client_key)
    algo = client.algo('salmaniqbalons/rounder/0.1.0')
    print(algo.pipe(input).result)