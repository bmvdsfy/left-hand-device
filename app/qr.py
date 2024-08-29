
import numpy
import qrcode

#pip install Pillow qrcode numpy
#https://blog.i-o.io/?id=1549862841

def generate_qr(url):
    qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    border=0,
    box_size=1,
    version=1,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()

    a = numpy.asarray(img)
    for r in a:
        for c in r:
            if c: print(' '*2,end=''),
            else: print('█'*2,end=''),
        print('')


if __name__ == "__main__":
    generate_qr("hello world")