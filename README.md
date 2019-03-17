# Rasa_bot
Para ser testeado en C9

Instalación:

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

chmod a+x Miniconda3-latest-Linux-x86_64.sh

./Miniconda3-latest-Linux-x86_64.sh

conda create -n rasa python=3.6

conda activate rasa 

conda install -c conda-forge tensorflow

git clone https://github.com/sandroormeno/Rasa_bot.git

sudo pip install -r requerimientos.txt

sudo python -m spacy download es
