import streamlit as st
import qrcode
from io import BytesIO


def generate_qr_code(data, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer

# Main app
st.title("🚀 QR Code Generator Tool")

st.header("Generate Your QR Code")

data = st.text_input("Enter text or URL:")
col1, col2 = st.columns(2)
with col1:
    fill_color = st.color_picker("QR Color", "#000000")
with col2:
    bg_color = st.color_picker("Background Color", "#ffffff")
if st.button("Generate") and data:
    qr_image = generate_qr_code(data, fill_color, bg_color)
    st.image(qr_image, caption="Generated QR Code")
    st.download_button(
        label="Download QR Code",
        data=qr_image,
        file_name="qr_code.png",
        mime="image/png"
    )
else:
    st.warning("Please enter some text or URL")