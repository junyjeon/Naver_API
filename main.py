import requests
from bs4 import BeautifulSoup
import json
import re
import your_image_analysis_library
import your_text_analysis_library

# Constants
NAVER_STORE_URL = "https://m.smartstore.naver.com/royalwater/products/3924967847?NaPm=ct%3Dlghk3774%7Cci%3D84f7b67864bf6cb714e698e67d3c52d41d543b43%7Ctr%3Dsls%7Csn%3D403720%7Chk%3D7d16eed6acb6fb565c38de0e2def423f7585c71a"
YOUR_API_KEY = "7ysSMApWVx"

# Functions
def get_product_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    review_data = json.loads(re.search(r'window\.__PRELOADED_STATE__\s*=\s*({.*?});', str(soup)).group(1))

    reviews = []
    for review in review_data["reviews"]:
        reviews.append({
            "text": review["text"],
            "images": review["images"]
        })

    return reviews

def analyze_images(images):
    keywords = []

    for image in images:
        # Analyze the image using your_image_analysis_library
        image_keywords = your_image_analysis_library.analyze(image, YOUR_API_KEY)
        keywords.extend(image_keywords)

    return keywords

def analyze_text(text):
    # Analyze the text using your_text_analysis_library
    return your_text_analysis_library.analyze(text, YOUR_API_KEY)

# Main
def main():
    reviews = get_product_reviews(NAVER_STORE_URL)

    for review in reviews:
        image_keywords = analyze_images(review["images"])
        text_keywords = analyze_text(review["text"])

        print("Image Keywords:", image_keywords)
        print("Text Keywords:", text_keywords)

if __name__ == "__main__":
    main()
