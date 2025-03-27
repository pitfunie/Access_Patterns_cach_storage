import redis
import boto3

# Initialize Redis (cache) and S3 (persistent store)
cache = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
s3 = boto3.client('s3')

BUCKET_NAME = 'feed-storage-bucket'

def write_through(user_id, feed_data):
    # Write to cache
    cache.set(user_id, feed_data)
    
    # Write to persistent storage (S3)
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f'feeds/{user_id}.json',
        Body=feed_data
    )
    print(f"Write-through: Data written to cache and persistent store.")

# Example usage
write_through('user123', '{"feed": "New Post Content"}')
