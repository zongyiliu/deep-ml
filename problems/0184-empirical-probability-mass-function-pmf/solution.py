from collections import Counter

def empirical_pmf(samples):
    if not samples:
        return []
    
    n = len(samples)
    counts = Counter(samples)               # {value: count}
    
    # Sort by value, compute probability for each
    return [(value, count / n) for value, count in sorted(counts.items())]