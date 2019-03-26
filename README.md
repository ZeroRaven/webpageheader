# webpageheader
Use the http.client package to read the contents of the www.uci.edu top level web page and print out the first 3 lines. You will need to use http.client.HTTPSConnection() to make the connection to the www.uci.edu web page. Then you will need to use conn.request("GET", "/") to send the get request. Then use conn.getresponse() to extract the response and use the read() method of the response to return the contents of the webpage.
![2019-03-26-135532_1360x768_scrot](https://user-images.githubusercontent.com/11957243/55003035-7ae28180-4fcf-11e9-97a7-5fb58730bb0a.png)
