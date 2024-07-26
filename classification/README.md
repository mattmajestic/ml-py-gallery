# Pokemon Classification

Building a classification model to value my Pokemon card collection.  


## Data

Data being loaded from `img/ dir` as PDF inputs of 9 Pokemon cards per sheet/file

## Preprocessing

1) Trim PDF of 9 cards to remove excess space
2) Cut up the page for each card so 9 cards per page
3) File will be generated in `output_images` of each card

## Use Pokemon TCG SDK/API

Create an API Key at https://pokemontcg.io/ and add `POKEMONTCG_IO_API_KEY=API_KEY_YOU_GET`

```
# Load .env file for Pokémon TCG API
from dotenv import load_dotenv
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

load_dotenv()

cards = Card.all()
cards
```