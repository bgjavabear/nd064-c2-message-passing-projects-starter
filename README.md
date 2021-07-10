# UdaConnect

## How to run

1. Launch virtual machine

```shell
vagrant up
```

2. ssh into the machine and execute the following command

For some reason I have to execute it on my local machine, otherwise it does not work.

```shell
vagrant ssh
sudo su -
zypper in -t pattern apparmor
```

3. copy the content of k3s.yaml file

```shell
cat /etc/rancher/k3s/k3s.yaml
```

4. copy the content into ~/.kube/config file

```shell
nano ~/.kube/config
```

5. create all kubernetes resources

```shell
### Steps

1. `kubectl apply -f deployment/db-configmap.yaml` - Set up environment variables for the pods
2. `kubectl apply -f deployment/db-secret.yaml` - Set up secrets for the pods
3. `kubectl apply -f deployment/postgres.yaml` - Set up a Postgres database running PostGIS
4. `kubectl apply -f deployment/kafka-configmap.yaml` - Set up env variables for kafka pods
5. `kubectl apply -f deployment/zookeeper.yaml` - Set up a Zookeeper for Kafka
6. `kubectl apply -f deployment/kafka.yaml` - set up kafka
7. `kubectl apply -f deployment` - set up the remain resources 
```

6. copy the name of postgres pod

```shell
kubectl get po 
```

7. initialize the database

```shell
sh scripts/run_db_command.sh <POD_NAME>
```

8. Access UI application by going to 

```shell
localhost:30000
```