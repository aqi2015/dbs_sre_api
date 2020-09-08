"""
@File    : test_create_pod.py
@Time    : 2020/7/22 4:17 下午
@Author  : Akiqi
@Email   : linqi03@beyondsoft.com
@Software: PyCharm
"""

import kubernetes
import uuid
import time

from kubernetes import client, config
from kubernetes.client.api import core_v1_api


def id_generator(name):
    return name + "-" + str(uuid.uuid3(uuid.NAMESPACE_DNS, str(time.time())))


namespace='ada-auto'
name = id_generator('alluxio')
container_image = "alluxio-shell-worker:latest"
container_name = "jobcontainer"
command = ['python3', '/alluxio_worker.py']
args = ["mkdir /test_dir"]

config.load_kube_config(config_file="../kubeconfig.yaml")
# Body is the object Body
body = client.V1Job(api_version="batch/v1", kind="Job")
# Body needs Metadata
# Attention: Each JOB must have a different name!
body.metadata = client.V1ObjectMeta(namespace=namespace, name=name)
# And a Status
body.status = client.V1JobStatus()
# Now we start with the Template...
template = client.V1PodTemplate()
template.template = client.V1PodTemplateSpec()
# Passing Arguments in Env:
# env_list = []
# for env_name, env_value in {}:
#     env_list.append(client.V1EnvVar(name=env_name, value=env_value))
container = client.V1Container(args=args, command=command, image=container_image, image_pull_policy="IfNotPresent",
                               name=container_name)

template.template.spec = client.V1PodSpec(containers=[container], restart_policy='Never')
# And finaly we can create our V1JobSpec!
body.spec = client.V1JobSpec(ttl_seconds_after_finished=600, template=template.template)

configuration = kubernetes.client.Configuration()
api_instance = kubernetes.client.BatchV1Api(kubernetes.client.ApiClient(configuration))
api_response = api_instance.create_namespaced_job(namespace=namespace, body=body, pretty=True)

print(api_response.to_str())