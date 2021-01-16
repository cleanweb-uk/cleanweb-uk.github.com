#!/usr/bin/python
import boto
import os
import time
from boto.s3.connection import S3Connection

HOST="s.greenqloud.com"

def upload_website(bucket_name,
                   website_dir,
                   index_file,
                   error_file=None):
    """
    Upload a static website contained in a local directory to
    a bucket in S3.

    bucket_name The name of the bucket to upload website to.
    website_dir Fully-qualified path to directory containing
                website.
    index_file  The name of the index file (e.g. index.html)
    error_file  The name of the error file.  If not provided
                the default S3 error page will be used.
    """
    conn = S3Connection(ACCESS_KEY, SECRET_KEY,host=HOST)
    try:
        bucket = conn.lookup(bucket_name)
    except:
        pass
    if bucket==None:
        bucket = conn.create_bucket(bucket_name,policy='public-read')
    # Make sure bucket is publicly readable
    #bucket.set_canned_acl('public-read')

    for root, dirs, files in os.walk(website_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, website_dir)
            print "full_path"+full_path
            print "rel_path"+rel_path
            print 'Uploading %s as %s' % (full_path, rel_path)
            key = bucket.new_key(rel_path)
            key.set_contents_from_filename(full_path, policy='public-read')
            if ".html" in key:
                key.content_type = 'text/html'

    # Now configure the website
    bucket.configure_website(index_file, error_file)

    # A short delay, just to let things become consistent.
    time.sleep(5)

    print 'You can access your website access at:'
    print bucket.get_website_endpoint()


if  __name__ =='__main__':
    ACCESS_KEY=os.getenv('EC2_ACCESS_KEY')
    SECRET_KEY=os.getenv('EC2_SECRET_KEY')
    bucket_name=os.getenv('TARGET_DOMAIN')
    subpath="public"
    website_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)),subpath)
    print "website dir is:" +website_dir
    index_file="index.html"
    error_file="error.html"
    upload_website(bucket_name,website_dir,index_file,error_file)


