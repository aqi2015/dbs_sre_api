"""
@File    : test_create_pod.py
@Time    : 2020/7/22 4:17 下午
@Author  : Akiqi
@Email   : linqi03@beyondsoft.com
@Software: PyCharm
"""

from kubernetes import client, config
from kubernetes.client.api import core_v1_api

# argv = '''{'requestor': 'amp', 'worker': 'alluxio', 'action': 'write_file', 'task_id': 'SAAB-001', 'payload': '{"path": "/test01", "content": "test01 content\\n"}', 'name': 'alluxio01', 'admin': 'Rohit'}'''
argv = {
    "host": "10.211.55.5",
    "port": 39999,
    "requestor": "amp",
    "worker": "alluxio",
    "action": "write_file",
    "task_id": "SAAB-001",
    "payload": json.dumps({"path": "/test01", "content": "test01 content\n"}),
    "name": "alluxio01",
    "admin": "Rohit"
}
# argv = json.dumps(argv)

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(config_file="kubeconfig.yaml")
# core_v1 = core_v1_api.CoreV1Api()
# name = 'busybox-test'
# resp = None
# resp = core_v1.read_namespaced_pod(name=name, namespace='default')
#
# sys.exit()

# 获取API的CoreV1Api版本对象
v1 = client.CoreV1Api()

pod = client.V1Pod()
env_list = list()
env_list.append(client.V1EnvVar(name="ALLUXIO_ARGS", value=argv))
container = client.V1Container(env=env_list, image="alluxio-worker:latest", image_pull_policy="Never", name="test")
# container.image="alluxio-worker"
# container.args=["sleep", "3600"]
# container.name="busybox"

spec = client.V1PodSpec(containers=[container])
pod.metadata = client.V1ObjectMeta(name="test")

# spec.containers = [container]
pod.spec = spec

ret = v1.list_namespaced_pod(namespace="default")
for i in ret.items:
    print("%s  %s  %s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

v1.create_namespaced_pod(namespace="default", body=pod)

ret = v1.list_namespaced_pod(namespace="default")
for i in ret.items:
    print("%s  %s  %s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

# v1.delete_namespaced_pod(name="busybox", namespace="default", body=client.V1DeleteOptions())
