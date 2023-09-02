import os
import random
import re
import sys
import random

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    pages = get_pages(corpus)
    model = dict()

    if corpus[page]:
        for pag in pages:
            if pag in corpus[page]:
                model[pag] = damping_factor/len(corpus[page]) + (1-damping_factor)/len(pages)
            else:
                model[pag] = (1-damping_factor)/len(pages)
    else:
        for pag in pages:
            model[pag] = 1/len(pages)

    p = 0

    for key in model:
        p += model[key]

    return model
    #raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pages = get_pages(corpus)
    pagerank = dict()
    for page in pages:
        pagerank[page] = 0

    for i in range(n):
        if i == 0:
            page = random.choice(pages)
            pagerank[page] += 1/n
        else:
            weight_model = list()
            trans_model = transition_model(corpus,page,damping_factor)
            for key in trans_model:
                weight_model.append(trans_model[key])

            page_r = random.choices(pages, weight_model)
            page = page_r[0]
            pagerank[page] += 1/n

    return pagerank

    #raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = get_pages(corpus)
    anti = anti_corpus(corpus)
    pagerank = dict()
    pages_tolerance = dict()

    for page in pages:
        if not corpus[page]:
            #print(f"Page {page} has no links. All pages will be included")
            for p in pages:
                corpus[page].add(p)

    #print(f"New corpus: {corpus}")
    #Initialization in 1/N
    for page in pages:
        pagerank[page] = 1/len(pages)
        pages_tolerance[page] = 1

    e = max_value(pages_tolerance)
    temp = dict()

    #Starting pagerank
    while (e > 0.0001):
        # Save the values for futur testing
        for page_key in pagerank:
            temp[page_key] = pagerank[page_key]

        #Update each probability for each page in the corpus
        for page_key in pagerank:
            pagerank[page_key] = (1 - damping_factor) / len(pages)
            for page_link in anti[page_key]:
                pagerank[page_key] += (damping_factor * pagerank[page_link] / len(corpus[page_link]))

        #Once the updated values Normalize the values
        sum = 0
        for page_key in pagerank:
            sum += pagerank[page_key]

        for page_key in pagerank:
            pagerank[page_key] /= sum

        for page_key in pagerank:
            pages_tolerance[page_key] = abs(pagerank[page_key] - temp[page_key])

        e = max_value(pages_tolerance)
        #print(f"New 'e' max: {e}")

    return pagerank
    #raise NotImplementedError

def get_pages(corpus):

    pages = list()
    #Collecting only the pages in corpus
    for key_page in corpus:
        if key_page not in pages:
            pages.append(key_page)
        for ref_pag in corpus[key_page]:
            if ref_pag not in pages:
                pages.append(ref_pag)

    return pages

def anti_corpus(corpus):
    pages = get_pages(corpus)
    anti_corpus =dict()

    for page in pages:
        anti_corpus[page] = set()

    for page in pages:
        for page_link in corpus[page]:
            if page not in anti_corpus[page_link]:
                anti_corpus[page_link].add(page)
    return anti_corpus

def max_value(d):
    max = list(d.values())[0]
    for key in d:
        if d[key] > max:
            max = d[key]
    return max

if __name__ == "__main__":
    main()
