def rank_teams(votes: list[str]) -> str:
    hash_map = {}
    for vote in votes:
        for i, team in enumerate(vote):
            if team not in hash_map:
                hash_map[team] = [0] * len(vote)
            hash_map[team][i] += 1
            
    alphabetical_order_teams = sorted(hash_map.keys())
    ranked_teams = "".join(sorted(alphabetical_order_teams, key=lambda x: hash_map[x], reverse=True))
    return ranked_teams


if __name__ == '__main__':
    votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
    
    print(rank_teams(votes))