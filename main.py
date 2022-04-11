import os
import time
import pyautogui


# 获取坐标。
def getPosition(image, confidence=0.8):

    src = os.path.join(os.getcwd(), "images", image)
    return pyautogui.locateCenterOnScreen(src, confidence=confidence)


# 获取图片列表。
imageList = os.listdir("images")


if __name__ == "__main__":

    time.sleep(0.1)

    while True:

        showList = []

        for image in imageList:

            position = getPosition(image)

            if position:

                showList.append((image, position))

        if len(showList) > 0:

            # 结算。
            if "end.png" in [item[0] for item in showList]:
                print("抢到菜啦！")
                break
            # 收获时间选择。
            elif "time.png" in [item[0] for item in showList]:
                x, y = getPosition("time.png")
                pyautogui.click(x, y, interval=0.5)
                # 额外的三个时间段。
                for item in range(3):
                    if getPosition("time.png"):
                        pyautogui.click(x, y=y-55, interval=0.5)
            # 选择最优先的图片点击。
            else:
                indexList = [item for item in showList if len(item[0].split("-")) > 1]
                index = len(indexList)-1
                if index >= 0:
                    x, y = indexList[index][1]
                    pyautogui.click(x, y, interval=0.5)
