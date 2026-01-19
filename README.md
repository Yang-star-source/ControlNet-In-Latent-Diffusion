# ControlNet-In-Latent-Diffusion
Build ControlNet from scratch based on pretrained Latent Diffusion

<p>
  <img src="images/sample1.png" width="600" title="Sample Result">
  <img src="images/sample2.png" width="600" title="Sample Result">
  <img src="images/sample3.png" width="600" title="Sample Result">
</p>

## Architecture

**Z** : Noisy Latent , time embedding

**X**: a copy of z

**C** : condition , cat's canny map were used in this training

**Blue Block** : Freeze during training

**Green Block**: Trainable

<p>
  <img src="images/flowchart1.png" width="600" title="Flow Chart">
</p>

