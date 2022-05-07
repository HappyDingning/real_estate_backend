import oss2

from token_info.models import BucketInfo

decimals = 18

image_bucket_info = BucketInfo.objects.get(file_type='image')
meta_data_bucket_info = BucketInfo.objects.get(file_type='json')
image_tmp_bucket_info = BucketInfo.objects.get(file_type='image_tmp')

# need to config by yourself
auth = oss2.Auth('', '')

image_bucket = oss2.Bucket(auth, image_bucket_info.end_point, image_bucket_info.name)
meta_data_bucket = oss2.Bucket(auth, meta_data_bucket_info.end_point, meta_data_bucket_info.name)
image_tmp_bucket = oss2.Bucket(auth, image_tmp_bucket_info.end_point, image_tmp_bucket_info.name)
