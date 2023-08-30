# import qrcode
from qrcode import QRCode, constants
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask


qr = QRCode(version=1,
    error_correction=constants.ERROR_CORRECT_H,     
    box_size=30,
    border=2
)
url = "https://duappy.com"
qr.add_data(url)
qr.make()


img_3 = qr.make_image(
    image_factory=StyledPilImage, 
    module_drawer=RoundedModuleDrawer(), 
    embeded_image_path="images/duappy_illustrator.png",
    eye_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(230, 57, 70)) 
    ).convert("RGB")

img_3.save('newlogo_qr.png')

print("QR generated")
