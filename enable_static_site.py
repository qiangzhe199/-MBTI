import sys
from qcloud_cos import CosConfig, CosS3Client

SECRET_ID = sys.argv[1]
SECRET_KEY = sys.argv[2]
REGION = "ap-beijing"
BUCKET = "mbti-test-qiangzhe-1449572002"

config = CosConfig(Region=REGION, SecretId=SECRET_ID, SecretKey=SECRET_KEY)
client = CosS3Client(config)

# 开启静态网站，索引文档设为 index.html，错误文档也指向它
resp = client.put_bucket_website(
    Bucket=BUCKET,
    WebsiteConfiguration={
        "IndexDocument": {"Suffix": "index.html"},
        "ErrorDocument": {"Key": "index.html"},
    },
)
print("put_bucket_website OK")

# 验证
conf = client.get_bucket_website(Bucket=BUCKET)
print("WebsiteConfiguration:", conf.get("WebsiteConfiguration"))
