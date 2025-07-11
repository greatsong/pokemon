import streamlit as st

st.set_page_config(
    page_title="귀여운 포켓몬 갤러리",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 귀여운 포켓몬 갤러리")

pokemon_images = [
    {"name": "Pikachu (피카츄)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"},
    {"name": "Eevee (이브이)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"},
    {"name": "Jigglypuff (푸린)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"},
    {"name": "Bulbasaur (이상해씨)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"},
    {"name": "Togepi (토게피)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/175.png"},
]

for p in pokemon_images:
    st.subheader(p["name"])
    st.image(p["url"], use_container_width=True)

st.success("모두 다 귀엽죠? 😊")

st.subheader("직접 다운로드해서, github에 업로드한 이미지")
st.image("포켓몬스터_모두의이야기.jpg", use_container_width=True)
