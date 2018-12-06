""" This is a class for upload download and crypt file to s3"""
import os
import time
from multiprocessing.pool import ThreadPool
import boto3


class S3Cicle:
    """ This is a class for upload download and crypt file to s3"""

    def __init__(
            self,
            bucket_name,
            encryption='AES256',
            aws_access_key_id=None,
            aws_secret_access_key=None):
        self.s3_client = boto3.resource(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        self.__bucket = self.s3_client.Bucket(bucket_name)
        self.downloaded_dir = str('Downloads-'+time.strftime('%Y%m%d-%H%M%S'))
        self.files_list = [file for file in self.__bucket.objects.all()]
        self.encryption = encryption

    def __str__(self):
        return str(self.files_list)

    def _get_file_structure(self):
        file_list_to_change = list()
        for file in self.files_list:
            key = self.s3_client.Object(self.__bucket.name, file.key)
            if not key.server_side_encryption:
                file_list_to_change.append(file.key)
                path, _ = os.path.split(file.key)
                new_path = self.downloaded_dir+"/"+path
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
        return file_list_to_change

    def _file_cicle(self, file_name):
        s3_file_name = self.downloaded_dir+"/"+file_name
        self.__bucket.download_file(
            file_name, s3_file_name)
        #self.__bucket.s3.meta.client.upload_file(
        #    s3_file_name, file_name, extra_args={
        #        'ServerSideEncryption': self.encryption
        #    })

    def magic_method(self):
        """Most exciting method"""
        pool = ThreadPool(processes=10)
        pool.map(self._file_cicle, self._get_file_structure())


def _main():
    t_0 = time.time()
    my_object = S3Cicle(
        'here-olp-marina',
        aws_access_key_id='key',
        aws_secret_access_key='secret')
    my_object.magic_method()
    print(time.time() - t_0)


if __name__ == "__main__":
    _main()
