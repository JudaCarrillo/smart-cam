import cv2
import os
import time
import tkinter as tk
from tkinter import Label, Button, Toplevel, messagebox, Frame
from PIL import Image, ImageTk

# Crear carpeta de capturas si no existe
save_path = "capturas"
if not os.path.exists(save_path):
    os.makedirs(save_path)

# array
capturas_temporales = []

# Configurar la cámara
cap = cv2.VideoCapture(0)

# Clasificador de rostros
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Ventana principal
root = tk.Tk()
root.title("Mi cámara")

# Label para video
label = Label(root)
label.pack()


# Actualizar video en la ventana
def update_video():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        label.imgtk = imgtk
        label.configure(image=imgtk)

    label.after(10, update_video)


# Capturar imagen
def take_picture():
    ret, frame = cap.read()
    if ret:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        frame_copy = frame.copy()  # Copia del frame para almacenar
        capturas_temporales.append((timestamp, frame_copy))
        print(f"Imagen guardada temporalmente: {timestamp}")


# Mostrar imágenes capturadas
def show_images():
    ventana = Toplevel(root)
    ventana.title("Mis Imágenes")

    frame_imagenes = Frame(ventana)
    frame_imagenes.pack()

    # Eliminar imagen
    def delete(timestamp, frame):
        try:
            # Eliminar de la lista de capturas temporales
            capturas_temporales[:] = [
                item for item in capturas_temporales if item[0] != timestamp
            ]
            frame.destroy()
            messagebox.showinfo("Éxito", "Imagen eliminada")
        except Exception as e:
            messagebox.showerror("Error", e)

    def save(timestamp, frame):
        try:
            # Buscar la imagen en la lista de capturas temporales
            img_frame = next(
                item[1] for item in capturas_temporales if item[0] == timestamp
            )

            # Guardar la imagen en la carpeta "capturas"
            filename = os.path.join(save_path, f"captura_{timestamp}.jpg")
            cv2.imwrite(filename, img_frame)

            messagebox.showinfo("Éxito", f"Imagen guardada en {filename}")
        except Exception as e:
            messagebox.showerror("Error", e)

    def save_all():
        try:
            for timestamp, img_frame in capturas_temporales:
                filename = os.path.join(save_path, f"captura_{timestamp}.jpg")
                cv2.imwrite(filename, img_frame)
            messagebox.showinfo("Éxito", "Todas las imágenes han sido guardadas.")
        except Exception as e:
            messagebox.showerror("Error", e)

    # Eliminar todas las imágenes
    def delete_all():
        try:
            capturas_temporales.clear()  # Vaciar el array de imágenes temporales
            for widget in frame_imagenes.winfo_children():
                widget.destroy()  # Eliminar las imágenes de la interfaz
            messagebox.showinfo("Éxito", "Todas las imágenes han sido eliminadas.")
        except Exception as e:
            messagebox.showerror("Error", e)

    # Mostrar imágenes con botones
    for timestamp, img_frame in capturas_temporales:
        img = Image.fromarray(img_frame).resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)

        frame = Frame(frame_imagenes)
        frame.pack(side=tk.LEFT, padx=5, pady=5)

        lbl_img = Label(frame, image=img_tk)
        lbl_img.image = img_tk
        lbl_img.pack()

        btn_eliminar = Button(
            frame,
            text="Eliminar",
            command=lambda ts=timestamp, f=frame: delete(ts, f),
        )
        btn_eliminar.pack()

        btn_save = Button(
            frame, text="Guardar", command=lambda ts=timestamp, f=frame: save(ts, f)
        )
        btn_save.pack()

    btn_guardar_todo = Button(ventana, text="Guardar todo", command=save_all)
    btn_guardar_todo.pack(pady=10)

    btn_eliminar_todo = Button(ventana, text="Eliminar todo", command=delete_all)
    btn_eliminar_todo.pack(pady=10)


# Cerrar la aplicación
def close():
    cap.release()
    cv2.destroyAllWindows()
    root.quit()


# Botones
btn_capturar = tk.Button(root, text="Capturar", command=take_picture)
btn_capturar.pack()

btn_ver_imagenes = tk.Button(root, text="Mis imágenes", command=show_images)
btn_ver_imagenes.pack()

btn_salir = tk.Button(root, text="Cerrar", command=close)
btn_salir.pack()

# Iniciar video
update_video()

# Ejecutar
root.mainloop()