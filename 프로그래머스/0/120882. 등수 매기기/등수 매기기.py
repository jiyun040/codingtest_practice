def solution(score):
    avg_scores = [(sum(s) / 2) for s in score]
    sorted_scores = sorted(avg_scores, reverse=True)

    ranks = []
    for avg in avg_scores:
        rank = sorted_scores.index(avg) + 1
        ranks.append(rank)

    return ranks