from flask import Flask,request,jsonify,send_file,render_template
import re
from io import BytesIO

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import base64

STOPWORDS=set(stopwords.words("english"))
app=Flask(__name__)
