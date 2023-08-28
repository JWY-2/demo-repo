docker build -t jwy626/demo:latest .
docker login
docker push  jwy626/demo
helm upgrade release-1 --install ./mychart --set apiversion=1.1
helm upgrade release-2 --install ./mychart --set apiversion=1.2
helm list
sleep 5
kubectl get svc | awk '{if ($4 != "<pending>" && NR>1)print $4}'