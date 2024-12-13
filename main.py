import picamera2
import cv2

def capture_and_display_video():
    # Initialize Picamera2
    picam2 = picamera2.Picamera2()

    # Configuration dictionary with proper keys
    picam2.configure(picam2.create_video_configuration(main={"size": (720, 720), "format": "RGB888" },
    lores={"size": (440, 440), "format": "YUV420"}, raw={"size": (2304,1296)}, encode="lores"))

    # Start the camera
    picam2.start()

    try:
        while True:
            # Capture a frame
            frame = picam2.capture_array()

            # Display the frame
            cv2.imshow("720p Video Stream", frame)

            # Break loop with 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Camera stopped.")
    finally:
        # Stop and release resources
        picam2.stop()
        cv2.destroyAllWindows()

# Call the function
capture_and_display_video()
