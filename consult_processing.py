import csv
import json
import operator
import os

import numpy as np
from bs4 import BeautifulSoup

from inverted_index import utils

inv_index = utils.readIndexFromCsv('./inverted_index/')


def get_attr(attr):
    attr_dict = dict()
    for key, value in inv_index.items():
        a, item = key.split('.')
        if a == attr.title():
            attr_dict[item] = value
    return attr_dict


def get_targets(query):
    doc_dict = dict()
    for key, values in inv_index.items():
        _, item = key.split('.')
        values = json.loads(values)
        if item in query:
            for v in values:
                try:
                    doc_dict[v[0]].append((item, v[1]))
                except KeyError:
                    doc_dict[v[0]] = list()
                    doc_dict[v[0]].append((item, v[1]))
    return doc_dict


def doc_at_time_without_tfidf(query):
    doc_dict = get_targets(query)
    score_dict = dict()
    for key, values in doc_dict.items():
        score_dict[key] = 0
        for val in values:
            score_dict[key] += val[1]
        score_dict[key] *= len(values)
    score_sorted = sorted(score_dict.items(),
                          key=lambda kv: kv[1], reverse=True)
    score_sorted = [x[0] for x in score_sorted]
    return score_sorted, score_dict


def query_matrix(query):
    doc_dict = get_targets(query)
    q_matrix = dict()
    for key, values in doc_dict.items():
        for val in values:
            try:
                q_matrix[val[0]].append([key, val[1]])
            except:
                q_matrix[val[0]] = list()
                q_matrix[val[0]].append([key, val[1]])
    return q_matrix


def query_weight_matrix(query):
    q_matrix = query_matrix(query)
    query_tfidf = list()
    doc_tfidf = list()
    for _, values in q_matrix.items():
        term_idf = np.log2(80/len(values))
        doc_dict = dict()
        for v in values:
            doc_dict[v[0]] = v[1]
        doc_term_tf = list()
        query_term_tf = list()
        for i in range(1, 81):
            if i in doc_dict.keys():
                query_term_tf.append(doc_dict[i])
                doc_term_tf.append(doc_dict[i])
            else:
                query_term_tf.append(-1)
                doc_term_tf.append(0)

        query_term_tf = 0.5 + (0.5 * np.array(query_term_tf))
        query_term_tfidf = query_term_tf*term_idf
        query_tfidf.append(query_term_tfidf)

        doc_term_tf = np.array(doc_term_tf)*term_idf
        doc_tfidf.append(doc_term_tf)

    query_tfidf = np.array(query_tfidf)
    doc_tfidf = np.array(doc_tfidf)
    return doc_tfidf, query_tfidf


def cosine_score(query):
    doc_tfidf, query_tfidf = query_weight_matrix(query)
    query = query.split(' ')
    doc_score = dict()
    for term_index, pair in enumerate(doc_tfidf):
        for doc, val in enumerate(pair):
            doc_idx = doc + 1
            if doc_idx in doc_score.keys():
                doc_score[doc_idx] += val * query_tfidf[term_index][doc]
            else:
                doc_score[doc_idx] = val * query_tfidf[term_index][doc]
    texts = get_texts()
    for doc, score in doc_score.items():
        magnetude = len(texts[doc-1])
        doc_score[doc] = score/magnetude

    aux = doc_score
    for doc in list(aux):
        if aux[doc] == 0:
            doc_score.pop(doc, None)

    score_sorted = sorted(doc_score.items(),
                          key=lambda kv: kv[1], reverse=True)
    score_sorted = [x[0] for x in score_sorted]
    return score_sorted, doc_score


def get_texts():
    texts = list()
    texts_path = os.path.join(os.path.join(os.path.join(
        os.path.abspath('.'), 'inverted_index'), 'data'), 'texto')
    for text in [str(x)+'.txt' for x in range(1, 81)]:
        if text.endswith('.txt'):
            with open(os.path.join(texts_path, text), 'r') as f:
                txt = f.read()
                texts.append(txt)
                f.close()
    return texts


def spearman(normal, cosined):
    sume = 0
    for i, val in enumerate(normal):
        dim = i - cosined.index(val)
        sume += pow(dim, 2)
    divid = pow(len(normal), 3) - len(normal)
    if divid != 0:
        dim = 6*sume/divid
    else:
        dim = 0
    return 1 - dim


def make_pairs(normal, cosined):
    normal_pairs = list()
    cosined_pairs = list()
    for i, n in enumerate(normal):
        if i != len(normal)-1:
            for m in normal[i+1:]:
                normal_pairs.append([n, m])

    for i, n in enumerate(cosined):
        if i != len(cosined)-1:
            for m in cosined[i+1:]:
                cosined_pairs.append([n, m])

    return normal_pairs, cosined_pairs


def kendal_tau(normal, cosined):
    discordant = 0
    norp, cosp = make_pairs(normal, cosined)
    for n in norp:
        if not n in cosp:
            discordant += 1
    kt = discordant*-2
    if len(norp) != 0:
        kt /= len(norp)*2
    else:
        kt = 0
    return kt + 1


def get_htmls_from_list(topk):
    html_path = os.path.join(os.path.join(os.path.join(
        os.path.abspath('.'), 'inverted_index'), 'data'), 'html')
    htmls = [os.path.join(html_path, str(html)+'.html')
             for html in range(1, 81)]
    links = list()
    for x in topk:
        sauce = open(htmls[x-1], 'r')
        soup = BeautifulSoup(sauce, features='lxml')
        link = soup.find('link', {'rel': 'canonical'})
        if link is None:
            link = soup.find('meta', {'property': 'og:url'})
            links.append(link['content'])
        else:
            if not 'mundomax' in link['href']:
                links.append(link['href'])
            else:
                links.append(htmls[x-1])
    return links


def main():
    query = input()
    docs_without_tfidf, _ = doc_at_time_without_tfidf(query)
    docs_with_tfidf, _ = cosine_score(query)
    spearman_cor = spearman(docs_without_tfidf, docs_with_tfidf)
    kendal_tau_cor = kendal_tau(docs_without_tfidf, docs_with_tfidf)
    docs_with_tfidf = get_htmls_from_list(docs_with_tfidf)
    docs_without_tfidf = get_htmls_from_list(docs_without_tfidf)
    print("Top 5 escolhas sem TF-IDF:")
    for x in docs_without_tfidf[:5]:
        print(x)
    print("---------------------------------------------------------------------------")
    print("Top 5 escolhas com TF-IDF:")
    for x in docs_with_tfidf[:5]:
        print(x)
    print("---------------------------------------------------------------------------")
    print("Correlacao de Spearman:")
    print(spearman_cor)
    print("---------------------------------------------------------------------------")
    print("Correlacao de Kendal Tau:")
    print(kendal_tau_cor)
    print("---------------------------------------------------------------------------")

    return


if __name__ == "__main__":
    main()
