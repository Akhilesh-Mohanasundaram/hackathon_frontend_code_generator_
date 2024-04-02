from templates import HTML_TEMPLATE, CSS_TEMPLATE
from utils import color_contrast

def generate_frontend_code(user_input):
    title = user_input.get('title', 'Untitled')
    heading = user_input.get('heading', 'Welcome')
    text = user_input.get('text', '')

    # Generating HTML code
    html_code = HTML_TEMPLATE.format(title=title, heading=heading, text=text)

    # Generating CSS code
    background_color = user_input.get('background_color', '#ffffff')
    font_color = user_input.get('font_color', '#000000')
    css_code = CSS_TEMPLATE.format(background_color=background_color, font_color=font_color)

    return html_code, css_code
