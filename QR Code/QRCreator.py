import qrcode
import pyqrcode
import qrdecode


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


def create_QR(input_txt):
    qr.add_data(input_txt)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def QR_Decode():


    a=qrdecode.decode(r'D:\Abhijeet Python\Locker\Project\RSA\Encrypted_QR.jpg')

    return a


QR_Decode()
