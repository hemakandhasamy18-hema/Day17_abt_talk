# ==========================================
# DAY 17 - BACKTRACKING & SEARCH
# Generate All Subsets
# ==========================================

def generate_subsets(gems):
    result = []
    current = []

    def backtrack(index):
        # Base case
        if index == len(gems):
            result.append(current.copy())
            return

        # Choice 1: Include the current gem
        current.append(gems[index])
        backtrack(index + 1)

        # Backtrack: remove the gem
        current.pop()

        # Choice 2: Exclude the current gem
        backtrack(index + 1)

    backtrack(0)

    return result


# Input gems
gems = ["Ruby", "Diamond", "Emerald"]

# Generate all subsets
subsets = generate_subsets(gems)

# Display results
print("======================================")
print("      MAGICAL TREASURE CHEST")
print("======================================")

print("\nGems:", gems)

print("\nAll Possible Combinations:")

for i, subset in enumerate(subsets, 1):
    print(f"{i}. {subset}")

# Count total combinations
print("\nTotal Combinations:", len(subsets))

# Expected number of subsets
print("Expected Combinations:", 2 ** len(gems))