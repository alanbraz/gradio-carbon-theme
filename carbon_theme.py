import gradio as gr

carbon_theme = gr.themes.Monochrome(
    font=[gr.themes.GoogleFont('IBM Plex'), gr.themes.GoogleFont('IBM Plex Sans'), 'system-ui', 'sans-serif'],
    primary_hue=gr.themes.Color(c50="#ffffff", c100="#edf5ff", c200="#d0e2ff", c300="#a6c8ff", c400="#78a9ff", c500="#4589ff", c600="#0f62fe", c700="#0043ce", c800="#002d9c", c900="#001d6c", c950="#001141"),
    neutral_hue=gr.themes.Color(c50="#ffffff", c100="#f4f4f4", c200="#e0e0e0", c300="#c6c6c6", c400="#a8a8a8", c500="#8d8d8d", c600="#6f6f6f", c700="#525252", c800="#393939", c900="#262626", c950="#161616"),
).set(
    background_fill_primary_dark='*neutral_950',
    background_fill_secondary='*neutral_100',
    background_fill_secondary_dark='*neutral_900',
    border_color_accent='*neutral_200',
    border_color_accent_dark='*neutral_800',
    border_color_primary_dark='*neutral_800',
    link_text_color='*neutral_950',
    link_text_color_dark='*neutral_100',
    link_text_color_active='*primary_600',
    button_primary_background_fill='*primary_600',
    button_primary_background_fill_dark='*primary_600',
    button_primary_background_fill_hover='#0353e9',
    button_secondary_background_fill_dark='*neutral_800'
)
