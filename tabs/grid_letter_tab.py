# Third party imports
import streamlit as st

# Local imports
from utils.handle_grids import get_grids, read_grid
from utils.toolbox import display_generated_grids



def run():
    st.title("✨⛄ Decoding Letter-Grids ⛄✨")
    st.divider()
    for _ in range(2):
        st.write('')

    st.write('''
        Some puzzle answers come in the form of a two-dimensional grid of letters. 
        I've encountered 5 of these, although I suspect there might be more.
        Just for fun, I wrote some functions to help both decode and generate these letter grids.
        Hope you enjoy!
    ''')

    grids = get_grids()
    decode_tab, generate_tab, = st.tabs(['Decode Grid', 'Generate Grid'])


    with decode_tab:
        st.write('')

        grid_provided = st.session_state.get('grid_memory')

        if not grid_provided or not grid_provided.strip():
            st.write('Enter a 2D letter to decode (examples below):')
            st.text_area('Grid input:', key='grid_memory', label_visibility='collapsed')
            st.button('Decode grid')
            for reference, link, grid in grids['examples']:
                st.divider()
                st.text(f'{reference}  \n\n{grid}')
                st.caption(f'*([link to the puzzle]({link}))*')
            
        else:  
            st.text(f'The grid you provided: \n\n{grid_provided}')
            decoded = read_grid(grid_provided)

            if decoded:
                st.subheader(decoded)
                st.divider()
                st.button('Try a different one!', key='try_new_grid_input')

            else:
                st.error("""
                    :scream: Oops, something went wrong!  
                    :thinking_face: Perhaps there's an issue with the grid you provided...  
                    :crossed_fingers: Check if you copied it correctly and try re-entering it.  
                    :email: If the problem persists, drop me a message: mgtezak@gmail.com
                """) 
                st.button('Try again!')       

    with generate_tab:
        st.write('')

        letter_input = st.session_state.get('letter_input')
        if not letter_input or not letter_input.strip():
            st.write('Enter a message to project onto a 2D grid:')
            st.text_input('Letter input:', key='letter_input', label_visibility='collapsed')
            st.button('Generate grid')

        else:
            display_generated_grids(letter_input)
            st.write('')
            st.button('Try a different one!', key='try_new_letter_input')
