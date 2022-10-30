import hvplot.pandas
import panel as pn
import holoviews as hv
import sqlite3
import pandas as pd
import json

# Import dashboard subclasses and dependencies
hv.extension('bokeh')
pn.extension('tabulator')
PALETTE = ["#ff6f69", "#ffcc5c", "#88d8b0", ]

# Create db connection.
cnx = sqlite3.connect('pokemons.db')

# Get all Pokemon data
df = pd.read_sql_query('SELECT * FROM pokemons', cnx)
df['id'] = df['id'].astype(str)

#Sanitize
for i, row in df.iterrows():
    #Sanitize game_indices to comma seperated string
    game_indices = json.loads(df['game_indices'][i])
    game_indices = ','.join([gi['name'] for gi in game_indices])
    df.at[i,'game_indices'] = game_indices

    #Sanitize slot_types to comma seperated string
    slot_types = json.loads(df['slot_types'][i])
    slot_types = ','.join([f'slot{st["slot"]}:{st["name"]}' for st in slot_types])
    df.at[i,'slot_types'] = slot_types

# Make DataFrame Pipeline Interactive
idf = df.interactive()

# Create data foundation for dashboard
all_pokemon = (
    idf
)

#Construct UI
all_pokemons_table = all_pokemon.pipe(pn.widgets.Tabulator, pagination='remote', page_size=10, sizing_mode='stretch_width')

#Layout using Template
template = pn.template.FastListTemplate(
    title='Pokemon Dashboard', 
    main=[all_pokemons_table.panel()],
    accent_base_color="#c92014",
    header_background="#c92014",
)

#Display dashboard
template.show()