HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>{heading}</h1>
    </header>
    <main>
        <p>{text}</p>
    </main>
</body>
</html>
"""

CSS_TEMPLATE = """
body {{
    background-color: {background_color};
    color: {font_color};
}}

header {{
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}}

main {{
    padding: 20px;
}}
"""