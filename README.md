# Wandb histogram over time example

Edit: wandb supports this natively. Below solution is still useful though.

```
import wandb
wandb.init()
import numpy as np
import math
for i in range(1, 1000):
    wandb.log({'gaussian_process':wandb.Histogram(np.random.randn(1000) * math.log(i) / 1000)})
wandb.finish()
```

I wanted this:

![tensorboard histogram over time](tensorboard.png)

So I made this repo to do it in wandb, inspired by [this](https://stackoverflow.com/questions/71506186/how-to-get-create-a-histogram-over-time).

![seaborn histogram over time](seaborn.png)

Result:

![wandb histogram over time](wandb.png)

Unfortunately you still have to add a panel manually since wandb doesn't offer a programmatic way to do this. Just click 'edit panel', and you should see the following:

![edit-wandb](edit-wandb.png)
