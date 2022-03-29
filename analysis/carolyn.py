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

#all_stopwords = sp.Defaults.stop_words

##Import CSV as Dataframes
schools_df = pd.read_csv("Smith-07-10-2020-FROZEN.csv")
del(schools_df['Unnamed: 0'])
sds_temp = []
sds_array = []
for i in range(len(schools_df)-1): #for each course
    cID = str(schools_df['CourseID'][i])
    if "SDS" in cID: #if that course is in the SDS department
        sds_temp = (schools_df['CourseID'][i], schools_df['Descriptions'][i])
        sds_array.append(sds_temp) #append  to the fixed list of SDS courses
###print("sds_array:",sds_array) 

 
'''
take the description, go word by word, and take out stop words
'''
sds_df = pd.DataFrame(sds_array) #create permanent new data frame
sds_df.columns = ['CourseID','Descriptions'] #label columns

#stop words definition
stop_words = list(stopwords.words('english'))
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
stop_words.append('-PRON-')
first_stops = ['cr','ul','ii','cog','pp','ps','geog','cosc','biol','el','sesp',
               'eecs','oba','phys','phy','mth','cmsc','nur','ce','cs','iii'] #unkown/unnecessary abbreviations
second_stops = ['make','impact','apply','change','involve','reside','vary','may',
                'meet','use','include','pertain','tell','cover','devote',
                'recognize','carry'] #verbs that are not useful
third_stops = ['new','minimum','useful','mainly','large','liberal','formerly',
               'especially','absolutely','graduate','odd','one','throughout',
               'weekly','least','well','hour','common','require','along','least',
               'long','related','prior','open','sophomore','junior','single',
               'necessary'] #unuseful descriptors
fourth_stops = ['treat','prereq','prerequisite','creditsprerequisite',
                'corequisite','either','assignment','major','none','arts','core',
                'andor','semester','hoursprereq','student','instructor','threehour',
                'within','lecturescover','satisfactoryno','summer','yifat',
                'givenfor','term','classroom','area','inquiry','researchintensive',
                'year','via','teacher','ofhow'] #other unuseful words
#our additionnal stops
fifth_stops = ['with', 'intro', 'introduction', 'to', 'and', 'special', 'studies', '&', 'topics', 'in', 'seminar', 'capstone', 'colloquium', 'lecture', 'undergraduates']
stop_words.extend(first_stops)
stop_words.extend(second_stops)
stop_words.extend(third_stops)
stop_words.extend(fourth_stops)
stop_words.extend(fifth_stops)
#print(stop_words)

deleted_words = ""
#remove stopwords from df:
for i in range(len(sds_df)): # for each row
  cID = sds_df.loc[i,'CourseID'].lower().split() #go into each course' cID
  j = len(cID) - 1
  while j >=0:
    if cID[j] in stop_words:
      deleted_words = deleted_words + cID[j]
      del cID[j]
    j-=1
  sds_df.loc[i,'CourseID'] = ' '.join(cID)   
#print('deleted:\n', deleted_words) 
#print('sds_df with stop words removed:\n',sds_df)

sds_terms = []
###an array with just the words in the cID, no "sds ### "
for i in range(len(sds_df)): # for each row
  cID = sds_df.loc[i,'CourseID']
  cID = cID[8:]
  if(cID != ''):
    sds_terms.append(cID)
print(sds_terms)


with open('blank5.txt','a+') as file_object:
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
  
        


text_file=""
# function that adds s and es etc
with open('blank4.txt','r') as file:
    for line in file:
        text_file+=line.strip()+"\n" # skip first one (the original one)
        text_file+=line.strip()+"s\n" # add s 
        text_file+=line.strip()+"es\n" # add es 
    file.close()
with open('blank4.txt','w') as file:
    file.write(text_file)
    file.close()
bok1 = open('blank4.txt','r') # re assign to new text list 
bok = bok1.read().split('\n')
for i in range(len(bok)): #lowercase each bok term
  bok[i] = bok[i].lower()






