from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called presentation_card,
# and that the code to display that component is in the "frontend" folder
presentation_card_frontend_dir = (Path(__file__).parent / "presentation_card_frontend").absolute()
_presentation_card_component_func = components.declare_component(
	"presentation_card", path=str(presentation_card_frontend_dir)
)

# Create the python function that will be called
def presentation_card(
    image_path: str,
    name: str,
    post: str,
    description: str,
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _presentation_card_component_func(
        image_path=image_path,
        name=name,
        post=post,
        description=description,
        key=key,
    )

    return component_value

# Tell streamlit that there is a component called presentation_card,
# and that the code to display that component is in the "frontend" folder
projects_carousel_frontend_dir = (Path(__file__).parent / "projects_carousel_frontend").absolute()
_projects_carousel_component_func = components.declare_component(
	"projects_carousel", path=str(projects_carousel_frontend_dir)
)

# Create the python function that will be called
def projects_carousel(
    title: str,
    subtitle: str,
    cards: str,
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _projects_carousel_component_func(
        title=title,
        subtitle=subtitle.replace("\n", "<br>"),
        cards=cards,
        key=key,
    )

    return component_value



def main():

    value_presentation_card = presentation_card(image_path="images/profile.png",
                              name="Abraão Andrade",
                              post="Cientista de Dados Júnior",
                              description="Atua como Pesquisador no Instituto do Cérebro UFRN e Estagiário em Análise de Dados e Automação de Processos no Supermercado Nordestão")

    st.write(value_presentation_card)

    title = "Work"     
    subtitle =  '''Check my commercioal and non commercial projects.
               If you have any questions feel free to ask me for more information'''
    cards = [["images/zenk.jpg", "ZENK project", "Web Scraping | RPA | Data Anlysis", "A formação da memória requer a expressão gênica induzida pela atividade neuronal. Esta resposta inclui uma série de genes dependentes de atividade tidos como mediadores das mudanças necessárias para a consolidação e manutenção da memória."],
             ["images/B2B.jpg", "Prospecção de Clientes B2B", "Google API | Python | Streamlit", "Aplicação para prospectar potenciais clientes B2B no Rio Grande do Norte utilizando uma API da Google chamada Places."],
             ["images/tracking.jpg", "Bird Tracking", "Data Processing | Data Visualization", "Aplicação para processar dados de coordenadas e gerar visualizações em mapa de calor."]]
            
    value_projects_carousel = projects_carousel(title=title,
                               subtitle=subtitle,
                               cards=cards)
    st.write(value_projects_carousel)


if __name__ == "__main__":
    main()
