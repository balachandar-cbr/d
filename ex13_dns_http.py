# Ex 13: DNS Query and HTTP/HTTPS Request Testing
import socket
import urllib.request

domain = input("Enter domain name: ")
try:
    ip_address = socket.gethostbyname(domain)
    print("\nDNS QUERY RESULT")
    print("----------------")
    print("Domain Name :", domain)
    print("IP Address :", ip_address)
except socket.gaierror:
    print("DNS resolution failed.")

url = input("\nEnter HTTP/HTTPS URL: ")
try:
    response = urllib.request.urlopen(url, timeout=10)
    print("\nHTTP/HTTPS REQUEST RESULT")
    print("-------------------------")
    print("URL :", url)
    print("Status Code :", response.status)
    print("Response :", response.read(200).decode("utf-8", errors="ignore"))
except Exception as e:
    print("Request failed:", e)
