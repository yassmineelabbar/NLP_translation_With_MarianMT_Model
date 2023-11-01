import streamlit as st
from PIL import Image
from transformers import MarianMTModel, MarianTokenizer

# Load translation model and tokenizer
model_name = "yasmineelabbar/marian-finetuned-kde4-en-to-fr-accelerate"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)


def translate_text(input_text):
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    translation = model.generate(inputs, max_length=100)[0]
    translated_text = tokenizer.decode(translation, skip_special_tokens=True)
    return translated_text


def main():
    st.title("Transloom - English to French Translator")

    # Display Transloom logo
    image = Image.open("C:/Users/yazid/PycharmProjects/appTranslate/transloom.jpg")
    st.image(image, caption="Transloom Logo", use_column_width=True)

    input_text = st.text_area("Enter English text for translation:")
    if st.button("Translate"):
        if input_text.strip() == "":
            st.warning("Please enter text to translate.")
        else:
            translated_text = translate_text(input_text)
            st.success("Translation:")
            st.info(translated_text)


if __name__ == "__main__":
    main()
