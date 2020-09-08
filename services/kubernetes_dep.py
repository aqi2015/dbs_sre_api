"""
@File    : kubernetes_dep.py
@Time    : 2020/8/4 4:01 下午
@Author  : Akiqi
@Email   : linqi03@beyondsoft.com
@Software: PyCharm
"""

import kubernetes.client
import time
import uuid

from kubernetes import client, config, utils
from kubernetes.client.rest import ApiException


response_405 = {
    'status': 405,
    'description': 'Invalid input'
}
response_406 = {
    'status': 406,
    'description': 'something (Internal Server ) error'
}


def id_generator(name):
    return name + "-" + str(uuid.uuid3(uuid.NAMESPACE_DNS, str(time.time())))


def create_deployment(worker, input_args, namespace="default"):
    print(worker, input_args, namespace)
    image = worker + "-worker:latest"
    name = id_generator(worker)
    env_vars = {"INPUT_ARGS": input_args}
    env_list = []
    for env_name, env_value in env_vars.items():
        env_list.append(client.V1EnvVar(name=env_name, value=env_value))

    config.load_kube_config(config_file="kubeconfig.yaml")
    apps_v1_api = client.AppsV1Api()
    container = client.V1Container(
        env=env_list,
        name="deployment",
        # image="gcr.io/google-appengine/fluentd-logger",
        image=image,
        image_pull_policy="IfNotPresent",
        ports=[client.V1ContainerPort(container_port=5678)],
    )
    # Template
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": worker}, namespace=namespace, name=name),
        spec=client.V1PodSpec(containers=[container], restart_policy="Always"))  # There is no need to restart here
    # print("Template")
    # print(template)
    # print(template.metadata)
    # Spec
    spec = client.V1DeploymentSpec(
        replicas=1,
        selector={
            "matchLabels": {"app": worker}
        },
        template=template)
    # Deployment
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=name),
        spec=spec)
    # Creation of the Deployment in specified namespace
    # (Can replace "default" with a namespace you may have created)
    res = apps_v1_api.create_namespaced_deployment(
        namespace=namespace, body=deployment
    )
    print('#'*10 + '75')
    print(dir(res))
    print(res.status)
    return res
