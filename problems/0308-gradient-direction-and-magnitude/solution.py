import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    g = np.array(gradient, dtype=float)
    magnitude = np.linalg.norm(g)

    if magnitude == 0:
        zeros = [0.0] * len(g)
        return {"magnitude": 0.0, "direction": zeros, "descent_direction": zeros}

    direction = g / magnitude

    return {
        "magnitude": float(magnitude),
        "direction": direction.tolist(),
        "descent_direction": (-direction).tolist()
    }