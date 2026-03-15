import streamlit as st
import pdfplumber


# -------- PDF TO HTML FUNCTION -------- #

def convert_pdf_to_html(pdf_path):

    html = """
    <html>
    <head>
    <style>

    body{
        font-family: Arial, Helvetica, sans-serif;
        background-color:#f4f6f9;
        margin:40px;
        color:#333;
    }

    h1{
        text-align:center;
        color:#0b3d91;
        border-bottom:3px solid #0b3d91;
        padding-bottom:10px;
        font-size:16px;
    }

    h2{
        color:#0b3d91;
        margin-top:25px;
        font-size:13px;
    }

    p{
        font-size:12px;
        line-height:1.6;
        margin-bottom:8px;
    }

    table{
        width:100%;
        border-collapse:collapse;
        margin-top:20px;
        background:white;
    }

    th, td{
        border:1px solid #ccc;
        padding:8px;
    }

    th{
        background:#0b3d91;
        color:white;
    }

    tr:nth-child(even){
        background:#f2f2f2;
    }

    .container{
        background:white;
        padding:30px;
        border-radius:10px;
        box-shadow:0px 0px 10px rgba(0,0,0,0.1);
    }

    </style>
    </head>

    <body>

    <div class="container">
    <h1>PDF Datasheet Converted to HTML/CSS</h1>
    """

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:

                lines = text.split("\n")

                for line in lines:

                    line = line.strip()

                    if line.isupper() and len(line) < 60:
                        html += f"<h2>{line}</h2>"
                    else:
                        html += f"<p>{line}</p>"

            tables = page.extract_tables()

            for table in tables:

                html += "<table>"

                for i, row in enumerate(table):

                    html += "<tr>"

                    for cell in row:

                        if i == 0:
                            html += f"<th>{cell}</th>"
                        else:
                            html += f"<td>{cell}</td>"

                    html += "</tr>"

                html += "</table>"

    html += """
    </div>
    </body>
    </html>
    """

    return html


# -------- STREAMLIT UI -------- #

st.set_page_config(page_title="PDF to HTML/CSS Converter")

st.title("PDF to Structured HTML/CSS Converter")

st.write("Upload a technical datasheet PDF and convert it into structured HTML with CSS styling.")


uploaded_file = st.file_uploader(
    "Upload Product Datasheet PDF",
    type=["pdf"]
)


if uploaded_file:

    if st.button("Convert to HTML/CSS"):

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        html_output = convert_pdf_to_html("temp.pdf")

        st.subheader("HTML Preview")

        st.components.v1.html(
            html_output,
            height=800,
            scrolling=True
        )

        st.download_button(
            label="Download HTML File",
            data=html_output,
            file_name="datasheet.html",
            mime="text/html"
        )