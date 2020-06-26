
from http.server import BaseHTTPRequestHandler, HTTPServer
import pyautogui
import keyboard
from pynput.keyboard import Controller, Key

hostName = "0.0.0.0"
serverPort = 8080
controller = Controller()

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<form action='request.py'>", 'utf-8'))
        self.wfile.write(bytes("<button value='z' type='submit' name='button'>z</button>", "utf-8"))
        self.wfile.write(bytes("<button value='q' type='submit' name='button'>q</button>", "utf-8"))
        self.wfile.write(bytes("<button value='a' type='submit' name='button'>a</button>", "utf-8"))
        self.wfile.write(bytes("<button value='1' type='submit' name='button'>1</button>", "utf-8"))
        self.wfile.write(bytes("<button value='esc' type='submit' name='button'>Esc</button>", "utf-8"))
        self.wfile.write(bytes("<button value='tab' type='submit' name='button'>Tab</button>", "utf-8"))
        self.wfile.write(bytes("<button value='|' type='submit' name='button'>|</button>", "utf-8"))
        self.wfile.write(bytes("<button value='f1' type='submit' name='button'>F1</button>", "utf-8"))
        self.wfile.write(bytes("<button value='f2' type='submit' name='button'>F2</button>", "utf-8"))
        self.wfile.write(bytes("</form>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

        if self.path != '/favicon.ico':
            letter = self.path.split('=')
            print(letter[-1])
            if (letter[-1] != 'f1') & (letter[-1] != 'f2'):
                keyboard.press_and_release(letter[-1])
            else:
                pyautogui.press(letter[-1])

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
