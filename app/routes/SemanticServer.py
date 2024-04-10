from flask import Blueprint, request, jsonify
import requests
import plotly.express as px
semantic_bp = Blueprint('Semantic', __name__)

@semantic_bp.route('/semantic/recommendations/<path:doi>', methods=['GET'])
def fetch_recommendation_paper_based_on_doi(doi):
    print(f"DOI received: {doi}")
    url = f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/{doi}?limit=10&fields=title,url,abstract,authors"
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        print(response.json());
        return jsonify({"error": "Failed to fetch data"}), 500

@semantic_bp.route('/semantic/easyrecommendations/<path:doi>', methods=['GET'])
def fetch_easyrecommendation_paper_based_on_doi(doi):
    print(f"DOI received: {doi}")
    url = f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/{doi}?limit=5&fields=title"
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        print(response.json());
        return jsonify({"error": "Failed to fetch data"}), 500


@semantic_bp.route('/semantic/paper_authors/<path:doi>', methods=['GET'])
def fetch_paper_authors_based_on_doi(doi):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}/authors?fields=name,paperCount,citationCount,url&offset=0"
    print(f"DOI received: {doi}")
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        print(response.json());
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

@semantic_bp.route('/semantic/authors/citations/<path:doi>', methods=['GET'])

def fetch_cited_by_based_on_doi(doi):
    offset = request.args.get('offset', '0')
    limit = request.args.get('limit', '7')
    url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}/citations?fields=year,title&offset={offset}&limit={limit}"
    response = requests.get(url)
    if response.ok:
        return jsonify(response.json())
    else:
        print(response.json());
        return jsonify({"error": "Failed to fetch data"}), 500


def build_graph(child, parent):
    fig = px.treemap(
        names=child,
        parents=parent
    )
    fig.update_traces(
        root_color="lightgrey",
        marker=dict(cornerradius=5),
        textfont=dict(size=30)
    )
    fig.update_layout(
        margin=dict(t=5, l=5, r=5, b=5),
        font=dict(size=40)
    )

    return fig.to_json()
@semantic_bp.route('/semantic/treemap-data', methods = ['POST'])

def get_treemap_data():
    
    data = request.json
    children_list = data['children']
    parent_list = data['parent']

    return build_graph(children_list, parent_list)



