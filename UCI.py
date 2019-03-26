import http.client
conn = http.client.HTTPSConnection("www.uci.edu")
conn.request("GET", "/")
rsp = conn.getresponse()
print(rsp.status, rsp.reason) # Prints that the request went through
data = rsp.read()
print (data[:1000]) #Prints 1000 bytes