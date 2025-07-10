import streamlit as st

st.set_page_config(page_title="귀여운 포켓몬 갤러리", page_icon="🐾", layout="centered")
st.title("🐾 귀여운 포켓몬 갤러리")
st.write("아래는 실제로 존재하는 귀여운 포켓몬들의 공식 오피셜 아트워크입니다!")

pokemon_images = [
    {"name": "Pikachu (피카츄)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"},
    {"name": "Eevee (이브이)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"},
    {"name": "Jigglypuff (푸린)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"},
    {"name": "Bulbasaur (이상해씨)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"},
    {"name": "Togepi (토게피)", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/175.png"},
]

for p in pokemon_images:
    st.subheader(p["name"])
    st.image(p["url"], use_column_width=True)

st.success("모두 다 귀엽죠? 😊")
