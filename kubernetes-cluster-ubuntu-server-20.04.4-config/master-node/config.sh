

sudo apt-get update

sudo apt-get install docker.io

sudo systemctl enable docker

sudo systemctl status docker

sudo systemctl start docker

# Add Kubernetes Signing Key

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add

sudo apt-get install curl

# Add Software Repositories

sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"

# Kubernetes Installation Tools

sudo apt-get install kubeadm kubelet kubectl

sudo apt-mark hold kubeadm kubelet kubectl

kubeadm version

# Begin Kubernetes Deployment

sudo swapoff –a

# Assign Unique Hostname for Each Server Node 


sudo hostnamectl set-hostname master-node 

# Initialize Kubernetes on Master Node
# if facing issues, add the flag --ignore-preflight-errors=all

sudo kubeadm init --pod-network-cidr=10.244.0.0/16

mkdir -p $HOME/.kube

sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Deploy Pod Network to Cluster

sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# Verify that everything is running and communicating:

kubectl get pods --all-namespaces

# To check the nodes, enter:

kubectl get nodes






























