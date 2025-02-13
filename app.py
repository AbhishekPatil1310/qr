from flask import Flask, render_template, send_file
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

app = Flask(__name__)

@app.route('/')
def personal_info():
    return render_template('personal_info.html')

@app.route('/qr_code')
def qr_code():
    return send_file('static/qr_code.png', mimetype='naruto/png')

if __name__ == "__main__":
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add the URL pointing to this Flask app (adjust localhost URL as needed)
    qr.add_data("qr-el9qhzuhp-abhisheks-projects-680a2fd9.vercel.app")  # Replace with your deployed URL when hosted
    qr.make(fit=True)

    # Customize the QR Code design
    custom_qr = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(0, 102, 204)),
    )

    # Save the QR Code to the static folder
    custom_qr.save('static/qr_code.png')

    # Run the Flask app
    app.run(debug=True)
