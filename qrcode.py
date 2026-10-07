import qrcode 

data = input ("Enter the link of whatever you want to convert into QR code: ")
qr = qrcode.QRCode(version=1, box_size =8 , border=5)
qr.add_data(data)
qr.make(fit=True)
qr_img =qr.make_image(fill_color="black", back_color="white")
qr_img.save("myqrcode.png")


