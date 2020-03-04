
# running Nautilus node cheat sheet
## install kubernetes
```
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl

chmod +x ./kubectl

sudo mv ./kubectl /usr/local/bin/kubectl

kubectl version

```

# install Docker 
```
sudo apt install docker.io
```

# log in docker

```
docker login
```
# get base ubuntu image
```
docker pull ubuntu
```
# start container from the ubuntu image
```
docker run -t -d --name base ubuntu
```
# ssh into container 
```
docker exec -it base /bin/bash
```
# leave container 
```
exit
```
# create new image from customized container
docker commit -m "Created example image" -a "Your Name" base YourDockerUsername/example-image:v1

# upload image 
```
docker push YourDockerUsername/example-image:v1
```
# clean up
```
docker stop base
docker rm base
docker rmi YourDockerUsername/example-image:v1
```

# create yaml files create-volume.yaml and jobs.yaml
	check example yaml files

# allocate volume
```
kubectl create -n YourNautilusNamespace -f create-volume.yaml
```
# run docker image in job
```
kubectl create -n YourNautilusNamespace -f jobs.yaml
```
# check running pods
```
kubectl get pods -n YourNautilusNamespace
```
# transfer data to allocation
```
kubectl cp /[PathToYour]/SampleData/ YourNautilusNamespace/example-job:/testvol/SampleData

```
# ssh into jobs
```
kubectl exec -n YourNautilusNamespace -it example-pod -- /bin/bash
```
# delete job
kubectl delete -n msu-stpalab -f ../create_job.yaml

# transfer data out  --> don't need the '/' before testvol/
```
kubectl cp YourNautilusNamespace/example-pod:/testvol/SampleOutput /[YourDesiredPath]/sampleOutput

```
# check storage
```
kubectl get -f create-volume.yaml -n YourNautilusNamespace
```
# delete storage
```
kubectl delete -n YourNautilusNamespace -f create-volume.yaml
```
