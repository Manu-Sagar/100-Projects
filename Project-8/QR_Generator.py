import qrcode

from PIL import ImageColor
def validate_color(color):
    try:
        ImageColor.getrgb(color)
        return True
    except ValueError:
        return False

def generate_qr_code(data,filename,qr_color,back_color):
    try:
        qr=qrcode.QRCode(
            version=1,
            box_size=10,
            border=2
        )

        qr.add_data(data)
        qr.make(fit=True)
        image=qr.make_image(
            fill_color=qr_color,
            back_color=back_color
        )
        image.save(filename)
        print(f"QR code saved successfully as {filename}")

    except OSError:
        print("Unable to save the QR code file")

    except Exception as e:
        print("An unexpected error occurred:", e)

def main():
    data=input("Enter text or URL to generate QR code: ")
    if not data.strip():
        print("Input cannot be empty")
        return
    filename=input("Enter output Filename (without extention):")

    if not filename.strip():
        print("Filename cannot be empty")
        return
    qr_color=input("Enter QR code color:").strip()
    back_color=input("Enter background color:").strip()
    if not qr_color or not back_color:
        print("Colors cannot empty")
        return
    
    if not validate_color(qr_color):
        print("Invalid QR code color!")
        return

    if not validate_color(back_color):
        print("Invalid background color!")
        return

    filename=filename.strip()+".png"
    generate_qr_code(data,filename,qr_color,back_color)
if __name__=="__main__":
    main()
