import requests

BASE_URL = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search'

def fetch_articles(query: str, limit: int=5, open_access: bool=False):
    search_query = query

    if open_access:
        search_query += " OPEN_ACCESS:y"

    params = {
        "query": search_query,
        "format": "json",
        "resultType": "core", # for the abstract 
        "pageSize": limit
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: The API request failed --> {e}")
        return []

    raw_result = data.get("resultList").get("result")
    articles = []

    for item in raw_result:
        article = {
            "id": item.get("id"),
            "title": item.get("title", "Could not be found."),
            "author": item.get("authorString"),
            "abstract": item.get("abstractText", "There is no abstarct info."),
            "doi": item.get("doi"),
            "pub_year": item.get("pubYear")
        }

        articles.append(article)

    return articles

