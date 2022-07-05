'''
importing modules opencv and mediapipe and pyautogui
'''

import cv2         # module opencv
import mediapipe as mp   # module mediapipe
import pyautogui   # module pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
# defining the screen width and height
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # flip is using mirroring the camera screen
    frame_height, frame_width, _ = frame.shape  # defining the widht and height of output frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark  # landmarks of hands
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print(x, y)
                # id == 8 means the index finger tip
                if id == 8:
                    # Highlight the index finger tip by circle, color
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width * x
                    index_y = screen_height/frame_height * y
                    pyautogui.moveTo(index_x, index_y)  # pyautogui.moveTo is using to move curser on screen
                # id == 4 means the thumb tip
                if id == 4:
                    # Highlight the thumb tip by circle, color
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width * x
                    thumb_y = screen_height/frame_height * y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        # print('Click')
                        pyautogui.click()  # for click
                        pyautogui.sleep(1)  # sleep time is 1 sec

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
