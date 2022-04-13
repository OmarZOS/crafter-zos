#!/bin/bash

# #installing
# sudo apt install openssl

#Generate private key and certificate signing request
openssl genrsa -aes256 -passout pass:gsahdg -out server.pass.key 4096

openssl rsa -passin pass:gsahdg -in server.pass.key -out server.key

rm server.pass.key

openssl req -new -key server.key -out server.csr \
    -subj "/C=DZ/ST=Algiers/L=Algiers/O=Zos/OU=IT Department/CN=localhost"

#Generate SSL certificate
openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt

# # adding your certificate into ubuntu certificates..
# sudo mkdir -p /usr/local/share/ca-certificates/extra


# sudo cp server.crt /usr/local/share/ca-certificates/extra

# # reconfiguring the path to certificates
# sudo dpkg-reconfigure ca-certificates

# # # To do this non-interactively, run:

# # sudo update-ca-certificates

# # then, in chrome: add authority