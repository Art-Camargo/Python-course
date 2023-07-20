import qrcode
phone_number = '+5554981248316'
img = qrcode.make(phone_number)
img.save('Qrcode_my_brazilian_phone.png')
img.show()
