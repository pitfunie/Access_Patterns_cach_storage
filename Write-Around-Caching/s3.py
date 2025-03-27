def write_around(user_id, feed_data):
    # Write directly to persistent storage (S3)
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f'feeds/{user_id}.json',
        Body=feed_data
    )
    print(f"Write-around: Data written directly to persistent store.")

# Example usage
write_around('user789', '{"feed": "Rarely Accessed Content"}')
