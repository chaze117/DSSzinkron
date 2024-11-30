import streamlit as st
from st_login_form import *
def Character(character:str,char_img:str,a1:str,a3:str,a2:str,id:int,h1='',h2='',h3='',szin_img='',osszes=0,done=0,mh=''):
    client = st.connection(name="supabase", type=SupabaseConnection)
    char = client.table('characters').select('*',count=None).eq('id',id)
    char = char.execute()
    uid = char.data[0]['assigned_user']
    username = ""
    img = ""
    if uid != None:
        user = client.table("users").select('username',count=None).eq('id',uid).execute()
        username = user.data[0]['username']
        if client.get_public_url("profilepics",st.session_state['username']) != None:
            img = client.get_public_url("profilepics",st.session_state['username'])
    check = ""
    if done == osszes : check="✔️"
    with st.expander(character +" - "+ str(done) +"/"+str(osszes) + " "+check):
        percent = done/osszes
        st.progress(percent,str(round(percent*100))+'%')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(char_img)
        with col2:
            st.audio(a1)
            st.audio(a2)
            st.audio(a3)
        with col3:
            if h1 != "": st.audio(h1)
            if h2 != "": st.audio(h2)
            if h3 != "": st.audio(h3)
        with col4:
            if img != "":
                st.image(img)
            else:
                if szin_img != '': st.image(szin_img)
                else: st.image('img/nia.jpg')
        if mh!='':
            st.markdown("<p style='marginTop:-35px; font-size:25px'>Magyar hangja: "+mh+"</p>",unsafe_allow_html=True)
        else:
            st.markdown("<p style='marginTop:-35px; font-size:25px'>Magyar hangja: "+username+"</p>",unsafe_allow_html=True)
st.markdown("""
            <style>
            .stAudio{
                height:30px;
                margin:10px 0 -15px -40px;
                }
            .stMainBlockContainer{
                max-width:60%}
            .stElementToolbar{
                visibility: hidden;}
            .stExpander p{
                font-size: 30px;
                text-align: center;
                
            }
            .stProgress p{
                font-size: 20px;
            }
            .stSidebar p{
                font-size: 16px;
            }
            </style>
            """,unsafe_allow_html=True)
charP = {
    'Alvina of the Darkroot Wood':0,
    'Anastacia of Astora':0,
    'Andre of Astora':0,
    'Big Hat Logan':0,
    'Crestfallen Merchant':0,
    'Crestfallen Warrior':0,
    'Crossbreed Priscilla':0,
    'Dark Sun Gwyndolin':0,
    'Darkstalker Kaathe':0,
    'Domhnall of Zena':0,
    'Dusk of Oolacile':0,
    'Eingyi':0,
    'Elizabeth':0,
    'Giant Blacksmith':0,
    'Griggs of Vinheim':0,
    'Gwynevere, Princess of Sunlight':33,
    'Hawkeye Gough':0,
    'Ingward':0,
    'Kingseeker Frampt':0,
    'Knight Lautrec of Carim':0,
    'Lady of the Darkling':0,
    'Laurentius of the Great Swamp':0,
    "Lord's Blade Ciaran":0,
    "Marvellous Chester":0,
    "Oscar Knight of Astora":0,
    "Oswald of Carim":0,
    "Patches":0,
    "Petrus of Thorolund":0,
    "Quelaag's sister":0,
    "Quelana of Izalith":0,
    "Rhea of Thorolund":0,
    "Rickert of Vinheim":0,
    "Shiva of the East":0,
    "Sieglinde of Catarina":0,
    "Siegmeyer of Catarina":0,
    "Snuggly the Crow":0,
    "Solaire of Astora":0,
    "Undead Merchant (Female)":0,
    "Undead Merchant (Male)":0,
    "Vamos":0,
    "Vince of Thorolund":0,
    }
sum = sum(charP.values())
ovP = sum/3012
st.progress(ovP,"Jelenlegi állapot " +str(round(ovP*100,1))+" %")
Character('Alvina of the Darkroot Wood','img/Alvina.png','sound/Alvina0.mp3','sound/Alvina1.mp3','sound/Alvina2.mp3',1,osszes=58,done=charP['Alvina of the Darkroot Wood'])
Character('Anastacia of Astora','img/Anastacia.png','sound/Anastacia1.mp3','sound/Anastacia2.mp3','sound/Anastacia3.mp3',2,osszes=20,done=charP['Anastacia of Astora'])
Character('Andre of Astora','img/Andre.png','sound/Andre0.mp3','sound/Andre1.mp3','sound/Andre2.mp3',3,osszes=106,done=charP['Andre of Astora'])
Character('Big Hat Logan','img/Logan.png','sound/Logan0.mp3','sound/Logan1.mp3','sound/Logan2.mp3',4,osszes=89,done=charP['Big Hat Logan'])
Character('Crestfallen Merchant', 'img/CMerchant.png','sound/CrestfallenMerchant1.mp3','sound/CrestfallenMerchant2.mp3','sound/CrestfallenMerchant3.mp3',5,osszes=51,done=charP['Crestfallen Merchant'])
Character('Crestfallen Warrior', 'img/Cwarrior.png','sound/CrestfallenWarrior0.mp3','sound/CrestfallenWarrior1.mp3','sound/CrestfallenWarrior2.mp3',6,osszes=146, done=charP['Crestfallen Warrior'])
Character('Crossbreed Priscilla', 'img/priscilla.png','sound/Priscilla0.mp3','sound/Priscilla1.mp3','sound/Priscilla2.mp3',7,osszes=15, done=charP['Crossbreed Priscilla'],mh='kyrande_foxfairy',szin_img='https://static-cdn.jtvnw.net/jtv_user_pictures/9e170390-1005-4143-8c89-6b4855131b6c-profile_image-150x150.png')
Character('Dark Sun Gwyndolin', 'img/Gwyndolin.png','sound/Gwyndolin0.mp3','sound/Gwyndolin1.mp3','sound/Gwyndolin2.mp3',8,osszes=35,done=charP['Dark Sun Gwyndolin'])
Character('Darkstalker Kaathe', 'img/Kaathe.png','sound/Kaathe0.mp3','sound/Kaathe1.mp3','sound/Kaathe2.mp3',9,osszes=105,done=charP['Darkstalker Kaathe'])
Character('Domhnall of Zena', 'img/Domhnall.png','sound/Domhnall0.mp3','sound/Domhnall1.mp3','sound/Domhnall2.mp3',10,osszes=52,done=charP['Domhnall of Zena'])
Character('Dusk of Oolacile', 'img/dusk.png','sound/Dusk0.mp3','sound/Dusk1.mp3','sound/Dusk2.mp3',11,osszes=73,done=charP['Dusk of Oolacile'])
Character('Eingyi', 'img/Eingyi.png','sound/Eingyi0.mp3','sound/Eingyi1.mp3','sound/Eingyi2.mp3',12,osszes=69,done=charP['Eingyi'])
Character('Elizabeth', 'img/Elizabeth.png','sound/Elizabeth0.mp3','sound/Elizabeth1.mp3','sound/Elizabeth2.mp3',13,osszes=67,done=charP['Elizabeth'])
Character('Giant Blacksmith', 'img/GiantBlacksmith.png','sound/GiantBlacksmith0.mp3','sound/GiantBlacksmith1.mp3','sound/GiantBlacksmith2.mp3',14,osszes=44,done=charP['Giant Blacksmith'])
Character('Griggs of Vinheim', 'img/Griggs.png','sound/Griggs0.mp3','sound/Griggs1.mp3','sound/Griggs2.mp3',15,osszes=141,done=charP['Griggs of Vinheim'])
Character('Gwynevere, Princess of Sunlight', 'img/Gwyn.png','sound/Gwyn0.mp3','sound/Gwyn1.mp3','sound/Gwyn2.mp3',16,osszes=33,done=charP['Gwynevere, Princess of Sunlight'],h1='sound/hun_Gwyn0.mp3',h2='sound/hun_Gwyn1.mp3',h3='sound/hun_Gwyn2.mp3',mh='kyrande_foxfairy',szin_img='https://static-cdn.jtvnw.net/jtv_user_pictures/9e170390-1005-4143-8c89-6b4855131b6c-profile_image-150x150.png')
Character('Hawkeye Gough', 'img/Hawkeye.png','sound/Hawkeye0.mp3','sound/Hawkeye1.mp3','sound/Hawkeye2.mp3',17,osszes=107,done=charP['Hawkeye Gough'])
Character('Ingward', 'img/Ingward.png','sound/Ingward1.mp3','sound/Ingward2.mp3','sound/Ingward3.mp3',18,osszes=73,done=charP['Ingward'])
Character('Kingseeker Frampt', 'img/Frampt.png','sound/Frampt0.mp3','sound/Frampt1.mp3','sound/Frampt2.mp3',19,osszes=88,done=charP['Kingseeker Frampt'])
Character('Knight Lautrec of Carim', 'img/Lautrec.png','sound/Lautrec0.mp3','sound/Lautrec1.mp3','sound/Lautrec2.mp3',20,osszes=81,done=charP['Knight Lautrec of Carim'])
Character('Lady of the Darkling', 'img/Darkling.png','sound/Darkling0.mp3','sound/Darkling1.mp3','sound/Darkling2.mp3',21,osszes=56,done=charP['Lady of the Darkling'])
Character('Laurentius of the Great Swamp', 'img/Laurentius.png','sound/Laurentius1.mp3','sound/Laurentius2.mp3','sound/Laurentius3.mp3',22,osszes=118,done=charP['Laurentius of the Great Swamp'])
Character("Lord's Blade Ciaran", 'img/Ciaran.png','sound/Ciaran0.mp3','sound/Ciaran1.mp3','sound/Ciaran2.mp3',23,osszes=29,done=charP["Lord's Blade Ciaran"])
Character("Marvellous Chester", 'img/Chester.png','sound/Chester0.mp3','sound/Chester1.mp3','sound/Chester2.mp3',24,osszes=74,done=charP['Marvellous Chester'])
Character("Oscar, Knight of Astora", 'img/Oscar.png','sound/Oscar0.mp3','sound/Oscar1.mp3','sound/Oscar2.mp3',25,osszes=36,done=charP['Oscar Knight of Astora'])
Character("Oswald of Carim", 'img/Oswald.png','sound/Oswald0.mp3','sound/Oswald1.mp3','sound/Oswald2.mp3',26,osszes=52,done=charP['Oswald of Carim'])
Character("Patches", 'img/Patches.png','sound/Patches0.mp3','sound/Patches1.mp3','sound/Patches2.mp3',27,osszes=179,done=charP['Patches'])
Character("Petrus of Thorolund", 'img/Petrus.png','sound/Petrus0.mp3','sound/Petrus1.mp3','sound/Petrus2.mp3',28,osszes=109,done=charP['Petrus of Thorolund'])
Character("Quelaag's sister", 'img/Quelaag.png','sound/Quelaag0.mp3','sound/Quelaag1.mp3','sound/Quelaag2.mp3',29,osszes=37,done=charP["Quelaag's sister"])
Character("Quelana of Izalith", 'img/Quelana.png','sound/Quelana0.mp3','sound/Quelana1.mp3','sound/Quelana2.mp3',30,osszes=73,done=charP['Quelana of Izalith'])
Character("Rhea of Thorolund", 'img/Rhea.png','sound/Rhea0.mp3','sound/Rhea1.mp3','sound/Rhea2.mp3',31,osszes=63,done=charP['Rhea of Thorolund'])
Character("Rickert of Vinheim", 'img/Rickert.png','sound/Rickert1.mp3','sound/Rickert2.mp3','sound/Rickert3.mp3',32,osszes=80,done=charP['Rickert of Vinheim'])
Character("Shiva of the East", 'img/Shiva.png','sound/Shiva0.mp3','sound/Shiva1.mp3','sound/Shiva2.mp3',33,osszes=46,done=charP['Shiva of the East'])
Character("Sieglinde of Catarina", 'img/Sieglinde.png','sound/Sieglinde0.mp3','sound/Sieglinde1.mp3','sound/Sieglinde2.mp3',33,osszes=41,done=charP['Sieglinde of Catarina'])
Character("Siegmeyer of Catarina", 'img/Siegmeyer.png','sound/Siegmeyer2.mp3','sound/Siegmeyer3.mp3','sound/Siegmeyer4.mp3',35,osszes=215,done=charP['Siegmeyer of Catarina'])
Character("Snuggly the Crow", 'img/Snuggly.png','sound/Snuggly0.mp3','sound/Snuggly1.mp3','sound/Snuggly2.mp3',36,osszes=13,done=charP['Snuggly the Crow'])
Character("Solaire of Astora", 'img/Solaire.png','sound/Solaire1.mp3','sound/Solaire2.mp3','sound/Solaire3.mp3',37,osszes=109,done=charP['Solaire of Astora'])
Character("Undead Merchant (Female)", 'img/UDMerchF.png','sound/UDMerchF0.mp3','sound/UDMerchF1.mp3','sound/UDMerchF2.mp3',38,osszes=80,done=charP['Undead Merchant (Female)'])
Character("Undead Merchant (Male)", 'img/UDMerchM.png','sound/UDMerchM0.mp3','sound/UDMerchM1.mp3','sound/UDMerchM2.mp3',39,osszes=72,done=charP['Undead Merchant (Male)'])
Character("Vamos", 'img/Vamos.png','sound/Vamos0.mp3','sound/Vamos1.mp3','sound/Vamos2.mp3',40,osszes=47,done=charP['Vamos'])
Character("Vince of Thorolund", 'img/Vince.png','sound/Vince0.mp3','sound/Vince1.mp3','sound/Vince3.mp3',41,osszes=30,done=charP['Vince of Thorolund'])

