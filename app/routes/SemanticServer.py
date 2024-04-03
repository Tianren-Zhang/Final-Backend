from flask import Blueprint, request, jsonify
import requests

semantic_bp = Blueprint('Semantic', __name__)

@semantic_bp.route('/semantic/recommendations/<path:doi>', methods=['GET'])
def fetch_recommendation_paper_based_on_doi(doi):
    print(f"DOI received: {doi}")
    url = f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/{doi}?limit=10&fields=title,url,abstract,authors"
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

@semantic_bp.route('/semantic/paper_authors/<path:doi>', methods=['GET'])
def fetch_paper_authors_based_on_doi(doi):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}/authors?fields=name,paperCount,citationCount,url&offset=0"
    print(f"DOI received: {doi}")
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

@semantic_bp.route('/semantic/authors/<authorId>', methods=['GET'])
def fetch_author_based_on_id(authorId):
    url = f"https://api.semanticscholar.org/graph/v1/author/{authorId}?fields=name,url,papers.abstract,papers.url,papers.title"
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        print(response.json());
        return jsonify({"error": "Failed to fetch data"}), 500

