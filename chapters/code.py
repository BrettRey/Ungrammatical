import random
import argparse
import matplotlib.pyplot as plt
import numpy as np

def init_speakers(num_speakers, initial_grammar):
    speakers = []
    for _ in range(num_speakers):
        speakers.append({
            "grammar": initial_grammar.copy(),
            "status": np.random.rand()  # Random status between 0 and 1
        })
    return speakers

def update_grammar(speaker, heard_adj, heard_construction, base_learning_rate, threshold):
    current_raising_acceptability = speaker["grammar"][heard_adj]["raising"]
    heard_raising_acceptability = 1 if heard_construction == "raising" else 0
    
    # Calculate the non-linear learning rate based on the current acceptability
    learning_rate = base_learning_rate * current_raising_acceptability * (1 - current_raising_acceptability)
    
    # Update raising acceptability based on the difference from the threshold
    difference = heard_raising_acceptability - threshold
    speaker["grammar"][heard_adj]["raising"] += learning_rate * difference
    
    # Ensure raising acceptability stays within [0, 1]
    speaker["grammar"][heard_adj]["raising"] = max(0, min(1, speaker["grammar"][heard_adj]["raising"]))
    
    # Update non-raising acceptability
    speaker["grammar"][heard_adj]["non-raising"] = 1 - speaker["grammar"][heard_adj]["raising"]

def innovate(speaker, adjectives, innovation_chance):
    if random.random() < innovation_chance:
        new_adj = random.choice(list(adjectives.keys()))
        speaker["grammar"][new_adj] = {"raising": np.random.rand() * 0.3, "non-raising": np.random.rand() * 0.7 + 0.3}
        # Normalize the acceptabilities
        total = sum(speaker["grammar"][new_adj].values())
        for construction in speaker["grammar"][new_adj]:
            speaker["grammar"][new_adj][construction] /= total

def simulate(speakers, adjectives, generations, base_learning_rate, innovation_chance, threshold):
    history = {adj: [] for adj in adjectives}
    for generation in range(generations):
        for speaker in speakers:
            for _ in range(5):
                adj = random.choice(list(speaker["grammar"].keys()))
                if random.random() < speaker["grammar"][adj]["raising"]:
                    construction = "raising"
                else:
                    construction = "non-raising"
            for _ in range(3):
                other_speaker = random.choice(speakers)
                heard_adj = random.choice(list(other_speaker["grammar"].keys()))
                heard_construction = "raising" if random.random() < other_speaker["grammar"][heard_adj]["raising"] else "non-raising"
                update_grammar(speaker, heard_adj, heard_construction, base_learning_rate, threshold)
                innovate(speaker, adjectives, innovation_chance)
        for adj in adjectives:
            history[adj].append(sum(s["grammar"][adj]["raising"] for s in speakers) / len(speakers))
    return history

def visualize(history, generations):
    for adj, scores in history.items():
        plt.plot(range(generations), scores, label=adj)
    plt.xlabel("Generation")
    plt.ylabel("Average Acceptability in Raising")
    plt.legend()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Language change simulation")
    parser.add_argument("--num_speakers", type=int, default=100, help="Number of speakers")
    parser.add_argument("--generations", type=int, default=200, help="Number of generations")
    parser.add_argument("--base_learning_rate", type=float, default=0.1, help="Base learning rate")
    parser.add_argument("--innovation_chance", type=float, default=0.01, help="Innovation chance")
    parser.add_argument("--threshold", type=float, default=0.6, help="Acceptability threshold for raising construction")
    args = parser.parse_args()

    adjectives = {
        "likely": {"raising": 0.9, "non-raising": 0.1},
        "happy": {"raising": 0.5, "non-raising": 0.5},
        "eager": {"raising": 0.3, "non-raising": 0.7},
        "reluctant": {"raising": 0.1, "non-raising": 0.9}
    }

    speakers = init_speakers(args.num_speakers, adjectives)
    history = simulate(speakers, adjectives, args.generations, args.base_learning_rate, args.innovation_chance, args.threshold)
    visualize(history, args.generations)

if __name__ == "__main__":
    main()