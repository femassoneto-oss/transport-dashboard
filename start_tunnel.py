import time
from pyngrok import ngrok

# Open a tunnel on port 8501 (Streamlit default)
public_url = ngrok.connect(8501, "http")
print(f"Public URL: {public_url}")
# Keep tunnel open until user stops
try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    ngrok.disconnect(public_url)
    print("Tunnel closed")
