import sys
from qcloud_cos import CosConfig, CosS3Client

SECRET_ID = sys.argv[1]
SECRET_KEY = sys.argv[2]
REGION = "ap-beijing"
BUCKET = "mbti-test-qiangzhe-1449572002"

config = CosConfig(Region=REGION, SecretId=SECRET_ID, SecretKey=SECRET_KEY)
client = CosS3Client(config)

# 1. 查 bucket 的响应头规则
try:
    rr = client.get_bucket_replication(Bucket=BUCKET)
    print("replication:", rr)
except Exception as e:
    print("replication err:", e)

# 2. 查 CORS / 网站配置
try:
    w = client.get_bucket_website(Bucket=BUCKET)
    print("website:", w)
except Exception as e:
    print("website err:", e)

# 3. 列出 bucket 根目录对象，看 index.html 是否存在及大小
resp = client.list_objects(Bucket=BUCKET)
if "Contents" in resp:
    for o in resp["Contents"]:
        print("obj:", o.get("Key"), o.get("Size"))
else:
    print("no contents")

# 4. 直接 head 看所有头
h = client.head_object(Bucket=BUCKET, Key="index.html")
print("--- head_object full ---")
for k, v in h.items():
    if k not in ("Body",):
        print(k, "=", v)
