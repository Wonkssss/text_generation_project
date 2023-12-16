from __future__ import annotations

from itertools import cycle, chain
from torch.optim import Optimizer
from torch.optim.lr_scheduler import LRScheduler
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm

import builtins
import math
import torch
import torch.nn as nn
import torch.nn.functional as F

superheroes_ds = SuperHeroes()