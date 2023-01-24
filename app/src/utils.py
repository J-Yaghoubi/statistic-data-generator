import scipy.stats


def dist(min_val: float, max_val: float, mean: float, std: float):
    """
    Generate scaled beta distribution
    """
    scale = max_val - min_val
    unscaled_mean = (mean - min_val) / scale
    unscaled_var = (std / scale) ** 2    

    # computation of alpha and beta can be derived from mean and variance formulas
    t = unscaled_mean / (1 - unscaled_mean)
    beta = ((t / unscaled_var) - (t * t) - (2 * t) - 1) / ((t * t * t) + (3 * t * t) + (3 * t) + 1)
    alpha = beta * t
   
    # not all parameters may produce a valid distribution
    if alpha <= 0 or beta <= 0:
        raise ValueError('Sorry! Cannot create distribution for the given parameters...')
    
    # return scaled beta distribution with computed parameters
    return scipy.stats.beta(alpha, beta, scale=scale, loc=min_val)