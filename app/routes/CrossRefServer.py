from flask import Blueprint, request, jsonify
import requests
from urllib.parse import quote_plus

crossRef_bp = Blueprint('CrossRef', __name__)

@crossRef_bp.route('/crossref/paper_by_doi/<path:doi>', methods=['GET'])
def fetch_recommendation_paper_based_on_doi(doi):
    print(f"DOI received: {doi}")
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

@crossRef_bp.route('/crossref/paper_by_title/<path:title>', methods=['GET'])
def fetch_paper_authors_based_on_doi(title):
    encoded_title = quote_plus(title)  # Ensures that the title is URL-safe
    url = f"https://api.crossref.org/works?query.title={encoded_title}"
    print(f"Title received: {title}")
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500