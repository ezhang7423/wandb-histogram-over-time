import wandb
wandb.init()


for i in range(100):
    wandb.log({'loss-1': 5+i, 'loss-2': i})