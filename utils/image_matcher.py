import os

import cv2 as cv
import numpy as np
import time

from utils.get_path import get_path


def get_match_coordinates(driver, image):
    path = get_path()
    relative_path = f'template_images/{image}'
    image_path = os.path.join(path, relative_path)
    template_image = cv.imread(image_path, cv.IMREAD_UNCHANGED)

    threshold = 0.57
    timeout = 120
    start_time = time.time()
    while time.time() - start_time < timeout:
        screenshot = driver.get_screenshot_as_png()
        screenshot = cv.imdecode(np.frombuffer(screenshot, np.uint8), cv.IMREAD_UNCHANGED)

        # Ensure both images have the same number of channels
        if screenshot.shape[2] == 4 and template_image.shape[2] == 3:
            template_image = cv.cvtColor(template_image, cv.COLOR_BGR2BGRA)

        # Convert both images to the same data type
        screenshot = screenshot.astype(np.float32)
        template_image = template_image.astype(np.float32)

        result = cv.matchTemplate(screenshot, template_image, cv.TM_CCOEFF_NORMED)

        # Get the best match position from the match result.
        _, max_val, _, max_loc = cv.minMaxLoc(result)

        if max_val >= threshold:
            return max_loc

        time.sleep(20)
