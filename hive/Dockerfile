FROM myhive-base:latest
# centos:8

# Using the root user
# USER root
# RUN  yum install -y gcc gcc-c++ libffi-devel python3-devel python3-pip python3-wheel openssl-devel cyrus-sasl-plain  cyrus-sasl-devel  cyrus-sasl-gssapi openldap-devel  && \
#    alternatives --set python /usr/bin/python3 && \
#    alternatives --install /usr/bin/pip pip /usr/bin/pip3 100 && \
#    pip install pyhive \
#                thrift \
#                sasl \
#                thrift_sasl

# 指定运行目录
# Specify the run directory
WORKDIR /app

COPY * /app/

RUN ls /app/

# RUN cat -n  /app/hive_worker_docker.py

ARG tb_action
ARG tb_name
ARG hostname
ARG port
ARG databases
ARG env_variable
ARG pay_load

ENV tb_action=${tb_action} \
    tb_name=${tb_name} \
    hostname=${hostname} \
    port=${port} \
    databases=${databases} \
    env_variable=${env_variable} \
    pay_load=${pay_load}

# RUN echo ' env_variable = ' $env_variable

RUN ls /app/
EXPOSE 10000
ENTRYPOINT ["python","/app/hive_worker_docker.py"]