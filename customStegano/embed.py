import os
import shutil
from stegano import lsb

def create_original_images_folder():
    if not os.path.exists("original_images"):
        os.makedirs("original_images")

def embed_message(image_path, message):
    try:
        create_original_images_folder()

        original_image_name = f"original_{os.path.basename(image_path)}"
        original_image_path = os.path.join("original_images", original_image_name)
        
        if not os.path.exists(original_image_path):
            shutil.copy(image_path, original_image_path)
            print(f"Оригінальне зображення збережено як {original_image_path}")

        steg_image_name = f"steg_{os.path.basename(image_path)}"
        steg_image_path = os.path.join("images", steg_image_name)
        
        encoded_image = lsb.hide(image_path, message)
        encoded_image.save(steg_image_path)  # Зберігаємо стегоконтейнер

        print(f"Повідомлення вбудовано успішно в зображення: {steg_image_path}")
    
    except Exception as e:
        print(f"Помилка: {e}")