
READ-ME: 
---

# Guide d'Utilisation du Modèle de Traduction (Marian MT)

## Introduction

Ce guide vous expliquera comment utiliser le modèle de traduction Marian MT pour traduire des textes de l'anglais vers le français. Le modèle Marian MT est un modèle de traitement automatique du langage naturel (NLP) pré-entraîné qui peut être utilisé pour des tâches de traduction.

## Prérequis

Avant de commencer à utiliser le modèle Marian MT, assurez-vous d'avoir installé les bibliothèques Python requises. Vous pouvez les installer à l'aide de `pip` comme suit :


pip install transformers sentencepiece
pip install torch
pip install sacrebleu


## Utilisation du Modèle de Traduction

### Installation et Importation

Tout d'abord, installez les bibliothèques nécessaires et importez les modules requis dans votre script Python ou Jupyter Notebook :

```python
!pip install transformers[sentencepiece]
!pip install torch
!pip install sacrebleu
!pip install sacremoses
from transformers import MarianTokenizer, MarianMTModel
```

### Chargement du Modèle

Ensuite, chargez le modèle Marian MT pour la traduction de l'anglais vers le français :


model_name = "yasmineelabbar/marian-finetuned-kde4-en-to-fr-accelerate"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
```

### Traduction de Texte

Maintenant que le modèle est chargé, vous pouvez l'utiliser pour traduire du texte. Voici comment traduire un texte en utilisant le modèle :

# Texte en anglais que vous souhaitez traduire
texte_en_anglais = "Hello, how are you?"

# Tokenisation du texte d'entrée
inputs = tokenizer(texte_en_anglais, return_tensors="pt")

# Traduction du texte
translation_ids = model.generate(**inputs)

# Décodage de la traduction en français
texte_traduit = tokenizer.batch_decode(translation_ids, skip_special_tokens=True)


`texte_traduit` contiendra la traduction en français du texte d'entrée.

## Conclusion

Félicitations ! Vous savez maintenant comment utiliser le modèle Marian MT pour traduire des textes de l'anglais vers le français. N'hésitez pas à explorer davantage les fonctionnalités du modèle pour répondre à vos besoins spécifiques de traduction.

Pour plus d'informations sur les fonctionnalités avancées du modèle Marian MT, consultez la documentation officielle de Hugging Face Transformers.

--- 

