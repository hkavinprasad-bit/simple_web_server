from http.server import HTTPServer,BaseHTTPRequestHandler
content ='''<html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 50px auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
        .title {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 24px;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="title">
        TCP/IP Protocol Suite
    </div>
    <table>
        <thead>
            <tr>
                <th>Layer</th>
                <th>Protocol</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Application Layer</td>
                <td>HTTP, FTP, SMTP, DNS</td>
                <td>Protocols used for communication between applications over a network.</td>
            </tr>
            <tr>
                <td>Transport Layer</td>
                <td>TCP, UDP</td>
                <td>Protocols that provide communication services directly to the application layer.</td>
            </tr>
            <tr>
                <td>Internet Layer</td>
                <td>IP, ICMP, ARP</td>
                <td>Protocols responsible for routing and addressing packets on a network.</td>
            </tr>
            <tr>
                <td>Link Layer</td>
                <td>Ethernet, PPP</td>
                <td>Protocols responsible for data transmission over physical media like cables and wireless.</td>
            </tr>
        </tbody>
    </table>
</div>

</body>
</html>

</html>'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()