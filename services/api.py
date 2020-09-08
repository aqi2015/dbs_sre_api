"""
@File    : api.py
@Time    : 2020/7/17 2:30 下午
@Author  : Akiqi
@Email   : linqi03@beyondsoft.com
@Software: PyCharm
"""

import json

from services import kubernetes_service as k8s
from flask import Flask, request
from flask_restful import Api, Resource

response_405 = {
    'status': 405,
    'description': 'Invalid input'
}

response_406 = {
    'status': 406,
    'description': 'something error '
}

with open('config/k8s_config.json') as f:
    k8s_config = json.load(f)


class Task(Resource):

    def post(self, worker=None):

        try:
            request_data = json.loads(request.get_data().decode('utf-8'))
            print(request_data)
        except Exception as e:
            print(e)
            return response_405

        if worker == None:
            worker = request_data.get('worker')

        # requestor = request_data.get('requestor')
        # action = request_data.get('action')
        args = request_data.get('args')
        # task_id = request_data.get('task_id')
        # payload = request_data.get('payload')
        # name = request_data.get('name')
        # admin = request_data.get('admin')
        imagename = request_data.get("imagename")

        if not worker or not imagename or not args:
            return response_405

        if worker == "alluxio":
            command = ['python3', '/alluxio_worker.py']
            status, r = k8s.kube_create_job(worker, args, command, imagename=imagename,
                                            namespace=k8s_config.get("namespace"))
            response = {
                'status': status,
                'description': r
            }

            return response

        elif worker == "hive":  # jessica
            env_variable = request_data.get("env_variable")
            tb_action = request_data.get('action')
            tb_name = request_data.get('tb_name')
            databases = request_data.get("databases")
            hostname = request_data.get("hostname")
            port = request_data.get("port")
            args = {
                "env_variable": env_variable,
                "tb_action": tb_action,
                "tb_name": tb_name,
                "databases": databases,
                "hostname": "10.211.55.5",
                "port": 10000,
                "requestor": requestor,
                "worker": worker,
                "task_id": task_id,
                "payload": payload,
                "name": name,
                "admin": admin
            }

            args_serialize = json.dumps(args)
            try:
                status, r = k8s.kube_create_job(worker, args_serialize, imagename=imagename,
                                                namespace=k8s_config.get("namespace"))
                if status == 500:
                    return response_406
                else:
                    response = {
                        'status': status,
                        'description': r.to_str()
                    }
                    return response
            except Exception as e:
                print(e)

        else:
            return response_405


if __name__ == '__main__':
    pass
