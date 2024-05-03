# socioscan
Socioscan is a powerful social media intelligence tool designed to cut through the clutter and reveal the hidden stories shaping online conversations.   
## The idea

Analytical tool to extract insights (shown on a simple dashboard) from social media posts about narratives, sentiments, initiators, influencers and clusters of accounts.
It should be applicable for studying disinformation campaigns, analysing public opinion, and assessing risks related to some topics.

It's a project created by team Watch Cats during participation in [Bellingcat's First In-person Hackathon](https://www.bellingcat.com/bellingcats-first-in-person-hackathon/). 

Inspired by [4CAT](https://4cat.nl/) and [twitter explorer](https://twitterexplorer.org/).
The development process is documented in [this Google document](https://docs.google.com/document/d/10xOgmZmvLM-BJeak-KNXzkx7H5oqnbn834-o94WbM50/edit#heading=h.m0d3jrsts18t).
## Datasets

[Twitter posts on various topics (1-20K)](https://drive.google.com/drive/u/0/folders/1GtUZkfD0cZ2xBBZ3FiDpH1Cgw_u-m1wh), including datasets enriched with topics and sentiments.

Instructions:
- [How to prepare dataset with Zeeschuimer](https://docs.google.com/document/d/19MAiqX7Vx1FcNJ44K-vSdnKDVC5gcFwtrSQiewnwW8A/edit)
- [How to prepare CSV dataset](https://docs.google.com/document/d/1TTulgfIhSEZRQODRem9ufJWXZ7tGJdHEVYSVk8Teit4/edit)
- Check utils/cluster_n_sentiments.ipynb for instructions on how to enrich datasets with sentiments and topics

**How can I get topics and sentiments for my dataset?** Cause it’s a resource- and time-consuming operation, we implemented it in the Jupyter Notebook script available on our GitHub. For tweets vectorization we are using hkunlp/instructor-large model, for clusterization – MiniBatchKMeans, for the detection of topics – GPT-4-Turbo API, for the sentiment analysis of tweets – cardiffnlp/twitter-roberta-base-sentiment-latest mode. All steps are reproducible.

## Installation

For local installation you need Python and pip installed.
```sh
pip install -r requirements.txt
streamlit run dashboard.py
```

## Utils

`utils` folder contains:
- CSV tweet datasets formatter (to Twitwi)
- `cluster_n_sentiments.ipynb`: ML stuff (enrichment of datasets with sentiments and topics)

### SOWEL classification

This tool uses the following OSINT techniques:
- [SOTL-5.2. Analyse Sentiments](https://sowel.soxoj.com/sentiments)

## Some other results

An example of a hashtag network built with [Twitter Explorer](https://twitterexplorer.org/) using one of the datasets

<img width="958" alt="HashtagNetwork" src="https://github.com/soxoj/bellingcat-hackathon-watchcats/assets/31013580/6327e7dd-ceb1-4f26-a5b4-6961dae5957b">
