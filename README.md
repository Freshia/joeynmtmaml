# &nbsp; ![Joey-NMT](joey-small.png) Joey NMT MAML
[![Build Status](https://travis-ci.com/joeynmt/joeynmt.svg?branch=master)](https://travis-ci.org/joeynmt/joeynmt)

## Goal and Purpose

This code builds on [Joey NMT](https://github.com/joeynmt/joeynmt) to introduce Model Agnostic Meta-Learning for Machine Translation.

:koala: Joey NMT framework is developed for educational purposes.

Check out the detailed [documentation](https://joeynmt.readthedocs.io) for Joey NMT and the [paper](https://arxiv.org/abs/1907.12484).

## Contributors
Joey NMT was initially developed and is maintained by [Jasmijn Bastings](https://github.com/bastings) (University of Amsterdam) and [Julia Kreutzer](https://juliakreutzer.github.io/) (Heidelberg University), now both at Google Research. [Mayumi Ohta](https://www.cl.uni-heidelberg.de/statnlpgroup/members/ohta/) at Heidelberg University is continuing the legacy.

## Joey NMT Features
Joey NMT implements the following features (aka the minimalist toolkit of NMT :wrench:):
- Recurrent Encoder-Decoder with GRUs or LSTMs
- Transformer Encoder-Decoder
- Attention Types: MLP, Dot, Multi-Head, Bilinear
- Word-, BPE- and character-based input handling
- BLEU, ChrF evaluation
- Beam search with length penalty and greedy decoding
- Customizable initialization
- Attention visualization
- Learning curve plotting

## Coding
In order to keep the code clean and readable, we make use of:
- Style checks: pylint with (mostly) PEP8 conventions, see `.pylintrc`.
- Typing: Every function has documented input types.
- Docstrings: Every function, class and module has docstrings describing their purpose and usage.
- Unittests: Every module has unit tests, defined in `test/unit/`.
Travis CI runs the tests and pylint on every push to ensure the repository stays clean.

## Usage


### Data Preparation

#### Parallel Data
For training a translation model, you need parallel data, i.e. a collection of source sentences and reference translations that are aligned sentence-by-sentence and stored in two files, 
such that each line in the reference file is the translation of the same line in the source file.

#### Pre-processing
Before training a model on it, parallel data is most commonly filtered by length ratio, tokenized and true- or lowercased.

The Moses toolkit provides a set of useful [scripts](https://github.com/moses-smt/mosesdecoder/tree/master/scripts) for this purpose.

In addition, you might want to build the NMT model not on the basis of words, but rather sub-words or characters (the `level` in JoeyNMT configurations).
Currently, JoeyNMT supports the byte-pair-encodings (BPE) format by [subword-nmt](https://github.com/rsennrich/subword-nmt) and [sentencepiece](https://github.com/google/sentencepiece).

### Configuration
Experiments are specified in configuration files, in simple [YAML](http://yaml.org/) format. You can find examples in the `configs` directory.
`small.yaml` contains a detailed explanation of configuration options.

Most importantly, the configuration contains the description of the model architecture (e.g. number of hidden units in the encoder RNN), 
paths to the training, development and test data, and the training hyperparameters (learning rate, validation frequency etc.).

## Naming
Joeys are [infant marsupials](https://en.wikipedia.org/wiki/Marsupial#Early_development). :koala:

