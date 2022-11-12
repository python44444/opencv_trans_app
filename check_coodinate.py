import cv2

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        return x, y

img = cv2.imread("images/man.png")

cv2.imshow("face", img)

cv2.setMouseCallback("face", onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
