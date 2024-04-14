import base64
import io
import os
import tkinter as tk

import onnxruntime
import torch
from PIL import Image, ImageTk
import ddddocr
import torchvision.transforms as transforms
import numpy as np


def manual_get_captcha(captcha_img_base64):
    """
    手动识别验证码
    :param captcha_img_base64: 验证码图片base64字符串
    :return: 验证码结果
    """
    window = tk.Tk()
    img_data = base64.b64decode(captcha_img_base64)
    img = Image.open(io.BytesIO(img_data))
    tkimg = ImageTk.PhotoImage(img)
    img_label = tk.Label(window, image=tkimg)
    img_label.pack()
    label = tk.Label(window, text='请输入验证码')
    label.pack()
    entry = tk.Entry(window)
    entry.pack()
    res = []

    def close_window():
        res.append(entry.get())
        window.destroy()

    button = tk.Button(window, text='提交', command=close_window)
    button.pack()
    window.mainloop()
    return res[0]


def ocr_get_captcha(captcha_img_base64):
    """
    ddddocr识别验证码
    准不了一点（
    太g了
    :param captcha_img_base64: 验证码图片base64字符串
    :return: 验证码结果
    """
    ocr = ddddocr.DdddOcr()
    img_data = base64.b64decode(captcha_img_base64)
    res_str = ocr.classification(img_data)
    res = eval(res_str)
    return res


def calculate_captcha_recognition_get_ruoyi_captcha(captcha_img_base64):
    """
    项目地址：https://github.com/fupinglee/CalculateCaptcha_Recognition

    项目名称：CalculateCaptcha_Recognition

    项目简介：使用pytorch训练和识别计算验证码（若依验证码）

    成功率还行
    :param captcha_img_base64: 验证码图片base64字符串
    :return: 验证码结果
    """
    # captcha_array = list("0123456789+-×÷=？")
    captcha_array = list("0123456789+-*/=？")
    img_data = base64.b64decode(captcha_img_base64)
    img = Image.open(io.BytesIO(img_data))
    trans = transforms.Compose([
        transforms.Resize((60, 160)),
        transforms.ToTensor()
    ])
    img_tensor = trans(img)
    img_tensor = img_tensor.reshape(1, 3, 60, 160)
    onnx_file_path = os.path.join(
        os.path.dirname((os.path.dirname(os.path.realpath(__file__)))),
        'static/mathcode.onnx'
    )
    ort_session = onnxruntime.InferenceSession(onnx_file_path)
    model_input_name = ort_session.get_inputs()[0].name
    onnx_out = ort_session.run(None, {model_input_name: to_numpy(img_tensor)})
    onnx_out = torch.tensor(np.array(onnx_out))
    onnx_out = onnx_out.view(-1, captcha_array.__len__())
    res_str = vec2text(onnx_out)
    res = eval(res_str[:-2])
    return res


def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()


def vec2text(vec):
    # captcha_array = list("0123456789+-×÷=？")
    captcha_array = list("0123456789+-*/=？")
    vec = torch.argmax(vec, dim=1)  # 把为1的取出来
    text = ''
    for i in vec:
        text += captcha_array[i]
    return text


if __name__ == '__main__':
    base64_str = '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'
    # res = manual_get_captcha(base64_str)
    # print(res)
    # res = ocr_get_captcha(base64_str)
    res = calculate_captcha_recognition_get_ruoyi_captcha(base64_str)
    print(res)
