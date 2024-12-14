import cv2

# Configure Tesseract path if needed (e.g., on Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import pytesseract

# Specify the full path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_numbers(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Preprocess the image for better OCR results
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # OCR to detect text
    text = pytesseract.image_to_string(thresh, config='--psm 6 digits')
    
    # Extract only numbers
    numbers = ''.join(filter(str.isdigit, text))
    return numbers

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)  # Use 0 for default camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect numbers in the frame
        numbers = detect_numbers(frame)
        if numbers:
            print(f"Detected Numbers: {numbers}")
        
        # Display the frame
        cv2.imshow("Camera Feed", frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
