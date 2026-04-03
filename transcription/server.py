# server.py
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "1"
from whisper_live.server import TranscriptionServer

server = TranscriptionServer()
server.run(host="0.0.0.0", port=9090, backend="faster_whisper")