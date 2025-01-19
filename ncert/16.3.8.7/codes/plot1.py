import random
import matplotlib.pyplot as plt

def simulate_coin_tosses(num_trials):
    # Array to count occurrences of 0, 1, 2, and 3 tails
    results = [0, 0, 0, 0]

    for _ in range(num_trials):
        tails = 0
        # Toss three coins
        for _ in range(3):
            if random.randint(0, 1) == 0:  # 0 represents tails
                tails += 1
        results[tails] += 1
    
    return results

def main():
    num_trials = 100000  # Number of trials for simulation
    results = simulate_coin_tosses(num_trials)

    # Calculate probabilities
    probabilities = [count / num_trials for count in results]

    print("Probabilities for 0, 1, 2, and 3 tails:", probabilities)
    print("Probability of exactly 2 tails:", probabilities[2])

    # Plot the results
    outcomes = ['0 Tails', '1 Tail', '2 Tails', '3 Tails']
    plt.bar(outcomes, probabilities, color='skyblue')
    plt.title('Probability Distribution of Tails in 3 Coin Tosses')
    plt.ylabel('Probability')
    plt.xlabel('Number of Tails')
    plt.ylim(0, 0.5)
    plt.show()

if __name__ == "__main__":
    main()

