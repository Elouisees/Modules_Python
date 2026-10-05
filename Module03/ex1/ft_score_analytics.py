#!/usr/bin/env python3

import sys


def score_check(score: int) -> int:
    if int(score) < 0:
        raise ValueError
    else:
        return score


if __name__ == "__main__":
    all_scores: list[int] = []

    print("=== Player Score Analytics ===")

    for i in range(1, len(sys.argv)):
        try:
            all_scores.append(score_check(int(sys.argv[i])))
        except Exception:
            print(f"Invalid parameter: '{sys.argv[i]}'")

    if len(sys.argv) == 0 or len(all_scores) == 0:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
    else:
        print("Scores processes: ", all_scores)
        print("Total players: ", len(all_scores))
        print("Total score: ", sum(all_scores))
        print("Average score: ", sum(all_scores) / len(all_scores))
        print("High score: ", max(all_scores))
        print("Low score: ", min(all_scores))
        print("Score range: ", max(all_scores) - min(all_scores))
