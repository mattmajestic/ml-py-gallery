import streamlit as st
import pandas as pd
import os
from PIL import Image
import streamlit.components.v1 as components
from streamlit_extras.badges import badge
from streamlit_extras.grid import grid
from streamlit_extras.jupyterlite import jupyterlite

def example_github():
    badge(type="github", name="mattmajestic/ml-py-gallery")

# Sample data for demonstration
sample_data = {
    "Card": ["Bulbasaur", "Caterpie", "Weedle"],
    "Value ($)": [100, 50, 30],
    "HP": [40, 40, 40],
    "Type": ["Grass", "Grass", "Bug"]
}
df = pd.DataFrame(sample_data)

# Function to simulate the valuation process
def value_cards(image_files):
    # For simplicity, we use the sample data
    return df

# Function to generate image carousel
def image_carousel(image_files):
    images = ""
    for image_file in image_files:
        img = Image.open(image_file)
        images += f'<img src="data:image/png;base64,{img_to_base64(img)}" style="width: 100%;"/>'
    return f"""
    <div class="carousel">
        {images}
    </div>
    <style>
        .carousel {{
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
        }}
        .carousel img {{
            scroll-snap-align: center;
            flex-shrink: 0;
            width: 100%;
            max-width: 300px;
            height: auto;
            margin-right: 16px;
            border-radius: 8px;
        }}
    </style>
    """

# Function to convert image to base64
import base64
from io import BytesIO

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Main app
def main():
    st.set_page_config(page_title="Pokémon Card Value Calculator", page_icon=":sparkles:")
    st.title('Pokémon Card Collection')
    
    # Display grid with the purpose of the app
    st.markdown(
        """
        <style>
        .grid-container {
            display: grid;
            grid-template-columns: 1fr 3fr;
            gap: 10px;
            padding: 10px;
        }
        .grid-item {
            padding: 20px;
            font-size: 18px;
            text-align: center;
        }
        </style>
        <div class="grid-container">
            <div class="grid-item">
                <strong>App Purpose</strong>
            </div>
            <div class="grid-item">
                <p>This app displays your Pokémon card collection and helps you evaluate their current market value.</p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Display images from the 'img' folder
    img_folder = 'img'
    if not os.path.exists(img_folder):
        st.error(f"Folder '{img_folder}' does not exist")
        return

    image_files = [os.path.join(img_folder, img) for img in os.listdir(img_folder) if img.endswith('.png')]

    st.subheader('Your Pokémon Cards')
    
    uploaded_files = st.file_uploader("Choose your Pokemon", accept_multiple_files=True)
    
    # Display image carousel
    carousel_html = image_carousel(image_files)
    components.html(carousel_html, height=400)

    st.subheader('Card Values')
    
    # Button to value the cards
    if st.button('Value My Cards'):
        st.balloons()
        card_values = value_cards(image_files)
        st.dataframe(card_values)
    
    
    # jupyterlite(500, 600)    
    example_github()

if __name__ == "__main__":
    main()
