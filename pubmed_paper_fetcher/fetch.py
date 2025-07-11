import requests
from xml.etree import ElementTree as ET
from typing import List, Dict
from pubmed_paper_fetcher.utils import is_non_academic_author

def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = f"{base_url}esearch.fcgi"
    fetch_url = f"{base_url}efetch.fcgi"

    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # number of papers to fetch
    }

    res = requests.get(search_url, params=params)
    ids = res.json().get("esearchresult", {}).get("idlist", [])
    if debug:
        print(f"Found PubMed IDs: {ids}")

    if not ids:
        return []

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }

    res = requests.get(fetch_url, params=fetch_params)
    root = ET.fromstring(res.content)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        authors = article.findall(".//Author")

        non_academic_authors = []
        affiliations = []

        for author in authors:
            name = author.findtext("LastName", "") + " " + author.findtext("ForeName", "")
            aff = author.findtext(".//AffiliationInfo/Affiliation", "")
            if is_non_academic_author(aff):
                non_academic_authors.append(name.strip())
                affiliations.append(aff.strip())

        if non_academic_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": ", ".join(non_academic_authors),
                "Company Affiliation(s)": ", ".join(affiliations),
                "Corresponding Author Email": "N/A"
            })

    return papers
