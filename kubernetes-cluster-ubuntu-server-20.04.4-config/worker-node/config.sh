

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

sudo hostnamectl set-hostname worker01 

# Join Worker Node to Cluster
# Switch to the worker system and enter the command you noted from kubeadm join

kubeadm join --discovery-token [...] --discovery-token-ca-cert-hash sha256:1234..cdef [...]































