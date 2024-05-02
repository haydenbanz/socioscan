import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import chain
from datetime import datetime
from wordcloud import WordCloud
from flask import Flask, render_template, request

app = Flask(__name__)

DISPLAY_DATE_SLIDER = False


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css" />', unsafe_allow_html=True)
        st.markdown('<style>.github-fork-ribbon{ position:fixed; z-index:1000000 }; .github-fork-ribbon:before{ background-color: #090; }</style>', unsafe_allow_html=True)
        st.markdown('<a class="github-fork-ribbon left-top" href="https://github.com/haydenbanz" data-ribbon="Fork me on GitHub" title="Fork me on GitHub">Fork me on GitHub</a>', unsafe_allow_html=True)

        st.title(":bar_chart: Socioscan")

        st.markdown(body="Socioscan is a powerful social media intelligence tool designed to cut through the clutter and reveal the hidden stories shaping online conversation and its analytical dashboard for OSINT researchers")

        df = request.files['dataset']
        if df is None:
            st.markdown(body="""Run test of example dataset analysis OR upload datasets (**you can use several**) of posts. """)

            with st.expander("Read more about Socioscan"):
                st.markdown("Socioscan means 'Analytical DAshboard (for NArratives)'.")
                st.markdown("Currently Twitter is only supported: Zeeschuimer (Twitter API ndjson) and CSV format")
                st.markdown("Remind you that results of analysis depends on the quality of dataset.")
                st.markdown("Read [here](https://docs.google.com/document/d/10xOgmZmvLM-BJeak-KNXzkx7H5oqnbn834-o94WbM50/edit#heading=h.1037l5l116z1) how to prepare new datasets.")

            uploaded_files = request.files.getlist("dataset")

            if not len(uploaded_files):
                st.stop()

            for i in range(len(uploaded_files)):
                if df is None:
                    df = components.input_file_to_dataframe(uploaded_files[i])
                else:
                    df = pd.concat([df, components.input_file_to_dataframe(uploaded_files[i])])
                    datasets_count += 1
                    df = df.reset_index()

        st.session_state["datasets_count"] = datasets_count
        st.session_state["df"] = df

    return render_template('analysis.html')


def extract_hashtags(text):
    hashtags_list = []
    hashtags = re.findall(r'#[a-zA-Z_-]+', text)
    for h in hashtags:
        hashtags_list.append(h[1:])
    return hashtags_list


if __name__ == '__main__':
    app.run(debug=True)
