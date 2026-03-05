from collections import defaultdict
from app.models import AwardInterval

def calculate_intervals(movies):
    winners = [m for m in movies if m.winner]
    producer_wins = defaultdict(list)

    for movie in winners:
        for producer in movie.producers:
            producer_wins[producer].append(movie.year)

    intervals = []
    for producer, years in producer_wins.items():
        if len(years) < 2:
            continue

        years.sort()

        for i in range(1, len(years)):
            previous_year = years[i - 1]
            following_year = years[i]
            interval = following_year - previous_year

            intervals.append(
                AwardInterval(
                    producer=producer,
                    interval=interval,
                    previousWin=previous_year,
                    followingWin=following_year,
                )
            )

    if not intervals:
        return {"min": [], "max": []}
    
    min_interval = min(i.interval for i in intervals)
    max_interval = max(i.interval for i in intervals)

    min_list = [i.__dict__ for i in intervals if i.interval == min_interval]
    max_list = [i.__dict__ for i in intervals if i.interval == max_interval]

    return {
        "min": min_list,
        "max": max_list,
    }