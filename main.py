import math
import wandb
import torch
from rich import print
wandb.init()




def log_wandb_distribution(key, samples, quantiles: list = None):
    assert len(samples.shape) == 1
    

    if quantiles is None:
        quantiles = [0.0001, 0.01, 0.05, 0.10, 0.25]
    
    # all values less than 0.5
    assert all([q < 0.5 for q in quantiles])    
    quantiles = quantiles + [0.5] + [1 - q for q in quantiles[::-1]] # add median
    
    dist_quantiles = torch.quantile(samples, torch.tensor(quantiles))
    
    d =  {
            key + f'/{q}': dist_quantiles[i].item() for i, q in enumerate(quantiles)
        }

    if wandb.run is None:
        print(d)
    else:
        wandb.log(
            d
        )
    # not a good solution since this is not editable over time    
    # d = {
    #     key: wandb.plot.line_series(
    #         xs=list(range(dist_quantiles.shape[1])),
    #         ys=dist_quantiles,
    #         keys=quantiles,
    #         title="Distribution over time",
    #         xname="Time Step",
    #     )
    # }




gaussian_process = []

for i in range(1, 100):
    data = torch.randn(100) * math.log(i)
    gaussian_process.append(data)
    log_wandb_distribution("gaussian_process", data)
