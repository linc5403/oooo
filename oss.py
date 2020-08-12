import oss2

endpoint = 'http://oss-cn-hangzhou.aliyuncs.com' # Suppose that your bucket is in the Hangzhou region.

auth = oss2.Auth('<Your AccessKeyID>', '<Your AccessKeySecret>')
bucket = oss2.Bucket(auth, endpoint, '<your bucket name>')

# The object key in the bucket is story.txt
key = 'story.txt'

# Upload
bucket.put_object(key, 'Ali Baba is a happy youth.')

# Download
bucket.get_object(key).read()

# Delete
bucket.delete_object(key)

# Traverse all objects in the bucket
for object_info in oss2.ObjectIterator(bucket):
    print(object_info.key)
