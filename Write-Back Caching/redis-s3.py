import threading

# Delayed sync function
def sync_to_s3(user_id, feed_data):
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f'feeds/{user_id}.json',
        Body=feed_data
    )
    print(f"Write-back: Data synced to persistent store.")

def write_back(user_id, feed_data):
    # Write to cache
    cache.set(user_id, feed_data)
    
    # Async sync to S3
    threading.Thread(target=sync_to_s3, args=(user_id, feed_data)).start()
    print(f"Write-back: Data written to cache, syncing to persistent store.")
    
# Example usage
write_back('user456', '{"feed": "Another Post Content"}')
