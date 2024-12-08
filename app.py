import gradio as gr
from transformers import pipeline

translation_pipeline = pipeline(
    "translation_en_to_fr",
    model="t5-base", 
    device=0 
)

def translate_transformers(English_text):
    results = translation_pipeline(English_text)
    return results[0]['translation_text']


# Interface Gradio
interface = gr.Interface(
    fn=translate_transformers,
    inputs=gr.Textbox(lines=2, placeholder='Text to translate'),
    outputs=gr.Textbox(label='French Translation Text')
)

interface.launch(share=True)