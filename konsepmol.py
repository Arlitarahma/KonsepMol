import streamlit as st

st.title(':blue[Konsep Mol]')
tab1,tab2,tab3=st.tabs(['Pengenalan','Materi Konsep Mol','Perhitungan'])

with tab1:
    st.subheader('Oleh Kelompok 8')
    st.subheader('Anggota:')
    
    st.write('1. Allyssa Qutratu''ain            (2219031)')

    st.write('2. Arlita Rahma Herdiyana          (2219038)')

    st.write('3. Nadya Syaharani Qodriah Darajat (2219122)')

    st.write('4. Nurazizah                       (2219138)')

    st.write('5. Zahratul Hayati Amalia          (2219185)')
    
with tab2:
    st.subheader('Pengertian Mol dan Konsep Mol')
    st.write('Mol merupakan jumlah tertentu untuk menyatakan banyaknya suatu zat yang berukuran kecil. Konsep mol merupakan perhitungan kuantitas yang berkaitan dengan jumlha atom, molekul, ion, atau electron dalam suatu zat. Menurut satuan Sistem Internasional (SI), satuan dasar dari kuantitas ini disebut mol. "Satu mol menyatakan jumlah zat suatu sistem yang mengandung sejumlah besaran elementer (atom, molekul, dan ion) yang setara dengan banyaknya atom yang terdapat dalam 12 gram tepat isotop Karbon 12 (C-12)"')
    st.subheader('Volume Mol')
    st.write('Volume molar adalah penentuan mol suatu zat yang berfasa gas')
    st.write(':green[Hubungan Mol dengan Volume Gas]')
    st.write('Pada suhu dan tekanan tertentu akan selalu berlaku bahwa semakin besar volume suatu gas maka jumlah partikel dalam gas tersebut juga akan semakin banyak yang artinya jumlah mol gas akan semakin besar. Hubungan volume gas dengan mol secara umum ditunjukkan oleh suatu persamaan yang biasa dikenal sebagai persamaan gas ideal. Volume gas sangat dipengaruhi oleh tekanan (P) dan temperatur (T).')
    st.write(':green[Persamaan Gas Ideal]')
    st.latex(r'PV=nRT')
    st.latex(r'Jumlah\space Mol\space (n)= \dfrac {PV} {RT}')
    st.write('''Keterangan:

P = tekanan (atm);

V = volume (liter);

n = jumlah mol;

R = konstanta gas ideal (0,082 L.atm/mol.K);

T = suhu gas (K)

a. Keadaan STP ((Standard Temperature Pressure)
   
Pada keadaan STP (Standard Temperature Pressure), yaitu pada suhu 0 ⁰C dan tekanan 1 atmosfer, maka volume satu mol gas sembarang adalah 22,4 liter.''')
    st.latex(r'Jumlah\space Mol\space (n) = \dfrac {Volume\space STP\space (L)} {22,4\space (L)}')
    st.write('''b.	Keadaan RTP (Room Temperature and Pressure) 
    
Pada keadaan RTP  (Room Temperature and Pressure), yaitu pada suhu ruangan dan tekanan 1 atmosfer, maka volume satu mol gas sembarang adalah 24 liter.''')
    st.latex(r'Jumlah\space Mol\space (n)= \dfrac {Volume\space RTP\space (L)} {24\space (L)}')
    st.subheader('Massa Molar')
    st.write('''Massa molar adalah massa 1 mol zat sebanyak Ar unsurnya atau Mr senyawanya yang dinyatakan dalam (gram/mol).''')
    st.write(':green[Hubungan Mol dengan Massa Suatu Zat]')
    st.write('''Satu mol zat apapun menunjukkan jumlah partikel yang sama, tetapi kalau  diukur massanya maka 1 mol zat yang berbeda umumnya memiliki massa yang berbeda.''') 
    st.latex(r'Jumlah\space Mol\space (n)= \dfrac {Massa\space (g)} {Ar/Mr}')
    st.subheader('Jumlah Partikel')
    st.write('Jumlah partikel dalam konsep mol merujuk pada jumlah partikel dalam satu mol suatu zat.')
    st.write(':green[Hubungan Mol dengan Jumlah Partikel]')
    st.write('Satu mol zat apapun akan memiliki jumlah partikel yang sama, yaitu sebesar 6,02x10²³ partikel.')
    st.latex(r'Jumlah\space Mol\space (n)= \dfrac {Jumlah\space Partikel} {6,02 ×10^{23}}')
    st.subheader('Molaritas')
    st.write('Molaritas merupakan salah satu ukuran konsentrasi larutan. Molaritas suatu larutan menyatakan jumlah mol suatu zat per liter larutan.') 
    st.write(':green[Hubungan Mol dengan Molaritas]')
    st.write('Banyaknya zat yang terdapat dalam suatu larutan dapat diketahui dengan menggunakan konsentrasi larutan yang dinyatakan dalam molaritas (M). Molaritas menyatakan banyaknya mol zat dalam 1 L larutan.')
    st.latex(r'Jumlah\space Mol\space (n)= {Molaritas\space (M) \cdot Volume\space (L)} ')
    st.image('https://i.postimg.cc/hGzq5k30/Screenshot-2023-05-05-161344.png',width=None)

with tab3:
    hitung=st.selectbox('Hubungan Mol dengan', ['Volume Gas','Massa','Jumlah Partikel','Molaritas'])
    if hitung=='Volume Gas':
        dihitung1=st.selectbox('Yang Akan Dihitung',['Mol','Volume'])
        if dihitung1=='Mol':
            keadaanmol=st.radio('Keadaan',['Keadaan Standar (STP)','Keadaan Pada Suhu Kamar (RTP)'])
            if keadaanmol=='Keadaan Standar (STP)':
                vmol1=st.number_input('Masukkan Volume (L)')
                molstp=vmol1/22.4
                if st.button('Hitung'):
                    st.write(f'Nilai Mol adalah {molstp} n')
            elif keadaanmol=='Keadaan Pada Suhu Kamar (RTP)':
                vmol2=st.number_input('Masukkan Volume (L)')
                molrtp=vmol2/24
                if st.button('Hitung'):
                    st.write(f'Nilai Mol adalah {molrtp} n')
        elif dihitung1=='Volume':
            keadaanvolume=st.radio('Keadaan',['Keadaan Standar (STP)','Keadaan Pada Suhu Kamar (RTP)'])
            if keadaanvolume=='Keadaan Standar (STP)':
                nstp=st.number_input('Masukkan Mol (n)')
                vstp=nstp*22.4
                if st.button('Hitung'):
                    st.write(f'Nilai Volume adalah {vstp} L')
            elif keadaanvolume=='Keadaan Pada Suhu Kamar (RTP)':
                nrtp=st.number_input('Masukkan Mol (n)')
                vrtp=nrtp*24
                if st.button('Hitung'):
                    st.write(f'Nilai Mol adalah {vrtp} L')
            
    elif hitung=='Massa':
        dihitung2=st.selectbox('Yang Akan Dihitung',['Mol','Massa'])
        if dihitung2=='Mol':
            m=st.number_input('Masukkan Massa (g)')
            armr1=st.number_input('Masukkan Ar/Mr')
            molmassa=m/armr1
            if st.button('Hitung'):
                    st.write(f'Nilai Mol adalah {molmassa} n')
        elif dihitung2=='Massa':
            nmassa=st.number_input('Masukkan Massa (g)')
            armr2=st.number_input('Masukkan Ar/Mr')
            massa=nmassa*armr2
            if st.button('Hitung'):
                    st.write(f'Nilai Massa adalah {nm} g')
                    
    elif hitung=='Jumlah Partikel':
        dihitung3=st.selectbox('Yang Akan Dihitung',['Mol','Jumlah Partikel'])
        if dihitung3=='Mol':
            x=st.number_input('Masukkan x')
            moljp=x/(6.02*10**23)
            if st.button('Hitung'):
                    st.write(f'Nilai Mol adalah {moljp} n')
        elif dihitung3=='Jumlah Partikel':
            njp=st.number_input('Masukkan Mol (n)')
            jp=njp*(6.02*10**23)
            if st.button('Hitung'):
                    st.write(f'Jumlah Partikel adalah {jp} x')
                
    elif hitung=='Molaritas':
        dihitung4=st.selectbox('Yang Akan Dihitung',['Mol','Molaritas'])
        if dihitung4=='Mol':
            molaritasmol=st.number_input('Masukkan Molaritas')
            vmolaritas=st.number_input('Masukkan Volume')
            nM=molaritasmol*vmolaritas
            if st.button('Hitung'):
                st.write(f'Nilai Mol adalah {nM} n')
        elif dihitung4=='Molaritas':
            nmolaritas=st.number_input('Masukkan Mol (n)')
            volumemolaritas=st.number_input('Masukkan Volume (L)')
            molaritas=nmolaritas/volumemolaritas
            if st.button('Hitung'):
                st.write(f'Nilai Molaritas adalah {nM} M')
            
            
        
        