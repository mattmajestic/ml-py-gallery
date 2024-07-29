# Pokemon Classification

Building a classification model to value my Pokemon card collection.  

## App/Frontend UI

[Visit App](https://pokemon-card-value-calculator.onrender.com/)

This is a Streamlit application running on `render.com` & `DockerHub`.

[![Docker Image](https://img.shields.io/docker/v/mattmajestic/pokemon-card-value-calculator?color=blue&label=mattmajestic/pokemon-card-value-calculator&logo=docker&logoColor=white&style=for-the-badge)](https://hub.docker.com/r/mattmajestic/pokemon-card-value-calculator)

## Data

Data being loaded from `img/ dir` as PDF inputs of 9 Pokemon cards per sheet/file

## Preprocessing

1) Trim PDF of 9 cards to remove excess space
2) Cut up the page for each card so 9 cards per page
3) File will be generated in `output_images` of each card

## Use Pokemon TCG SDK/API

Create an API Key at https://pokemontcg.io/ and add `POKEMONTCG_IO_API_KEY=API_KEY_YOU_GET`

