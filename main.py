import redis
import json
from pathlib import *
import base64
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time
def handle_job(job_id):
    cmd = 'sh transform_image.sh'
    
    #run job
    p = Popen(cmd, stdout = PIPE,stderr = STDOUT, bufsize=1, shell = True)
    
    #check when the work is done and return result
    for line in iter(p.stdout.readline, b''):
        line = line.decode("utf-8")
        print(line)
        if "reached max number of iterations" in line:
            return_result(job_id)



def return_result(job_id):
    with open("output/output.png", 'rb') as img:
        img_to_base64 = base64.b64encode(img.read())
        result_dict = {"jobId":str(job_id),"resultImage":img_to_base64.decode('utf-8')}
        result = json.dumps(result_dict)
        print(result)
        r = redis.Redis(host='192.168.56.1', port=6379, db=0)
        r.rpush('result', result)
        del r






def main():
    while(True):
        #get job
        r = redis.Redis(host='192.168.56.1', port=6379, db=0)
        job_string = r.rpop('pending')
        del r
        
        if job_string is not None:
            job = json.loads(job_string)
        else:
            print('No jobs availible!')
            time.sleep(2)
            continue

        # decode source image
        enc_image = job['contentImage'].encode('utf-8')
        image = base64.b64decode(enc_image)

        # decode style image
        enc_style = job['styleImage'].encode('utf-8')
        style = base64.b64decode(enc_style)


        # save images
        with open(str(Path.home()) + '/project/ImageController/input/image' + '.jpg', 'wb+') as f:
            f.write(image)

        with open(str(Path.home()) + '/project/ImageController/input/style' + '.jpg', 'wb+') as f:
            f.write(style)

        # start job
        handle_job(job['jobId'])    





main()

