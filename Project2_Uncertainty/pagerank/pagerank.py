import os
import random
import re
import sys
import copy

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
    Prob_Distribustion = {}

    links = corpus[page]
    length = len(links)
    if length:

        for link in corpus.keys():
            Prob_Distribustion[link] = (1 - damping_factor) / len(corpus)

        for link in corpus[page]:
            Prob_Distribustion[link] += damping_factor / len(corpus[page])

    else:
        for link in corpus:
            Prob_Distribustion[link] = 1/len(corpus)

    return Prob_Distribustion


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    Page_rank ={}

    #set all keys in corpus to value 0
    for link in corpus:
        Page_rank[link] = 0

    sample = random.choice(list(corpus.keys()))

    for i in range(1,n):
        sample_pg = transition_model(corpus, sample, damping_factor)

        for page in sample_pg:
            Page_rank[page] = ((i-1) * Page_rank[page] + sample_pg[page]) / i

        page = random.choices(list(Page_rank.keys()), list(Page_rank.values()), k = 1)[0]

    return Page_rank




def iterate_pagerank(corpus, damping_factor):

    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    d = damping_factor
    n = len(corpus)

    Page_rank = {}

    for page in corpus:
        Page_rank[page] = 1 / n

    stop = 0
    while not stop:

        stop = 1
        topr ={}

        for i in Page_rank.keys():

            temp = Page_rank[i]

            topr[i] = float((1 - d) / n)

            for page, link in corpus.items():
                if i in link:
                    topr[i] += float(d * Page_rank[page]/len(link))

            if abs(temp - topr[i]) > 0.001:
                stop =0

        for i in Page_rank.keys():
            Page_rank[i] = topr[i]

        return Page_rank


    raise NotImplementedError


if __name__ == "__main__":
    main()
