from recommender import get_recommendations

def test_recommender():
    result = get_recommendations(1, top_n=2)
    assert isinstance(result, list)
    assert len(result) > 0
