import keyboard
import pyautogui
import time
import random
import threading
import os

# ---------------------------------------------------
# Smooth and optimized version + 4 X presses
# ---------------------------------------------------

pyautogui.FAILSAFE = True

print("🚀 Starting in 2 seconds...")
time.sleep(2)

# ===============================
# Global variables
# ===============================
left_counter = 0
right_counter = 0
lock = threading.Lock()

press_c_flag = False
press_v_flag = False

# ===============================
# Relative paths to images
# ===============================
images_dir = os.path.join("..", "images")
left_image_path = os.path.join(images_dir, "left_side.png")
right_image_path = os.path.join(images_dir, "right_side.png")

# ===============================
# Function for X presses (🔥 now 4)
# ===============================
def press_x_sequence():
    for _ in range(4):
        keyboard.press_and_release('x')
        time.sleep(random.uniform(3, 4))
    time.sleep(random.uniform(0.25, 0.32))

# ===============================
# Thread C
# ===============================
def monitor_c():
    global press_c_flag
    while True:
        time.sleep(random.uniform(120, 180))
        with lock:
            press_c_flag = True

threading.Thread(target=monitor_c, daemon=True).start()

# ===============================
# Thread V
# ===============================
def monitor_v():
    global press_v_flag
    while True:
        time.sleep(random.uniform(150, 180))
        with lock:
            press_v_flag = True

threading.Thread(target=monitor_v, daemon=True).start()

# ===============================
# Thread Y
# ===============================
def monitor_y():
    while True:
        time.sleep(random.uniform(600, 900))
        print("💥 Thread: Pressing Y twice!")

        keyboard.press('y')
        time.sleep(random.uniform(0.08, 0.18))
        keyboard.release('y')

        time.sleep(random.uniform(0.3, 1))

        keyboard.press('y')
        time.sleep(random.uniform(0.08, 0.18))
        keyboard.release('y')

        print("💥 Finished pressing Y")

threading.Thread(target=monitor_y, daemon=True).start()

# ===============================
# Main loop
# ===============================
for main_cycle in range(20000):
    print(f"\n🔁 Cycle number {main_cycle + 1}")

    # ======================
    # RIGHT SIDE
    # ======================
    while True:
        try:
            right_found = pyautogui.locateOnScreen(
                right_image_path,
                confidence=0.6,  # can be changed back to 0.8
                grayscale=True
            )
        except pyautogui.ImageNotFoundException:
            right_found = None

        if right_found:
            time.sleep(random.uniform(0.28, 0.61))
            with lock:
                right_counter += 1
                current_right = right_counter
                c_flag = press_c_flag
                v_flag = press_v_flag
                press_c_flag = False
                press_v_flag = False

            print(f"➡ right_counter: {current_right}")

            if 6 <= current_right <= 7:
                print("💥 Pressing B based on counter (6-7)")
                time.sleep(random.uniform(0.73, 1.45))
                keyboard.press('b')
                time.sleep(random.uniform(1.3, 2.1))
                keyboard.release('b')
                right_counter = 0
                time.sleep(random.uniform(0.35, 1.12))

            if c_flag:
                print("💥 Pressing C")
                keyboard.press('c')
                time.sleep(random.uniform(0.08, 0.18))
                keyboard.release('c')

            if v_flag:
                print("💥 Pressing V")
                keyboard.press('v')
                time.sleep(random.uniform(0.08, 0.18))
                keyboard.release('v')

            press_x_sequence()
            break

        # Not found – move right
        keyboard.press('right')
        keyboard.press('d')
        time.sleep(random.uniform(0.18, 0.27))
        keyboard.release('d')
        keyboard.release('right')
        time.sleep(random.uniform(0.06, 0.13))

    # ======================
    # LEFT SIDE
    # ======================
    while True:
        try:
            left_found = pyautogui.locateOnScreen(
                left_image_path,
                confidence=0.6,  # can be changed back to 0.8
                grayscale=True
            )
        except pyautogui.ImageNotFoundException:
            left_found = None

        if left_found:
            time.sleep(random.uniform(0.28, 0.61))
            with lock:
                left_counter += 1
                current_left = left_counter

            print(f"⬅ left_counter: {current_left}")

            if 2 <= current_left <= 3:
                print("💥 Pressing Q based on counter (2-3)")
                time.sleep(random.uniform(0.73, 1.45))
                keyboard.press('q')
                time.sleep(random.uniform(1.3, 2.1))
                keyboard.release('q')
                left_counter = 0
                time.sleep(random.uniform(0.35, 1.12))

            press_x_sequence()
            break

        # Not found – move left
        keyboard.press('left')
        keyboard.press('d')
        time.sleep(random.uniform(0.18, 0.27))
        keyboard.release('d')
        keyboard.release('left')
        time.sleep(random.uniform(0.06, 0.13))

print("🏁 Finished successfully")