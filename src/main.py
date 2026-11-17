import cv2

def main():
    cap = cv2.VideoCapture(0)
    try:
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
            return
        print("카메라 연결에 성공했습니다.")

        ret, frame = cap.read()
        if not ret:
            print("카메라 프레임을 읽을 수 없습니다.")
            return
    
        print("카메라 프레임을 성공적으로 읽었습니다.")
        print(f"프레임 크기: {frame.shape}")
        cv2.imshow("please-stop-biting", frame)
        cv2.waitKey(0)

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("카메라 연결을 해제했습니다.")

if __name__ == "__main__":
    main()