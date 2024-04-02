#kubectl delete -f  storage-class.yaml  --namespace ingress-nginx
#kubectl delete -f Azure-pvc.yaml --namespace ingress-nginx
#kubectl delete -f  mysqldb.yml --namespace ingress-nginx
#kubectl delete -f service.yml --namespace ingress-nginx
kubectl apply -f  storage-class.yaml  --namespace ingress-nginx
kubectl apply -f Azure-pvc.yaml --namespace ingress-nginx
kubectl apply -f  mysqldb.yml --namespace ingress-nginx
kubectl apply -f service.yml --namespace ingress-nginx

