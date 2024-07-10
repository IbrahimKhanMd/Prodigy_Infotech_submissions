# main.py

import cv2
import mediapipe as mp
import pyautogui
import random
import util
from pynput.mouse import Button, Controller

mouse_controller = Controller()

display_width, display_height = pyautogui.size()

hand_detector = mp.solutions.hands
hand_model = hand_detector.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

def locate_index_fingertip(hand_data):
    if hand_data.multi_hand_landmarks:
        hand = hand_data.multi_hand_landmarks[0]
        return hand.landmark[hand_detector.HandLandmark.INDEX_FINGER_TIP]
    return None

def update_cursor_position(fingertip):
    if fingertip:
        cursor_x = int(fingertip.x * display_width)
        cursor_y = int(fingertip.y / 2 * display_height)
        pyautogui.moveTo(cursor_x, cursor_y)

def check_left_click(hand_points, thumb_index_distance):
    return (
        util.get_angle(hand_points[5], hand_points[6], hand_points[8]) < 50 and
        util.get_angle(hand_points[9], hand_points[10], hand_points[12]) > 90 and
        thumb_index_distance > 50
    )

def check_right_click(hand_points, thumb_index_distance):
    return (
        util.get_angle(hand_points[9], hand_points[10], hand_points[12]) < 50 and
        util.get_angle(hand_points[5], hand_points[6], hand_points[8]) > 90 and
        thumb_index_distance > 50
    )

def check_double_click(hand_points, thumb_index_distance):
    return (
        util.get_angle(hand_points[5], hand_points[6], hand_points[8]) < 50 and
        util.get_angle(hand_points[9], hand_points[10], hand_points[12]) < 50 and
        thumb_index_distance > 50
    )

def check_screenshot(hand_points, thumb_index_distance):
    return (
        util.get_angle(hand_points[5], hand_points[6], hand_points[8]) < 50 and
        util.get_angle(hand_points[9], hand_points[10], hand_points[12]) < 50 and
        thumb_index_distance < 50
    )

def interpret_gesture(image, hand_points, hand_data):
    if len(hand_points) >= 21:
        fingertip = locate_index_fingertip(hand_data)
        thumb_index_distance = util.get_distance([hand_points[4], hand_points[5]])

        if util.get_distance([hand_points[4], hand_points[5]]) < 50 and util.get_angle(hand_points[5], hand_points[6], hand_points[8]) > 90:
            update_cursor_position(fingertip)
        elif check_left_click(hand_points, thumb_index_distance):
            mouse_controller.press(Button.left)
            mouse_controller.release(Button.left)
            cv2.putText(image, "Left Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif check_right_click(hand_points, thumb_index_distance):
            mouse_controller.press(Button.right)
            mouse_controller.release(Button.right)
            cv2.putText(image, "Right Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif check_double_click(hand_points, thumb_index_distance):
            pyautogui.doubleClick()
            cv2.putText(image, "Double Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        elif check_screenshot(hand_points, thumb_index_distance):
            screenshot = pyautogui.screenshot()
            unique_id = random.randint(1, 1000)
            screenshot.save(f'my_screenshot_{unique_id}.png')
            cv2.putText(image, "Screenshot Taken", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

def run():
    visualize = mp.solutions.drawing_utils
    camera = cv2.VideoCapture(0)

    try:
        while camera.isOpened():
            success, image = camera.read()
            if not success:
                break
            image = cv2.flip(image, 1)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            hand_data = hand_model.process(rgb_image)

            hand_points = []
            if hand_data.multi_hand_landmarks:
                hand = hand_data.multi_hand_landmarks[0]
                visualize.draw_landmarks(image, hand, hand_detector.HAND_CONNECTIONS)
                for landmark in hand.landmark:
                    hand_points.append((landmark.x, landmark.y))

            interpret_gesture(image, hand_points, hand_data)

            cv2.imshow('Hand Gesture Control', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    run()