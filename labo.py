import gradio as gr

def labo_prompt(prompt_brut, style):
    # LIEU DE TRAVAIL DU PROMPT - comme Mureka
    structure = f"""[Intro: {style}]
[Couplet 1]
{prompt_brut}

[Refrain]
A-Z-IVO, c'est la Côte d'Ivoire

[Couplet 2]
Flow Yopougon, on met le feu
[Outro]
"""
    audio_desc = f"{style}, {prompt_brut}, Ivorian music, high quality"
    return structure, audio_desc

# Interface du labo
demo = gr.Interface(
    fn=labo_prompt,
    inputs=[gr.Textbox(label="Ton prompt brut ici"), gr.Dropdown(["Coupe Decale","Zouglou","Rap Ivoire"], value="Coupe Decale")],
    outputs=[gr.Textbox(label="Prompt travaille - Destination 1"), gr.Textbox(label="Prompt audio - Destination 2")],
    title="LABO A-Z-IVO - Lieu de travail des prompts"
)
demo.launch()
