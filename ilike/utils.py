from cobaya.yaml import yaml_load_file

def is_converged(pattern):
    """
    Check if the MCMC sampler has converged by reading the convergence status from a checkpoint file.
    Parameters
    ----------
    pattern : str
        The pattern used to construct the checkpoint filename (e.g., "my_run").
    Returns
    -------
    converged : bool
        True if the MCMC sampler has converged, False otherwise.

    """
    fname = pattern + ".checkpoint"
    return yaml_load_file(fname)["sampler"]["mcmc"]["converged"]

