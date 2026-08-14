import sys
from qcloud_cos import CosConfig, CosS3Client

SECRET_ID = sys.argv[1]
SECRET_KEY = sys.argv[2]
REGION = "ap-beijing"
BUCKET = "mbti-test-qiangzhe-1449572002"

config = CosConfig(Region=REGION, SecretId=SECRET_ID, SecretKey=SECRET_KEY)
client = CosS3Client(config)

# 用标准对象存储域名（非 cos-website）做几个测试：
# 1. 直接访问对象（可能 403 因为桶是私有读）
# 2. 生成带签名的预签名 URL，带 response-content-type=text/html，看是否能浏览器内联打开
import urllib.parse

# 生成预签名 URL（临时签名，公开对象也可以直接构造普通 URL）
try:
    url = client.get_presigned_url(
        Method="GET",
        Bucket=BUCKET,
        Key="index.html",
        Params={"response-content-type": "text/html", "response-content-disposition": "inline"},
        Expired=3600,
    )
    print("SIGNED_URL:")
    print(url)
except Exception as e:
    print("presign err:", e)

# 标准域名直接 URL（对象若为公有读可直接访问）
print()
print("STD_URL: https://" + BUCKET + ".cos." + REGION + ".myqcloud.com/index.html")
