#based on https://gist.github.com/bonzanini/5a4c39e4c02502a8451d

import Bio

from Bio import Entrez

#searching PubMed

def search(query):
    Entrez.email = 'random@gmail.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', #PubMed sort
                            retmax='150', #number of papers 
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'random@gmail.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results
import json
out_file = open("myfile1.json", "w")  #saving to json file
if __name__ == '__main__':
    results = search('pine') #PubMed search phrase
    id_list = results['IdList']
    papers = fetch_details(id_list)
    for i, paper in enumerate(papers['PubmedArticle']):
       print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
       print(json.dump(papers['PubmedArticle'][i], out_file, indent=2, separators=(',', ':')))




          
