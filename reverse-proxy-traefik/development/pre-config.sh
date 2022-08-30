
# Create a certificate authority (CA) with openssl

mkdir ca

# generate private key
openssl genrsa -aes256 -out ca/ca.key 4096

# generate a CA certificate
openssl req -new -x509 -sha256 -days 1095 -key ca/ca.key -out ca/ca.crt

# Now you can generate the client certificate

mkdir client

# generate private key
openssl genrsa -out client/client.key 4096

# generate a Certificate Signing Request (CSR)
openssl req -new -key client/client.key -sha256 -out client/client.csr

# generate the client certificate
openssl x509 -req -days 365 -sha256 -in client/client.csr -CA ca/ca.crt -CAkey ca/ca.key -set_serial 1 -out client/client.crt

# generate the .p12 (certificate + key)
openssl pkcs12 -export -clcerts -in client/client.crt -inkey client/client.key -out client/client.p12


# test with 

curl -sv https://whoami.example.com --cert client/client.crt --key client/client.key

# now install the cert.p15 file in your browser and try to access the webpage


























