from .models import Services

# from django.db.models.functions import GroupConcat
# from django.db.models import CharField, Value
import numpy as np
# numpy is a library for working with arrays
# it also has functions for working in domain of linear algebra, fourier transform, and matrices
import pandas as pd
# pandas is a library for data manipulation and analysis
import matplotlib.pyplot as plt
# matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB
# matlab is a programming language and multi-paradigm numerical computing environment
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# sklearn is a machine learning library for python
# sklearn.metrics.pairwise.cosine_similarity is a function that computes the cosine similarity between two vectors
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# wordcloud is a library for creating word clouds
# wordcloud.WordCloud is a class that creates a word cloud
# wordcloud.STOPWORDS is a set of default stopwords for english language
# wordcloud.ImageColorGenerator is a class that creates a color function from an image
import nltk
# nltk is a library for natural language processing
import re
# re is a library for regular expression operations
import string
# string is a library for common string operations
from nltk.corpus import stopwords
# nltk.corpus is a module that contains a collection of corpus reader classes
# nltk.corpus.stopwords is a set of stopwords for english language
import difflib
from difflib import get_close_matches
from nltk.stem import SnowballStemmer



def recommend(request):
    # load the data from the database
    services = Services.objects.all().prefetch_related('skills', 'category')[:3]
    preprocessed = []
    for service in services:
        text = f"{service.title} {','.join(service.description)} {','.join(service.skills.values_list('name', flat=True))} {','.join(service.category.values_list('name', flat=True))}"
        text = text.lower().translate(str.maketrans('', '', string.punctuation))
        for word in text.split():
            preprocessed.append(''.join(word))

    # # compute TF-IDF scores
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(preprocessed)


    # # compute pairwise cosine similarity
    cos_sim = cosine_similarity(tfidf)
    from account.models import UserSkills
    # get skills of request.user in skill_name variable
    skill_name = UserSkills.objects.filter(user=request.user)
    skills = []
    for skill in skill_name:
        skills.append(skill.name.values('name', flat=True)) 
    print(skills)
    # # generate recommendations
    # n_recommendations = 5
    # recommendations = {}
    # for i, service in enumerate(services):
    #     sim_scores = list(enumerate(cos_sim[i]))
    #     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #     sim_scores = sim_scores[1:n_recommendations+1]
    #     service_indices = [j for j, _ in sim_scores]
    #     recommendations[service] = services.filter(id__in=service_indices)
        # print(recommendations[service])