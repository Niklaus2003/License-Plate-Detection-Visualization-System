<h1 align="center">🚗 License Plate Detection & Visualization</h1>

<p align="center">
A classic end-to-end License Plate Detection and Recognition system using <b>YOLOv8</b>, <b>EasyOCR</b>, and <b>OpenCV</b>.
</p>

---

<h2>🧠 Overview</h2>
<p>
This project automates license plate detection and recognition from video or image feeds.  
Using <b>YOLOv8</b> for detection and <b>EasyOCR</b> for text extraction, it identifies license plates in real-time, corrects missing data, and visualizes the results with bounding boxes and recognized text overlays.
</p>

---

<h2>✨ Features</h2>
<ul>
  <li><b>Real-Time Detection:</b> Detects license plates from video streams or images using YOLOv8.</li>
  <li><b>OCR Text Extraction:</b> Reads and formats text from detected plates with EasyOCR.</li>
  <li><b>Data Cleaning:</b> Automatically fills missing or inconsistent frame data for accuracy.</li>
  <li><b>Visualization:</b> Draws bounding boxes, displays recognized text, and provides a live view of detections.</li>
  <li><b>CSV Logging:</b> Exports detected plate data with timestamps for record keeping.</li>
  <li><b>Modular Code Design:</b> Clear separation of detection, OCR, visualization, and data handling.</li>
</ul>

---

<h2>🧩 Project Modules</h2>
<ul>
  <li><code>main.py</code> – Main driver for detection, OCR, and pipeline coordination.</li>
  <li><code>add_missing_data.py</code> – Cleans and fills missing or noisy detection data.</li>
  <li><code>util.py</code> – Helper functions for text parsing, accuracy tracking, and bounding box formatting.</li>
  <li><code>visualize.py</code> – Handles dynamic visualization and real-time display of detections.</li>
</ul>

---

<h2>🧰 Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>YOLOv8 (Ultralytics)</li>
  <li>EasyOCR</li>
  <li>OpenCV</li>
  <li>NumPy</li>
  <li>Pandas</li>
  <li>Matplotlib</li>
</ul>

---

<h2>⚙️ Installation</h2>

```bash
git clone https://github.com/Niklaus2003/License-Plate-Detection.git
cd License-Plate-Detection
pip install -r requirements.txt
