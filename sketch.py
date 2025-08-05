import cv2

def sketchify(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return sketch

def webcam_mode():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        sketch = sketchify(frame)

        cv2.imshow("Webcam", frame)
        cv2.imshow("Sketch", sketch)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def image_mode(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image. Please check the path.")
        return

    sketch = sketchify(image)

    cv2.imshow("Original Image", image)
    cv2.imshow("Sketch", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        while True:
            print("Select mode:")
            print("1. Webcam")
            print("2. Image")
            print("0. Exit")
        
            choice = input("Enter choice: ")
        
            if choice == '1':
                webcam_mode()
            elif choice == '2':
                path = input("Enter path to image: ")
                image_mode(path)
            elif choice == '0':
                break
            else:
                print("Invalid choice.")
    except KeyboardInterrupt:
        print("User interrupted the program.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cv2.destroyAllWindows()
        print("Exiting the program.")
