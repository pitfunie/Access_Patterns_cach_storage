## In all the above examples, AWS S3 is used as the persistent source of truth. Regardless of the caching strategy, all data eventually resides in S3 for durability and recovery.

## For reading data, you can query the cache first and fall back to S3 if the data is not present in the cache (a cache miss).

## Script: Cache Read with Fallback to S3
