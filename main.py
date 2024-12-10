from customStegano.embed import embed_message
from customStegano.extract import extract_message, restore_original_image

def main():
    print("Стеганографія: ")
    print("1. Вбудувати повідомлення")
    print("2. Витягнути повідомлення")
    print("3. Відновити оригінальне зображення")
    choice = input("Введіть вибір (1, 2 або 3): ")

    if choice == "1":
        image_path = input("Введіть шлях до вихідного зображення: ")
        message = input("Введіть повідомлення для вбудовування: ")
        embed_message(image_path, message)
    elif choice == "2":
        container_path = input("Введіть шлях до стегоконтейнера: ")
        extract_message(container_path)
    elif choice == "3":
        steg_container_path = input("Введіть шлях до стегоконтейнера для відновлення: ")
        restore_original_image(steg_container_path)
    else:
        print("Невірний вибір.")
        
if __name__ == "__main__":
    main()