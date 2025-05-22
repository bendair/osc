from pythonosc import dispatcher, osc_server, udp_client
from timecode import SMPTETimecode
import threading
import time

# Master Timecode
timecode = SMPTETimecode(framerate=25)  # Set desired framerate here

def handle_trigger(address, *args):
    print(f"[Trigger Received] {address}: {args}")

def handle_cue(address, *args):
    print(f"[Cue Received] {address}: {args}")

def send_timecode(client):
    while True:
        current_tc = timecode.current_timecode()
        client.send_message("/sync/timecode", current_tc)
        time.sleep(1 / timecode.framerate)

def main():
    disp = dispatcher.Dispatcher()
    disp.map("/trigger/*", handle_trigger)
    disp.map("/cue/*", handle_cue)

    server_ip = "127.0.0.1"
    server_port = 5005

    # OSC server (for receiving messages)
    server = osc_server.ThreadingOSCUDPServer((server_ip, server_port), disp)
    print(f"[Server Running] Listening on {server_ip}:{server_port}")

    # Client (to broadcast timecode)
    client_ip = "127.0.0.1"
    client_port = 5006  # Client listening port
    osc_client = udp_client.SimpleUDPClient(client_ip, client_port)

    # Start timecode broadcast thread
    tc_thread = threading.Thread(target=send_timecode, args=(osc_client,), daemon=True)
    tc_thread.start()

    server.serve_forever()

if __name__ == "__main__":
    main()
