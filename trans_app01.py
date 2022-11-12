import cv2
from PIL import Image

original_face_img = "images/man.png"
original_mask_img = "images/otahuku.png"


def find_face():
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    img = cv2.imread(original_face_img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_list = cascade.detectMultiScale(img_gray)

    return face_list


def paste_img(face_list):
    # わかりやすいように、face_listの値をまとめておく
    x = face_list[0][0]  # X座標
    y = face_list[0][1]  # Y座標
    w = face_list[0][2]  # 横幅
    h = face_list[0][3]  # 縦幅
    print(x, y, w, h)

    # Pillowで画像を開く
    face_img = Image.open(original_face_img)
    mask_img = Image.open(original_mask_img)

    # 顔に合ったサイズに画像をリサイズしてフォルダに保存
    new_mask_img = mask_img.resize((w, h))
    new_mask_img.save("images/resized_mask_img.png")

    # マスク画像を顔に貼り付けるのと、背景透過のためのsplit()
    # 画像の貼り付けはPillowを使用した方がシンプルで簡単なのでこちらを使用します
    face_img.paste(new_mask_img, (x, y), new_mask_img.split()[3])

    # フォルダの中に保存される
    face_img.save("images/pasted_face_img.png")


def show_img(face_img):
    cv2.imshow("face", face_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    face_list = find_face()
    paste_img(face_list)
    # OpenCVで画像を読み込み
    face_img = cv2.imread("images/pasted_face_img.png")
    show_img(face_img)


if __name__ == "__main__":
    main()
