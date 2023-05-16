
from google.cloud import storage

def create_bucket(bucket_name):
    # Instantiate a client
    client = storage.Client()

    # Create the bucket
    bucket = client.create_bucket(bucket_name)

    print(f"Bucket '{bucket.name}' created.")

# Specify the desired bucket name
bucket_name = "ivobukk"

# Call the create_bucket function
create_bucket(bucket_name)

