from http.server import HTTPServer,BaseHTTPRequestHandler
import logging 
import time

logging.basicConfig(
    filename="/var/log/myapp/app.log",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a'
    )

class MyHandler(BaseHTTPRequestHandler):  #this is a child class we used basehttprequesthandler for inporting
    def do_GET(self): #exclusive method for getrequest
        global is_ready

        if self.path=="/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"{'status':'ok'}")
            return

        if self.path=="/ready":
            if is_ready==True:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"{'ready':'ok'}")
                return
            else:
                self.send_response(503)
                self.end_headers()
                self.wfile.write(b"{'ready':'No'}")
                return


        start = time.time()
        logging.info("Recieved request from %s",self.client_address)
        # while True:
        #     pass
        time.sleep(3)
        duration = time.time() - start
        if duration>1.5:
            is_ready=False
        else:
            is_ready=True

        self.send_response(200)
        self.end_headers() #ends get request and waits for body/subject
        self.wfile.write(b"MyApp is running")  #sends the body in form of bytes
        
        logging.info(f"request_end duration={duration:.4f}s")

server=HTTPServer(("127.0.0.1", 8080),MyHandler)
logging.info("Starting server on port 8080")
server.serve_forever()


# Type :set paste and press Enter.

# Press i to enter Insert mode.