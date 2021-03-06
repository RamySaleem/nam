from typing import List

import numpy as np
import torch


def get_num_units(
    config,
    dataloader: torch.utils.data.DataLoader,
) -> List:
  features, targets, *weights = next(iter(dataloader))

  num_unique_vals = [
      len(np.unique(features[:, i])) for i in range(features.shape[1])
  ]

  num_units = [
      min(config.num_basis_functions, i * config.units_multiplier)
      for i in num_unique_vals
  ]

  return num_units
