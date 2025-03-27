def read_feed(user_id):
    # Check the cache first
    feed_data = cache.get(user_id)
    if feed_data:
        print(f"Cache hit: {feed_data}")
        return feed_data
    
    # Fallback to S3 (cache miss)
    print("Cache miss: Fetching from persistent store.")
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=f'feeds/{user_id}.json')
    feed_data = obj['Body'].read().decode('utf-8')
    
    # Optionally, update the cache for future requests
    cache.set(user_id, feed_data)
    return feed_data

# Example usage
print(read_feed('user123'))
