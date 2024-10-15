def find_max_score(levels: list, scores: list):
    if not levels or not scores or len(levels) != len(scores):
        return ("Error", 0)
    max_score_index = scores.index(max(scores))
    return (levels[max_score_index], scores[max_score_index])

levels1 = ["Уровень 1", "Уровень 2", "Уровень 3", "Уровень 4"]
scores1 = [1000, 2500, 1500, 3000]

levels2 = ["Dungeon", "Forest", "Castle", "Mountain"]
scores2 = [600, 900, 700, 1200]

levels3 = ["Этап 1", "Этап 2", "Этап 3"]
scores3 = [450, 450, 450]

print(find_max_score(levels1, scores1))
print(find_max_score(levels2, scores2))
print(find_max_score(levels3, scores3)) 