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

            # 结算，但这里的5-saomiaoerweimazhifu.png目前并不存在，因为我没抢到过……。
            if "5-saomiaoerweimazhifu.png" in [item[0] for item in showList]:

                break

            # 收货时间选择。
            elif "time.png" in [item[0] for item in showList]:

                x, y = getPosition("time.png")
                pyautogui.click(x, y, interval=0.1)
                # 额外的时间段。（叮咚他妈天天更新，需要根据实际情况自己手动调整time.png和额外的时间段个数。）

                for item in range(1):
                    if getPosition("time.png"):
                        pyautogui.click(x, y=y-55, interval=0.1)

            # 选择最优先的图片点击。
            else:

                indexList = [item for item in showList if len(item[0].split("-")) > 1]
                index = len(indexList)-1

                if index >= 0:

                    x, y = indexList[index][1]
                    pyautogui.click(x, y, interval=0.1)
