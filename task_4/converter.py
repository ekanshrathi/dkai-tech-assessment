import pdfplumber
import pandas as pd

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
    }

    h2{
        color:#0b3d91;
        margin-top:30px;
    }

    p{
        font-size:14px;
        line-height:1.6;
        margin-bottom:8px;
    }

    table{
        border-collapse: collapse;
        width:100%;
        margin-top:20px;
        margin-bottom:30px;
        background:white;
    }

    table, th, td{
        border:1px solid #ccc;
    }

    th{
        background-color:#0b3d91;
        color:white;
        padding:10px;
        text-align:left;
    }

    td{
        padding:8px;
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
    <h1>PDF Datasheet Converted to HTML</h1>

    """

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:

            text = page.extract_text()

            if text:
                lines = text.split("\n")

                for line in lines:
                    html += f"<p>{line}</p>"

            tables = page.extract_tables()

            for table in tables:

                html += "<table border='1'>"

                for row in table:

                    html += "<tr>"

                    for cell in row:
                        html += f"<td>{cell}</td>"

                    html += "</tr>"

                html += "</table>"

    html += "</body></html>"

    return html