from frontend_generator import generate_frontend_code

def main():
    # Example input from user
    user_input = {
        'title': 'My Website',
        'heading': 'Welcome to My Website',
        'text': 'This is a sample text for demonstration purposes.',
        'background_color': '#f0f0f0',
        'font_color': '#333',
    }

    html_code, css_code = generate_frontend_code(user_input)

    # Output generated code
    print("Generated HTML code:")
    print(html_code)
    print("\nGenerated CSS code:")
    print(css_code)

if __name__ == "__main__":
    main()
