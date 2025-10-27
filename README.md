<h1 align="center">🚗 License Plate Detection & Visualization</h1>

<p align="center">
<b>This is a classic</b> — An end-to-end License Plate Detection and Recognition system powered by <b>YOLOv8</b>, <b>EasyOCR</b>, and <b>OpenCV</b>.  
It detects license plates in real-time, extracts text, handles missing data, and visualizes results with bounding boxes and dynamic annotations.
</p>

<hr>

<h2>🧠 Overview</h2>
<p>
This project demonstrates a complete computer vision pipeline for automatic license plate detection and recognition.  
It captures plates from video or image feeds, detects them using <b>YOLOv8</b>, performs text extraction via <b>EasyOCR</b>, cleans incomplete data, and visualizes the recognized results with bounding boxes and readable annotations.
</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li><b>Real-Time Detection:</b> Detects license plates in images and video feeds using YOLOv8.</li>
  <li><b>Text Recognition:</b> Uses EasyOCR to extract text from detected license plates accurately.</li>
  <li><b>Data Correction:</b> Automatically fills missing or noisy frame data for consistent tracking.</li>
  <li><b>Dynamic Visualization:</b> Displays results with bounding boxes and plate numbers in real-time.</li>
  <li><b>Logging System:</b> Exports all detected plate data to a CSV file for record-keeping.</li>
  <li><b>Modular Design:</b> Separate modules for detection, visualization, utilities, and data cleanup.</li>
</ul>

<hr>

<h2>🧩 Project Modules</h2>
<ul>
  <li><code>main.py</code> — Orchestrates the entire detection, OCR, and visualization pipeline.</li>
  <li><code>add_missing_data.py</code> — Cleans and fills missing or noisy detection data.</li>
  <li><code>util.py</code> — Contains helper functions for text parsing and result formatting.</li>
  <li><code>visualize.py</code> — Handles all visualization and output display functions.</li>
</ul>

<hr>

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

<hr>

<h2>⚙️ Installation</h2>

<pre>
git clone https://github.com/Niklaus2003/License-Plate-Detection.git
cd License-Plate-Detection
pip install -r requirements.txt
</pre>

<hr>

<h2>🚀 Usage</h2>

<pre>
python main.py
</pre>

<p>
Place your image or video file in the project directory, set its path in <code>main.py</code>, and run the script.  
The program will detect license plates, extract the text, visualize the bounding boxes, and save results to a CSV file.
</p>

<hr>

<h2>📊 Output</h2>
<ul>
  <li>Plates detected and highlighted in real-time with bounding boxes.</li>
  <li>Extracted license text displayed dynamically on each frame.</li>
  <li>CSV file containing timestamps and recognized text entries.</li>
</ul>

<hr>

<h2>💡 What I Learned</h2>
<ul>
  <li>Building modular, scalable computer vision pipelines.</li>
  <li>Integrating object detection with OCR for end-to-end automation.</li>
  <li>Handling noisy frame data and automating cleanup with Python.</li>
  <li>Real-time visualization and OpenCV optimization techniques.</li>
</ul>

<hr>

<h2>🔮 Future Enhancements</h2>
<ul>
  <li>📱 Web dashboard for live detection visualization.</li>
  <li>☁️ Cloud integration for real-time camera feeds.</li>
  <li>⚡ GPU-based acceleration for faster inference.</li>
  <li>🚘 Vehicle database linking for ownership validation.</li>
  <li>🧩 Integration with parking and toll management systems.</li>
</ul>

<hr>

<h2>📜 License</h2>
<p>This project is released under the <b>MIT License</b>.</p>

<hr>

<h3 align="center">🌟 Made with Passion for AI & Computer Vision 🚀</h3>
