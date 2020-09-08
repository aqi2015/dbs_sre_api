"""
@File    : alluxio_worker.py
@Time    : 2020/7/17 2:30 下午
@Author  : Akiqi
@Email   : linqi03@beyondsoft.com
@Software: PyCharm
"""
import json
import subprocess
# import sys

from flask import Flask, request
from flask_restful import Api, Resource
# from services import kubernetesService as k8s
# from kubernetes import client, config, utils

# import kubernetes
# import kubernetes.client
# import time


response_405 = {
    'status': 405,
    'description': 'Invalid input'
}

class Task(Resource):

    def post(self, worker=None):

        # 构建新参数
        if not worker:
            worker = request.form.get('worker')
        # print('worker: %s' % worker)

        if not worker:
            return response_405

        requestor = request.form.get('requestor')
        # worker = request.form.get('worker')
        action = request.form.get('action')
        task_id = request.form.get('task_id')
        payload = request.form.get('payload')
        name = request.form.get('name')
        admin = request.form.get('admin')

        if worker == "alluxio":
            args = {
                "host": "10.211.55.5",
                "port": 39999,
                "requestor": requestor,
                "worker": worker,
                "action": action,
                "task_id": task_id,
                "payload": payload,
                "name": name,
                "admin": admin
            }

            args_serialize = json.dumps(args)
            # print(args_serialize)
            # print("""docker run -d --net=host alluxio-worker '%s'""" % args_serialize)
            print("""docker run -d --net=host -e ALLUXIO_ARGS='%s' % args_serialize alluxio-worker""")
            # (status, output) = subprocess.getstatusoutput("""docker run -d --net=host alluxio-worker '%s'""" % args_serialize)
            (status, output) = subprocess.getstatusoutput("""docker run -d --net=host -e ALLUXIO_ARGS='%s'  alluxio-worker""" % args_serialize)

            # (status, output) = subprocess.getstatusoutput("""cd /root/k8s/dockerfile/alluxio_worker \
            # && ALLUXIO_ARGS='%s' \
            # && python3 alluxio_worker.py""" % args_serialize)
            print(status)
            print(output)

            if status == 0:
                response = {
                    'status': 200,
                    'description': 'OK'
                }
            else:
                response = {
                    'status': 500,
                    'description': output
                }

            return response
        else:
            return response_405

        # Configs can be set in Configuration class directly or using helper utility
        #config.load_incluster_config()
#        config.load_kube_config(config_file="kubeconfig.yaml")
#        configuration = kubernetes.client.Configuration()
#       api_instance = kubernetes.client.BatchV1Api(kubernetes.client.ApiClient(configuration))

#        v1 = client.CoreV1Api()
#        print("Listing pods with their IPs:")
#        ret = v1.list_pod_for_all_namespaces(watch=False)
        # for i in ret.items:
        #     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
#        k8s.kube_create_job(worker)


if __name__ == '__main__':
    pass
    # taskpost = TaskPost()
    # taskpost.post('test')
    # config.load_kube_config(config_file="../kubeconfig.yaml")

