from transformers import pipeline
from transformers.utils import logging
from PIL import Image
import torch
import os
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")


# os.environ["TRANSFORMERS_OFFLINE"] = "1"  # forces local only
# logging.set_verbosity_error()
model_path = "models/SmolVLM-500M-Instruct"
os.environ["TRANSFORMERS_CACHE"] = model_path

pipe = pipeline("image-text-to-text", model=model_path, device=device)



# res = pipe(prompt, max_new_tokens=150)
def generate_caption(image, user_prompt):
    prompt = {
        "images": [image],
        "text": "Look at this image: <image>. " + user_prompt
    }
    res = pipe(
        prompt,
        generate_kwargs={
            "max_new_tokens": 100,
            "temperature": 0.7,
            "do_sample": True,
            "top_p": 0.9,
        }
    )
    full_response = res[0]['generated_text']

    # Remove the prompt text from the beginning of the generated response
    if full_response.startswith(prompt["text"]):
        clean_response = full_response[len(prompt["text"]):].strip()
    else:
        clean_response = full_response.strip()

    return clean_response

gr.Interface(
    fn=generate_caption,
    inputs=[
        gr.Image(type="pil", label="Upload an Image"),
        gr.Textbox(
            lines=2,
            label="Give your custom Prompt. Leave empty to use default.",
            value="Describe everything visible in this image using complete sentences in a paragraph. Do not repeat information or mention objects that are not visible."
        ),
    ],
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Description Generator",
    description="Upload an image and optionally provide a custom prompt. Edit the prompt below or use the default.",
).launch(share=True)

