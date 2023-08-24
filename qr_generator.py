import qrcode
from PIL import Image

Logo_link = "images/duappy_illustrator.png"

logo = Image.open(Logo_link)

basewidth = 400

wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)


QRcode = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=33,
    border=2
)

url = "https://duappy.com"

QRcode.add_data(url)

QRcode.make()

QRcolor = "#E63946"

QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert("RGB")

pos = ((QRimg.size[0] - logo.size[0]) // 2, 
       (QRimg.size[1] - logo.size[1]) // 2)

QRimg.paste(logo, pos)

QRimg.save('logo_qr.png')

print("QR generated")