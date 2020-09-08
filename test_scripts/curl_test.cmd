curl http://10.211.55.10:5000/task/alluxio -X POST -d @create_dir.json -H "Content-Type: application/json"
curl http://10.211.55.10:5000/task/alluxio -X POST -d @create_file.json -H "Content-Type: application/json"
curl http://10.211.55.10:5000/task/alluxio -X POST -d @delete.json -H "Content-Type: application/json"
