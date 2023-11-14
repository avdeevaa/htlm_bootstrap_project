
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


hostName = "localhost"
serverPort = 8080

# with open('index.html', encoding='utf-8') as page:
#     page_content = page.read()
#     print(page_content)


class MyServer(BaseHTTPRequestHandler):


    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        with open('index.html', encoding='utf-8') as page:
            page_content = page.read()

            self.send_response(200)  # Отправка кода ответа
            self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
            self.end_headers()  # Завершение формирования заголовков ответа
            self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")