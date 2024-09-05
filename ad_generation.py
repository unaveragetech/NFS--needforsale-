# ad_generation.py
from string import Template
from datetime import datetime

# Function to generate an ad based on a template and provided data
def generate_ad(header, content, end_date):
    ad_template = Template("""
    <html>
        <body>
            <h1>$header</h1>
            <p>$content</p>
            <p>Offer valid until $end_date</p>
        </body>
    </html>
    """)
    return ad_template.substitute(header=header, content=content, end_date=end_date)

# Example of generating an ad
if __name__ == "__main__":
    header = "Special Discount!"
    content = "Save 50% on all items this weekend."
    end_date = datetime.now().strftime('%Y-%m-%d')
    ad = generate_ad(header, content, end_date)
    print(ad)
