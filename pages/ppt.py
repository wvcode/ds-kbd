from pptx import Presentation


def create_slide(prs, title, content):
    slide_layout = prs.slide_layouts[1]  # Usando o layout de título e conteúdo
    slide = prs.slides.add_slide(slide_layout)

    # Adicionando título
    title_placeholder = slide.shapes.title
    title_placeholder.text = title

    # Adicionando conteúdo
    content_placeholder = slide.placeholders[1]
    content_placeholder.text = content

    return slide


def create_presentation(slides, presentation_filename):
    # Criando uma apresentação vazia
    prs = Presentation()

    for idx, slide in slides.iterrows():
        title1 = str(idx)
        content1 = slide["resultado"]
        create_slide(prs, title1, content1)

    # Salvar a apresentação em um arquivo
    prs.save(presentation_filename)
