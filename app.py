import streamlit as st
from googletrans import Translator
from PIL import Image
import cv2
import os
import io
from gtts import gTTS
import webbrowser

port = int(os.environ.get("PORT",5000))
@st.cache(allow_output_mutation=True)
def load_init():
    return Translator()

temp_file_list = [file for file in os.listdir(os.getcwd()+'/temp')]
if len(temp_file_list) >= 1:
    for f in temp_file_list:
        os.remove(os.path.join(os.getcwd()+'/temp',f))
lang = ['hi']
translator = load_init()
st.sidebar.image("machine-learning.png",width = 100)
st.sidebar.markdown("### Data Frame")
choice = st.sidebar.radio('Select',['Home','Text Translator','Photo Translator'])
hide_streamlit_style = """<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
if st.sidebar.button("Instagram"):
    webbrowser.open("https://www.instagram.com/data_frame/",new=2)
if st.sidebar.button("Github"):
    webbrowser.open("https://github.com/yugdamor-git/",new=2)
if st.sidebar.button("Youtube"):
    webbrowser.open("https://www.youtube.com/channel/UC-UBtO3u9lwh6S-SNxvIM4A",new=2)

LANGUAGES = ['None','afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu', 'Filipino', 'Hebrew']

LANGUAGES_CODE = ['na','af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'fil', 'he']

if choice == 'Text Translator':
    st.title("Text Translator")
    st.markdown('Communicate smoothly and use a free online translator to instantly translate words, phrases, or documents between 90+ language pairs.')

    text = st.text_input('Type or Paste your text here to translate : ')
    if not len(text) <= 0:
        with st.spinner("Detecting Language"):
            lang = translator.detect(text).lang
        st.success("Detected language : "+ LANGUAGES[LANGUAGES_CODE.index(lang)])
        selected_lang = st.selectbox('Select Target language',list(range(len(LANGUAGES))),format_func= lambda x : LANGUAGES[x])
        #st.markdown(LANGUAGES_CODE[selected_lang])
        if LANGUAGES[selected_lang] != 'None':
            with st.spinner("Translating to " + LANGUAGES[selected_lang]):
                dest_lang = translator.translate(text,src=lang,dest=LANGUAGES_CODE[selected_lang])
                voice = gTTS(dest_lang.text,lang=LANGUAGES_CODE[selected_lang])
                voice_path = os.path.join(os.getcwd(),'temp')
                voice.save(voice_path+"/temp.mp3")
                st.markdown("Audio : ")
                st.audio(voice_path+"/temp.mp3")
            st.markdown(LANGUAGES[selected_lang] +' Translation : ' + dest_lang.text)

if choice == 'Home':
    st.title("Translate Free Online with Machine Translation")
    st.markdown('Free Machine Translation with no limits, always available at your fingertips')
    st.markdown('Enjoy voice & photo translation anytime and anywhere and enhance your communication with foreigners')
    st.markdown('Translate complex texts easily by writing or typing them using a keyboard or handwriting input')

if choice == 'Photo Translator':
    st.markdown("## i am not able to deploy this feature because i am using free heroku account. and this feature requires high processing power.")

