import sys
from qcloud_cos import CosConfig, CosS3Client

SECRET_ID = sys.argv[1]
SECRET_KEY = sys.argv[2]
REGION = "ap-beijing"
BUCKET = "mbti-test-qiangzhe-1449572002"

config = CosConfig(Region=REGION, SecretId=SECRET_ID, SecretKey=SECRET_KEY)
client = CosS3Client(config)

# 先看当前对象的响应头
try:
    head = client.head_object(Bucket=BUCKET, Key="index.html")
    print("BEFORE ContentDisposition:", head.get("Content-Disposition"))
except Exception as e:
    print("head_object error:", e)

# 复制到自身，覆盖 Content-Disposition 为 inline（并清除 attachment）
resp = client.copy_object(
    Bucket=BUCKET,
    Key="index.html",
    CopySource={
        "Bucket": BUCKET,
        "Key": "index.html",
        "Region": REGION,
    },
    CopyStatus="Copy",
    MetadataDirective="Replaced",
    ContentDisposition="inline",
    ContentType="text/html",
)
print("copy_object done")

head2 = client.head_object(Bucket=BUCKET, Key="index.html")
print("AFTER ContentDisposition:", head2.get("Content-Disposition"))
print("AFTER ContentType:", head2.get("Content-Type"))
