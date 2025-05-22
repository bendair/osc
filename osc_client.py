from pythonosc import dispatcher, osc_server, udp_client
import threading
import time

current_timecode = "00:00:00:00"

def update_timecode(address, *args):
    global current_timecode
    current_timecode = args[0]
    print(f"[Timecode Synced] {current_timecode}")

def main():
    # Client for sending triggers and cues
    server_ip = "127.0.0.1"
    server_port = 5005
    client = udp_client.SimpleUDPClient(server_ip, server_port)

    # Set up dispatcher for receiving timecode
    disp = dispatcher.Dispatcher()
    disp.map("/sync/timecode", update_timecode)

    # Client listening server (for receiving timecode)
    client_ip = "127.0.0.1"
    client_port = 5006
    server = osc_server.ThreadingOSCUDPServer((client_ip, client_port), disp)

    # Start server thread for listening to timecode
    threading.Thread(target=server.serve_forever, daemon=True).start()

    # Example: Sending triggers and cues with & without timecode
    while True:
        print("\nSending messages to server...\n")

        # Trigger without timecode
        client.send_message("/trigger/action", ["Play sound effect"])
        print("Sent trigger (no timecode)")

        # Cue without timecode
        client.send_message("/cue/lighting", ["Scene Bright"])
        print("Sent cue (no timecode)")

        # Trigger with synchronized timecode
        client.send_message("/trigger/action_tc", ["Start playback", current_timecode])
        print(f"Sent trigger with timecode: {current_timecode}")

        # Cue with synchronized timecode
        client.send_message("/cue/video_tc", ["Intro video cue", current_timecode])
        print(f"Sent cue with timecode: {current_timecode}")

        time.sleep(5)

if __name__ == "__main__":
    main()
