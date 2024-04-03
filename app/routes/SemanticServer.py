from flask import Blueprint, request, jsonify
import requests

papers_bp = Blueprint('papers', __name__)

@papers_bp.route('/recommendations/<path:doi>', methods=['GET'])
def fetch_recommendation_paper_based_on_doi(doi):
    print(f"DOI received: {doi}")
    url = f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/{doi}?limit=10&fields=title,url,abstract,authors"
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

@papers_bp.route('/paper_authors/<path:doi>', methods=['GET'])
def fetch_paper_authors_based_on_doi(doi):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}/authors?fields=name,paperCount,citationCount,url&offset=2"
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

