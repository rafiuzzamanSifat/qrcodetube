import qrcode
import image

qr= qrcode.QRCode(
    version= 15,  # version of qrcode, as mch high as much big and complicated image
    box_size=10,  #box where displayed
    border=5      #white part of the image
)

data="https://www.youtube.com/channel/UCdZ4hsopbJcZYIWMvLl8-EA"

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black', back_color="white")
img.save('siftube.png')
