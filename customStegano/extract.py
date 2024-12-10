from stegano import lsb
import shutil
import os

def create_original_images_folder():
    if not os.path.exists("original_images"):
        os.makedirs("original_images")

def extract_message(image_path):
    try:
        message = lsb.reveal(image_path)
        
        if message:
            print(f"Повідомлення: {message}")
        else:
            print("Повідомлення не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

def create_restored_images_folder():
    if not os.path.exists("restored_images"):
        os.makedirs("restored_images")

def restore_original_image(steg_container_path):
    try:
        create_restored_images_folder()
        
        original_image_name = f"original_{os.path.basename(steg_container_path)[5:]}"
        original_image_path = os.path.join("original_images", original_image_name)
        
        print(f"Шлях до оригінального зображення: {original_image_path}")
        
        if not os.path.exists(original_image_path):
            print(f"Оригінальне зображення не знайдено за шляхом {original_image_path}.")
            return
        
        restored_image_path = os.path.join("restored_images", f"restored_{original_image_name}")
        
        shutil.copy(original_image_path, restored_image_path)
        print(f"Оригінальне зображення відновлено як '{restored_image_path}'")
    
    except Exception as e:
        print(f"Помилка: {e}")
