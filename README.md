# OSC Server & Client with SMPTE Timecode

This repository provides a practical example of an **Open Sound Control (OSC)** server and client, including synchronized SMPTE-style timecode. It demonstrates cue and trigger messaging with precise timecode synchronization, suitable for multimedia control, live events, and broadcast applications.

---

## 📂 Files

* **`osc_server.py`**: Master OSC server that broadcasts timecode and receives cue/trigger messages.
* **`osc_client.py`**: OSC client that receives synchronized timecode and sends cue/trigger messages.
* **`timecode.py`**: Utility class for generating accurate SMPTE timecode at various standard frame rates.

---

## 🛠️ Installation

Install required Python libraries:

```bash
pip install python-osc
```

---

## 🚀 Running the Example

**1. Run the OSC server (Master):**

```bash
python osc_server.py
```

**2. Run the OSC client (Slave):**

```bash
python osc_client.py
```

The server will continuously broadcast synchronized SMPTE timecode, while the client receives this timecode and sends cue and trigger messages back to the server.

---

## 🎯 How OSC Works

**Open Sound Control (OSC)** is a protocol designed for real-time control and communication between multimedia devices and software. It operates using network packets sent typically via **UDP** (User Datagram Protocol), although it can optionally use TCP for increased reliability.

* **Messages**: OSC uses hierarchical address patterns similar to URLs:

  ```
  /cue/start
  /trigger/playback
  /sync/timecode
  ```

* **Ports**: Commonly used ports for OSC are:

  * `5005`, `5006`, `8000`, `8001`, `9000`, `57120`

* **Connection**: OSC typically uses UDP, providing fast, lightweight, connectionless messaging ideal for live control.

### Example Setup

```
OSC Client
(192.168.0.10) ---> (UDP Port: 5005)

OSC Server
(192.168.0.20 listens on UDP Port: 5005)
```

---

## ⏲️ SMPTE Timecode Support

This implementation supports standard SMPTE video frame rates:

* `23.976`, `24`, `25`, `29.97`, `30`, `50`, `59.94`, `60`

You can set the desired frame rate by modifying the `framerate` parameter in `osc_server.py`:

```python
timecode = SMPTETimecode(framerate=25)
```

---

## 📌 Project Structure

```
OSC Project
│
├── osc_server.py   # Master server for broadcasting timecode
├── osc_client.py   # Client for receiving timecode and sending messages
└── timecode.py     # SMPTE timecode generator utility
```

---

## 📖 License

Feel free to use, modify, and distribute this project as needed. Attribution appreciated!

---
