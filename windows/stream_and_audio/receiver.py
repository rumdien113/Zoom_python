import videostream
import threading
import socket

from windows.stream_and_audio.videostream import StreamingServer


local_ip = socket.gethostbyname(socket.gethostname())
receiver = StreamingServer(local_ip,9999)
t=threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue
