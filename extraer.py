from functools import *
import re
"""

1.1.1 The primary activities of software engineering
"""

def incertarSaltos(saltos, texto):
	if saltos:
		return incertarSaltos(saltos[1:], "".join(re.sub(saltos[0],"\n"+saltos[0],texto)))
	else:
		return texto


def quitarSalto(texto):
	return "".join(re.sub("\n"," ",texto))

a="""Probabilistic Latent Semantic Indexing The probabilistic latent semantic indexing (PLSI) method is similar to LSI, but achieves dimensionality reduction through a probabilistic mixture model. Speciﬁcally, we assume there are k latent common themes in the document collection, and each is characterized by a multinomial word distribution. A document is regarded as a sample of a mixture model with these theme models as components. We ﬁt such a mixture model to all the documents, and the obtained k component multinomial models can be regarded as deﬁning k new semantic dimensions. The mixing weights of a document can be used as a new representation of the document in the low latent semantic dimensions. 

Formally, let C = {fd 1 ;d 2 ;:::;d n g} be a collection of n documents. Let {q1 ;:::;q k be k} theme multinomial distributions. A word w in document di is regarded as a sample of the following mixture model. 

(10.14) 

where p d i ; j is a document-speciﬁc mixing weight for the j-th aspect theme, and å k j=1 p d i ; j = 1. The log-likelihood of the collection C is 

(10.15) 

where V is the set of all the words (i.e., vocabulary), c(w;d i ) is the count of word w in document d i , and =(fq j ;fp d i ; j g n i=1 g k j=1 ) is the set of all the theme model parameters. The model can be estimated using the Expectation-Maximization (EM) algorithm (Chapter 7), which computes the following maximum likelihood estimate: (10.16) 

Once the model is estimated, q 1 ;:::;q k deﬁne k new semantic dimensions and p d i ; j gives a representation of d i in this low-dimension space. 

10.4.3 Text Mining Approaches
There are many approaches to text mining, which can be classiﬁed from different perspectives, based on the inputs taken in the text mining system and the data mining tasks to be performed. In general, the major approaches, based on the kinds of data they take as input, are: (1) the keyword-based approach, where the input is a set of keywords or terms in the documents, (2) the tagging approach, where the input is a set of tags, and (3) the information-extraction approach, which inputs semantic information, such as events, facts, or entities uncovered by information extraction. A simple keyword-based approach may only discover relationships at a relatively shallow level, such as rediscovery of compound nouns (e.g., “database” and “systems”) or co-occurring patterns with less signiﬁcance (e.g., “terrorist” and “explosion”). It may not bring much deep understanding to the text. The tagging approach may rely on tags obtained by manual tagging (which is costly and is unfeasible for large collections of documents) or by some automated categorization algorithm (which may process a relatively small set of tags and require deﬁning the categories beforehand). The information-extraction approach is more advanced and may lead to the discovery of some deep knowledge, but it requires semantic analysis of text by natural language understanding and machine learning methods. This is a challenging knowledge discovery task. 

Various text mining tasks can be performedon the extracted keywords, tags, or semantic information. These include document clustering, classiﬁcation, information extraction, association analysis, and trend analysis. We examine a few such tasks in the following discussion. 

Keyword-Based Association Analysis “What is keyword-based association analysis?” Such analysis collects sets of keywords or terms that occur frequently together and then ﬁnds the association or correlation relationships among them. 

Like most of the analyses in text databases, association analysis ﬁrst preprocesses the text data by parsing, stemming, removing stop words, and so on, and then evokes association mining algorithms. In a document database, each document can be viewed as a transaction, while a set of keywords in the document can be considered as a set of items in the transaction. That is, the database is in the format {document id;a set of keywordsg} 

The problem of keyword association mining in document databases is thereby mapped to item association mining in transaction databases, where many interesting methods have been developed, as described in Chapter 5."""

saltos = ["#"]

print(len(a))