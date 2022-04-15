""" 
Steps:
Pull all the courses + descr that start with SDS
Remove all the stop words
Make biagrams in a “stupid” way
Bag of unigrams that's left run that through as the BOK
That function that adds s and es etc
Make function that looks at courses, strip stop words, 
	-input: department code for that school, ie SDS, KOR, THE, EGR, etc
	-goal: is this better? Is there something we can take from this experiment?
 """
#figure out how to pass department code as input from user
#then write this code as a function and pass it thru main

import pandas as pd
import numpy as np
import nltk
import spacy
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
import re
from re import *
from nltk.util import ngrams
from nltk.corpus import stopwords
import gower
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
from get_df_name_func import get_df_name
from process_words_funct import process_words
from tfidf_analysis import tfidf
from tokenizer import tokenize

nlp = spacy.load("en_core_web_sm")

def cleanBOK(textfile):

  departmentCode = input("Enter a department code you are interested in (ie SDS): ")
  departmentCode = departmentCode.upper()

  ##Import CSV as Dataframes
  schools_df = pd.read_csv("Smith-07-10-2020-FROZEN.csv")
  del(schools_df['Unnamed: 0'])
  sds_temp = []
  sds_array = []
  for i in range(len(schools_df)-1): #for each course
      cID = str(schools_df['CourseID'][i])
      if departmentCode in cID: #if that course is in the SDS department
          sds_temp = (schools_df['CourseID'][i])
          sds_array.append(sds_temp) #append  to the fixed list of SDS courses
  ###print("sds_array:",sds_array) 

  
  '''
  take the description, go word by word, and take out stop words
  '''
  sds_df = pd.DataFrame(sds_array) #create permanent new data frame
  sds_df.columns = ['CourseID'] #label columns

  sds_terms = []
  ###an array with just the words in the cID, no "sds ### "
  for i in range(len(sds_df)): # for each row
    cID = sds_df.loc[i,'CourseID']
    cID = cID[8:]
    if(cID != ''):
      sds_terms.append(cID)
  #print(sds_terms)

  #change this to be the uploaded text file
  with open('bok.txt','a+') as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data = file_object.read(10)
    if len(data) > 0 :
        file_object.write("\n")
    # Append text at the end of file
    for i in range(len(sds_terms)):
      file_object.write(sds_terms[i] + '\n')
    file_object.close()
    

  #change this to be the uploaded text file
  text_file=""
  # function that adds s and es etc
  with open('bok.txt','r') as file:
      for line in file:
          text_file+=line.strip()+"\n" # skip first one (the original one)
          text_file+=line.strip()+"s\n" # add s 
          text_file+=line.strip()+"es\n" # add es 
      file.close()
  with open('bok.txt','w') as file:
      file.write(text_file)
      file.close()
  bok1 = open('bok.txt','r') # re assign to new text list 
  bok = bok1.read().split('\n')
  for i in range(len(bok)): #lowercase each bok term
    bok[i] = bok[i].lower()
  
  return bok






