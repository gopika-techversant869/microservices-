from flask import Flask, request, Response
import requests

app = Flask(__name__)

MICROSERVICES = {
    "card": "http://gopay.com:5000",
    "wallet":"http://gopay.com:5002"
}

@app.route('/<service>/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
def proxy(service, path):
    
    if service not in MICROSERVICES:
        return {"error": "Unknown service"}, 404
    try:
        url = f"{MICROSERVICES[service]}/{path}"
    except Exception as e:
       
        return {"error": "Invalid URL"}, 400

    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for key, value in request.headers},
        data=request.get_data()
    )
  
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
