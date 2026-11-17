import cv2

def main():
    cap = cv2.VideoCapture(0)
    try:
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
            return
        print("카메라 연결에 성공했습니다.")
        print("미리보기 창에서 ESC를 누르면 종료됩니다.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("카메라 프레임을 읽을 수 없습니다.")
                break
        
            cv2.imshow("please-stop-biting", frame)
            key = cv2.waitKey(1)
            if key == 27:  # ESC 키를 누르면 종료
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("카메라 연결을 해제했습니다.")

if __name__ == "__main__":
    main()