import tkinter as tk
import cv2
import numpy as np
import tensorflow as tf
from tkinter import Button
from PIL import Image, ImageDraw

def save_canvas():
    global image
    filename = 'drawing.png'
    image.save(filename)

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((28, 28), Image.LANCZOS) # Resize to 28x28
    image.save("drawing.png")
    image = cv2.imread("drawing.png")[:, :, 0]
    image_array = np.array([image])
    image_array = np.invert(image_array)
    return image_array

def load_model():
    model = tf.keras.models.load_model('mnist_model.model')
    return model

def predict_number():
    image_path = 'drawing.png'
    model = load_model()
    processed_image = preprocess_image(image_path)
    prediction = model.predict(processed_image)
    print(np.argmax(prediction))
    print(prediction)
    return np.argmax(prediction)

def paint(event):
    global last_x, last_y

    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y, fill='black', width=20)
        draw.line([last_x, last_y, event.x, event.y], fill='black', width=20)

    last_x = event.x
    last_y = event.y

def clear_last_position():
    global last_x, last_y
    
    last_x = None
    last_y = None
    
def clear_image():
    global canvas, draw
    canvas.create_rectangle(0, 0, 300, 300, fill='white')
    draw.rectangle([0, 0, 300, 300], fill='white')
  
app = tk.Tk()
app.title('Drawing App')

# canvas
canvas = tk.Canvas(app, bg='white', width=300, height=300)
canvas.pack()
canvas.bind('<B1-Motion>', paint)
canvas.bind('<ButtonRelease-1>', lambda e: clear_last_position())

image = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(image)

last_x = None
last_y = None

# buttons
button_save = Button(text='Save', command=save_canvas)
button_save.pack()

button_predict = Button(text='Predict', command=predict_number)
button_predict.pack()

button_clear = Button(text='Clear Image', command=clear_image)
button_clear.pack()

app.mainloop()