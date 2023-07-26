import boto3

# Create a Secrets Manager client
secretsmanager_client = boto3.client('secretsmanager')

# Get the secret value
get_secret_value_response = secretsmanager_client.get_secret_value(
    SecretId='MySecretName'
)

# Save the secret value to a file
with open('secret.txt', 'w') as f:
    f.write(get_secret_value_response['SecretString'])