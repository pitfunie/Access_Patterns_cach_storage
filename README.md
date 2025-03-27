## Access_Patterns_cach_storage

## Summary:

##    Write-Through: Ensures strong consistency by writing to both the cache and storage.

##    Write-Back: Improves performance for write-heavy access patterns by asynchronously syncing to storage.

##    Write-Around: Bypasses the cache for infrequent updates, focusing on direct writes to the persistent store.

##    Read with Fallback: Combines cache and storage for efficient data access.

![2025-03-26_23-00-04](https://github.com/user-attachments/assets/91ccc66b-070d-4490-bf9f-a4b36d141308)


1. Metadata Storage Estimate

Assuming metadata includes basic information for each photo, such as:

    Photo ID

    User ID

    Timestamp

    Tags/Description

    Photo URL

Each metadata record could average 500 bytes per photo. For 100 million photos uploaded daily:

    Daily Metadata Storage:

100 million×500 bytes=50 GB/day100 \, \text{million} \times 500 \, \text{bytes} = 50 \, \text{GB/day}

    Annual Metadata Storage:

50 GB/day×365=18,250 GB/year=18.25 TB/year50 \, \text{GB/day} \times 365 = 18,250 \, \text{GB/year} = 18.25 \, \text{TB/year}
2. Photo Storage Estimate

Assuming the average photo size is 200KB (kilobytes):

    Daily Photo Storage:

100 million×200 KB=20,000 GB/day=20 TB/day100 \, \text{million} \times 200 \, \text{KB} = 20,000 \, \text{GB/day} = 20 \, \text{TB/day}

    Annual Photo Storage:

20 TB/day×365=7,300 TB/year20 \, \text{TB/day} \times 365 = 7,300 \, \text{TB/year}
Summary

    Metadata Storage Requirement: ~50 GB/day, ~18.25 TB/year.

    Photo Storage Requirement: ~20 TB/day, ~7,300 TB/year.

For 500 million daily active users, scalable solutions like cloud storage (e.g., AWS S3) and CDNs would be essential for handling both metadata and photos efficiently.

Would you like help exploring specific storage solutions or strategies to optimize costs and performance for such a large-scale system? Let’s brainstorm! 🚀
