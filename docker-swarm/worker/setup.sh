cat hosts >> /etc/hosts

# Install dependency packages with the below command
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common lsb-release

# Add docker key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg


# Add docker repository to your hosts with the following commands:
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update packages
sudo apt update

# Install Docker CE on Ubuntu22.04|20.04:
sudo apt install docker-ce

# list interfaces configurations
# ip address

# configure ip address
# ifconfig [interface-name] [ip-address]

# For me the interface for which Docker manager will advertise on is enp0s8

cat env.sh >> .bashrc


sudo docker swarm join [...........]

















