
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow.keras.preprocessing import image as tf_image
import numpy as np

model=tf.keras.models.load_model("mymodel3.keras")
img_size = (256, 256, 3)

def preprocess_image(img_path, target_size=img_size):
    img = tf_image.load_img(img_path, target_size=target_size)
    img_array = tf_image.img_to_array(img)
    img_array = img_array/255.
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def predict_image(model, img_path):
    preprocessed_img = preprocess_image(img_path)
    predictions = model.predict(preprocessed_img)
    predicted_class = np.argmax(predictions)
    if predicted_class == 0:
        predict_imagename = 'Apple'
        
    elif predicted_class == 1:
        predict_imagename = 'Avocado'

    elif predicted_class == 2:
        predict_imagename = 'Banana'

    elif predicted_class == 3:
        predict_imagename = 'Cherry'

    elif predicted_class == 4:
        predict_imagename = 'Kiwi'

    elif predicted_class == 5:
        predict_imagename = 'Mango'

    elif predicted_class == 6:
        predict_imagename = 'Orange'

    elif predicted_class == 7:
        predict_imagename = 'Pineapple'

    elif predicted_class == 8:
        predict_imagename = 'Strawberries'

    elif predicted_class == 9:
        predict_imagename = 'Watermelon'
    return predict_imagename


def open_file_dialog():
    file_path = filedialog.askopenfilename(title="select file", filetypes=[("png file", "*.png"), ("jpg file", "*.jpg"), ("jpeg file","*.jpeg")
                                                                          ])
    if file_path:
        image = Image.open(file_path)

        image_tk = ImageTk.PhotoImage(image)
        image_label.configure(image=image_tk)
        image_label.image = image_tk
        name_label.configure(text=f"The name of fruit: {predict_image(model,file_path)}")

  
  
# GUI 창 생성
root = tk.Tk()
root.title("fruit recognizer GUI")

image_label = tk.Label( text="Image Display Area")
image_label.pack(pady=10)

# 선택한 파일 경로를 표시할 레이블 생성
name_label = tk.Label(root, text="The name of fruit: ")
name_label.pack(pady =15)

# 파일 선택 버튼 생성
button = tk.Button(root, text="select file", command=open_file_dialog)
button.pack(pady=20)



# GUI 실행
root.mainloop()