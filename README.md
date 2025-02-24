# SmartCam - Real-Time Face Detection & Snapshot Manager

SmartCam is a Python-based application that leverages OpenCV for real-time video streaming and face detection, paired with a Tkinter-powered graphical user interface. It allows users to capture snapshots from their webcam feed, view and manage these images, and save or delete them as needed.

## Features

- **Real-Time Video Streaming:** Displays a live feed from your webcam.
- **Face Detection:** Uses Haar Cascade classifiers to detect and highlight faces in the video.
- **Snapshot Capture:** Easily capture images from the live video stream.
- **Image Management:** View, save, or delete captured images through a user-friendly interface.
- **Batch Operations:** Save or delete all captured images with a single click.

## Requirements

- Python 3.x
- [OpenCV](https://opencv.org/) (`opencv-python`)
- [Pillow](https://python-pillow.org/) (`Pillow`)
- Tkinter (typically bundled with Python)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/smartcam.git
   cd smartcam
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**

   ```bash
   python smartcam.py
   ```

2. **Interface Overview:**
   - **Live Video Feed:** The main window displays the real-time video stream from your webcam with detected faces outlined.
   - **Capture Button ("Capturar"):** Click to take a snapshot of the current frame. The image is stored temporarily.
   - **My Images Button ("Mis imágenes"):** Opens a window where you can review all the captured snapshots.
     - **Individual Image Options:**
       - **Save ("Guardar"):** Save the selected snapshot to the `capturas` directory.
       - **Delete ("Eliminar"):** Remove the snapshot from the temporary storage.
     - **Batch Options:**
       - **Save All ("Guardar todo"):** Save all captured images.
       - **Delete All ("Eliminar todo"):** Delete all captured images.
   - **Close Button ("Cerrar"):** Terminate the application.

3. **Image Storage:**
   - Saved images are stored in the `capturas` folder, which is created automatically if it doesn't exist.

## Project Structure

- `smartcam.py`: Main application script that handles video capture, face detection, and the GUI.
- `capturas/`: Directory for storing saved snapshots (automatically generated on first run).

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature/bugfix description"
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request with a detailed description of your changes.

## License

Distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pillow](https://python-pillow.org/)
