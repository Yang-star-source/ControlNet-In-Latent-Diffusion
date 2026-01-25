# ControlNet-In-Latent-Diffusion
This repository contains a manual implementation of ControlNet applied to an image generation model , Latent Diffusion Model (LDM), built entirely from scratch in PyTorch.

The model is trained to generate realistic cat images guided by **Canny Edge Maps**.

<table width="100%">
  <tr>
    <td align="center" width="50%">
      <img src="images/sample1.png" height="200px">
    </td>
    <td align="center" width="50%">
      <img src="images/T2ISample1.png" height="200px">
    </td>
  </tr>
  <tr>
    <td align="center"><b>Without Prompt</b></td>
    <td align="center"><b>Prompt: A cute orange cat with green eyes</b></td>
  </tr>
</table>

## Architecture
```
Z : Noisy Latent , time embedding
X : A copy of z
C : Condition , cat's canny map were used in this training
Blue Block : Freeze during training
Green Block: Trainable
```
<p>
  <img src="images/T21CNFlowChart.png" width="600" title="Flow Chart">
</p>

## Pre-trained Latent Diffusion 

This repo applied ControlNet on previous prebuilt Latent Diffusion Model from Scratch 

[Latent Diffusion From Scratch](https://github.com/Yang-star-source/Latent_Diffusion_From_Scratch)

## Codes Implementation

<table width="100%">
  <tr>
    <th align="center">ControlNet</th>
    <th align="center">Unconditional LDM</th>
    <th align="center">T2I LDM</th>
  </tr>
  <tr>
    <td><b>Training</b></td>
    <td align="center">
      <a href="https://colab.research.google.com/github/Yang-star-source/ControlNet-In-Latent-Diffusion/blob/main/ControlNet_Unconditional_LDM_Training.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
      </a>
    </td>
    <td align="center">
      <a href="https://colab.research.google.com/github/Yang-star-source/ControlNet-In-Latent-Diffusion/blob/main/ControlNet_T2I_LDM_Training.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
      </a>
    </td>
  </tr>
  <tr>
    <td><b>Inference</b></td>
    <td align="center">
      <a href="https://colab.research.google.com/github/Yang-star-source/ControlNet-In-Latent-Diffusion/blob/main/ControlNet_Unconditional_LDM_Inference.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
      </a>
    </td>
    <td align="center">
      <a href="https://colab.research.google.com/github/Yang-star-source/ControlNet-In-Latent-Diffusion/blob/main/ControlNet_T2I_LDM_Inference.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
      </a>
    </td>
  </tr>
</table>

## Dataset 
If you use this dataset in your research, please credit the authors

```bibtex
@inproceedings{choi2020starganv2,
  title={StarGAN v2: Diverse Image Synthesis for Multiple Domains},
  author={Yunjey Choi and Youngjung Uh and Jaejun Yoo and Jung-Woo Ha},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2020}
}
```

* **Dataset** -[Kaggle](https://www.kaggle.com/datasets/andrewmvd/animal-faces)

* **Processed data** -[Hugging Face](https://huggingface.co/datasets/ziyang06315/cats_images_dataset/tree/main)

## Reference
If you used the ideas from ControlNet in this project, please cite the original paper:

```bibtex
@inproceedings{zhang2023adding,
  title={Adding Conditional Control to Text-to-Image Diffusion Models},
  author={Zhang, Lvmin and Rao, Anyi and Agrawala, Maneesh},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={3836--3847},
  year={2023}
}
```

* **CLIP Embedding Documentation** -[Hugging Face](https://huggingface.co/docs/transformers/model_doc/clip)
* **OpenCV Edge Detection** -[Documentation](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html)
