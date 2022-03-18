import numpy as np
import pandas as pd
import streamlit as st
import random
import math


view_result = False


def parse_members():
    senpai_list = []
    with open('senpai', 'rt') as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue
            senpai_list.append(line.strip())
        
    kohai_list = []
    with open('kohai', 'rt') as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue
            kohai_list.append(line.strip())

    return senpai_list, kohai_list


if __name__ == '__main__':
    senpai_list, kohai_list = parse_members()

    st.title('Duit pul-E distributor')

    st.markdown(f'''
    # Status
    - 선배: {len(senpai_list)} 명
    - 후배: {len(kohai_list)} 명
    ''')

    if st.button('Shuffle!'):
        st.balloons()

        random.shuffle(kohai_list)

        indices = np.arange(0, len(kohai_list))
        chunks = np.array_split(indices, len(senpai_list))

        random.shuffle(senpai_list)

        col1, col2 = st.columns(2)

        for i in range(len(senpai_list)):
            col = col1 if i % 2 == 0 else col2

            col.markdown('## {} 조 (선배: {})'.format(i + 1, senpai_list[i]))
            for kohai in chunks[i]:
                col.markdown('- {}'.format(kohai_list[kohai]))