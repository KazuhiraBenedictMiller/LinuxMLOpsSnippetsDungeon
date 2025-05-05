<img src="/pics/Kubernetes.png">

## ▪️ Kubernetes ☸️

**Kubernetes in a Nutshell:**

* You define your desired state (Deployments, Services, ConfigMaps, etc.) in YAML manifests.
* You apply those manifests to a cluster (here using **kind** and **kubectl**).
* Kubernetes constantly reconciles actual state (running Pods, Services) to match desired state.
* You can scale, roll out updates, roll back, and inspect resources without rebuilding container images.

---

### 🔧 Installation & Setup

#### 1. Install `kubectl`

```bash
# macOS (Homebrew)
brew install kubectl

# Linux (apt)
sudo apt-get update && sudo apt-get install -y kubectl

# Windows (Chocolatey)
choco install kubernetes-cli
```

Verify:

```bash
kubectl version --client --short
```

#### 2. Install `kind` (Kubernetes in Docker)

```bash
# macOS (Homebrew)
brew install kind

# Linux
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
chmod +x ./kind && sudo mv ./kind /usr/local/bin/kind
```

Verify:

```bash
kind version
```

---

## 🚀 Create & Manage Clusters with kind

1. Create a single-node cluster:

   ```bash
   kind create cluster --name dev-cluster
   ```
2. List existing clusters:

   ```bash
   kind get clusters
   ```
3. Delete a cluster:

   ```bash
   kind delete cluster --name dev-cluster
   ```
4. Multi-node cluster (1 control-plane, 2 workers):

   ```yaml
   # kind-multi-node.yaml
   kind: Cluster
   apiVersion: kind.x-k8s.io/v1alpha4
   nodes:
     - role: control-plane
     - role: worker
     - role: worker
   ```

   ```bash
   kind create cluster --config kind-multi-node.yaml
   ```

---

## 📦 Working with Manifests

1. **Deployment** (`nginx-deployment.yaml`):

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-deployment
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
           - name: nginx
             image: nginx:stable
             ports:
               - containerPort: 80
   ```

   ```bash
   kubectl apply -f nginx-deployment.yaml
   ```

2. **Service** (`nginx-service.yaml`):

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: nginx-service
   spec:
     type: NodePort
     selector:
       app: nginx
     ports:
       - port: 80
         targetPort: 80
         nodePort: 30080
   ```

   ```bash
   kubectl apply -f nginx-service.yaml
   ```

3. **Ingress** (optional, with an ingress controller):

   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: nginx-ingress
   spec:
     rules:
       - host: localhost
         http:
           paths:
             - path: /
               pathType: Prefix
               backend:
                 service:
                   name: nginx-service
                   port:
                     number: 80
   ```

   ```bash
   kubectl apply -f nginx-ingress.yaml
   ```

4. **Inspect resources**:

   ```bash
   kubectl get deployments,svc,ingress
   kubectl get pods
   ```

5. **Logs & Exec**:

   ```bash
   kubectl logs <pod-name>
   kubectl exec -it <pod-name> -- /bin/sh
   ```

6. **Delete**:

   ```bash
   kubectl delete -f nginx-ingress.yaml
   kubectl delete -f nginx-service.yaml
   kubectl delete -f nginx-deployment.yaml
   ```

---

## ⚙️ Contexts, Namespaces & Config

* **Namespaces** isolate resources:

  ```bash
  kubectl create namespace dev
  kubectl config set-context --current --namespace=dev
  ```
* **Contexts** switch between clusters/users:

  ```bash
  kubectl config get-contexts
  kubectl config use-context kind-dev-cluster
  ```
* **ConfigMaps & Secrets**:

  ```bash
  kubectl create configmap app-config --from-file=./config/
  kubectl create secret generic db-creds --from-literal=username=admin --from-literal=password=secret
  ```
* **Kustomize** (built-in):

  ```bash
  kubectl kustomize ./overlays/dev | kubectl apply -f -
  ```

---

## 🌐 Networking & Load Balancing

* **Service Types**:

  * **ClusterIP** (default, internal)
  * **NodePort** (opens port on all nodes)
  * **LoadBalancer** (cloud provider LB)

* **Port Forwarding** (dev):

  ```bash
  kubectl port-forward svc/nginx-service 8080:80
  ```

* **Ingress Controllers** (NGINX, Traefik)

---

## 💾 Storage: Stateful & Ephemeral

* **PersistentVolume (PV)** & **PersistentVolumeClaim (PVC)**:

  ```yaml
  apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
    name: data-pvc
  spec:
    accessModes: ["ReadWriteOnce"]
    resources:
      requests:
        storage: 1Gi
  ```

  ```bash
  kubectl apply -f pvc.yaml
  ```
* **Mount in Pod**:

  ```yaml
  spec:
    volumes:
      - name: data
        persistentVolumeClaim:
          claimName: data-pvc
    containers:
      - name: app
        image: myapp
        volumeMounts:
          - mountPath: /data
            name: data
  ```

---

## 📈 Autoscaling & Rollouts

* **Horizontal Pod Autoscaler (HPA)**:

  ```bash
  kubectl autoscale deployment nginx-deployment --min=3 --max=10 --cpu-percent=50
  ```
* **Rollouts**:

  ```bash
  kubectl rollout status deployment/nginx-deployment
  kubectl rollout undo deployment/nginx-deployment
  ```
* **Rolling Update Strategy**:

  ```yaml
  spec:
    strategy:
      type: RollingUpdate
      rollingUpdate:
        maxSurge: 1
        maxUnavailable: 1
  ```

---

## 🛠️ Troubleshooting & Edge Cases

* **Events & Descriptions**:

  ```bash
  kubectl describe pod <pod>
  kubectl get events --sort-by='.metadata.creationTimestamp'
  ```
* **Resource Usage** (requires metrics-server):

  ```bash
  kubectl top nodes
  kubectl top pods
  ```
* **Debugging**:

  * `kubectl debug -it pod/<name> --image=busybox`
  * `kubectl cp <pod>:/path/to/file ./file`

---

## 🔄 Backup & Restore

* **Velero** for backup/restore:

  ```bash
  velero install --provider aws --bucket my-bucket --secret-file ./credentials-velero
  velero backup create backup-$(date +%Y%m%d)
  velero restore create --from-backup backup-20250505
  ```

---

## ⚡ Expanded Cheatsheet

| Command                                        | Description                                       |
| ---------------------------------------------- | ------------------------------------------------- |
| `kind create cluster`                          | Create a new kind cluster                         |
| `kind delete cluster`                          | Delete a kind cluster                             |
| `kubectl apply -f <file>`                      | Apply manifest                                    |
| `kubectl get pods,svc,deploy -A`               | List pods, services, deployments (all namespaces) |
| `kubectl describe <resource> <name>`           | Detailed info on resource                         |
| `kubectl logs <pod>`                           | View logs                                         |
| `kubectl exec -it <pod> -- sh`                 | Exec into container                               |
| `kubectl port-forward <res> <local>:<remote>`  | Forward port                                      |
| `kubectl scale deployment/<name> --replicas=N` | Scale replicas                                    |
| `kubectl delete -f <file>`                     | Delete resources defined in file                  |
| `kubectl config use-context <ctx>`             | Switch context                                    |
| `kubectl create namespace <ns>`                | Create namespace                                  |
| `kubectl rollout undo deployment/<name>`       | Rollback deployment                               |
| `kubectl patch <res> -p '<json>'`              | Patch resource                                    |
| `kubectl debug`                                | Start ephemeral container for debugging           |
| `kubectl top nodes`                            | Show node metrics                                 |
| `kubectl top pods`                             | Show pod metrics                                  |
| `kubectl get pvc`                              | List PVCs                                         |
| `kubectl describe ingress <name>`              | Describe Ingress                                  |

---

Official Kubernetes Docs: [https://kubernetes.io/docs/](https://kubernetes.io/docs/)
Kind Quickstart: [https://kind.sigs.k8s.io/](https://kind.sigs.k8s.io/)
Velero Docs: [https://velero.io/docs/](https://velero.io/docs/)
