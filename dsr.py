import streamlit as st
from st_login_form import *

client = st.connection(name="supabase", type=SupabaseConnection)
characters = client.table('characters').select('*',count=None).order('id')
characters = characters.execute()
users = client.table("users").select('*',count=None)
users = users.execute()
Done = {}
for c in characters.data:
    Done[c['name']] = c['done']
def searchUser(data,id):
    for item in data:
        if item['id'] == id:
            return item['username']
def Character(character:str,char_img:str,a1:str,a3:str,a2:str,id:int,h1='',h2='',h3='',szin_img='',osszes=0,mh=''):
    done = Done[character.replace("'",'')]
    uid = characters.data[id-1]['assigned_user']
    username = ""
    img = ""
    if uid != None:
        username = searchUser(users.data,uid)
        if client.get_public_url("profilepics",username) != None:
            img = client.get_public_url("profilepics",username)
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
            if username != "":
                st.markdown("<p style='marginTop:-35px; font-size:25px'>Magyar hangja: "+username+"</p>",unsafe_allow_html=True)
st.markdown("""
            <style>
            .stAudio{
                height:30px;
                }
            .stMainBlockContainer{
                max-width:60%}
            .stElementToolbar{
                visibility: hidden;}
            .stExpander p{
                font-size: 30px;
            }
            .stProgress p{
                font-size: 25px;
                text-align: center;
            }
            .stSidebar p{
                font-size: 16px;
            }
            .stMarkdown p{
                text-align: center;
            }
            </style>
            """,
            unsafe_allow_html=True)


sum = sum(Done.values())
ovP = sum/3012

st.image('dsr.png')

st.progress(ovP,"Jelenlegi állapot " +str(round(ovP*100,1))+" %  - "+str(sum)+"/3012" )

Character('Alvina of the Darkroot Wood','img/Alvina.png','sound/Alvina0.mp3','sound/Alvina1.mp3','sound/Alvina2.mp3',1,osszes=58)
Character('Anastacia of Astora','img/Anastacia.png','sound/Anastacia1.mp3','sound/Anastacia2.mp3','sound/Anastacia3.mp3',2,osszes=20)
Character('Andre of Astora','img/Andre.png','sound/Andre0.mp3','sound/Andre1.mp3','sound/Andre2.mp3',3,osszes=106,h1='https://txwxfzohqokyqsdhbadt.supabase.co/storage/v1/object/public/Andre%20of%20Astora/hun/v029000000.wav.wav',h2='https://txwxfzohqokyqsdhbadt.supabase.co/storage/v1/object/public/Andre%20of%20Astora/hun/v029000004.wav.wav',h3='https://txwxfzohqokyqsdhbadt.supabase.co/storage/v1/object/public/Andre%20of%20Astora/hun/v029000005.wav.wav')
Character('Big Hat Logan','img/Logan.png','sound/Logan0.mp3','sound/Logan1.mp3','sound/Logan2.mp3',4,osszes=89)
Character('Crestfallen Merchant', 'img/CMerchant.png','sound/CrestfallenMerchant1.mp3','sound/CrestfallenMerchant2.mp3','sound/CrestfallenMerchant3.mp3',5,osszes=51)
Character('Crestfallen Warrior', 'img/Cwarrior.png','sound/CrestfallenWarrior0.mp3','sound/CrestfallenWarrior1.mp3','sound/CrestfallenWarrior2.mp3',6,osszes=146, )
Character('Crossbreed Priscilla', 'img/priscilla.png','sound/Priscilla0.mp3','sound/Priscilla1.mp3','sound/Priscilla2.mp3',7,osszes=15,mh='kyrande_foxfairy',szin_img='https://static-cdn.jtvnw.net/jtv_user_pictures/9e170390-1005-4143-8c89-6b4855131b6c-profile_image-150x150.png')
Character('Dark Sun Gwyndolin', 'img/Gwyndolin.png','sound/Gwyndolin0.mp3','sound/Gwyndolin1.mp3','sound/Gwyndolin2.mp3',8,osszes=35)
Character('Darkstalker Kaathe', 'img/Kaathe.png','sound/Kaathe0.mp3','sound/Kaathe1.mp3','sound/Kaathe2.mp3',9,osszes=105)
Character('Domhnall of Zena', 'img/Domhnall.png','sound/Domhnall0.mp3','sound/Domhnall1.mp3','sound/Domhnall2.mp3',10,osszes=52)
Character('Dusk of Oolacile', 'img/dusk.png','sound/Dusk0.mp3','sound/Dusk1.mp3','sound/Dusk2.mp3',11,osszes=73)
Character('Eingyi', 'img/Eingyi.png','sound/Eingyi0.mp3','sound/Eingyi1.mp3','sound/Eingyi2.mp3',12,osszes=69)
Character('Elizabeth', 'img/Elizabeth.png','sound/Elizabeth0.mp3','sound/Elizabeth1.mp3','sound/Elizabeth2.mp3',13,osszes=67)
Character('Giant Blacksmith', 'img/GiantBlacksmith.png','sound/GiantBlacksmith0.mp3','sound/GiantBlacksmith1.mp3','sound/GiantBlacksmith2.mp3',14,osszes=44)
Character('Griggs of Vinheim', 'img/Griggs.png','sound/Griggs0.mp3','sound/Griggs1.mp3','sound/Griggs2.mp3',15,osszes=141)
Character('Gwynevere, Princess of Sunlight', 'img/Gwyn.png','sound/Gwyn0.mp3','sound/Gwyn1.mp3','sound/Gwyn2.mp3',16,osszes=33,h1='sound/hun_Gwyn0.mp3',h2='sound/hun_Gwyn1.mp3',h3='sound/hun_Gwyn2.mp3',mh='kyrande_foxfairy',szin_img='https://static-cdn.jtvnw.net/jtv_user_pictures/9e170390-1005-4143-8c89-6b4855131b6c-profile_image-150x150.png')
Character('Hawkeye Gough', 'img/Hawkeye.png','sound/Hawkeye0.mp3','sound/Hawkeye1.mp3','sound/Hawkeye2.mp3',17,osszes=107)
Character('Ingward', 'img/Ingward.png','sound/Ingward1.mp3','sound/Ingward2.mp3','sound/Ingward3.mp3',18,osszes=73)
Character('Kingseeker Frampt', 'img/Frampt.png','sound/Frampt0.mp3','sound/Frampt1.mp3','sound/Frampt2.mp3',19,osszes=88)
Character('Knight Lautrec of Carim', 'img/Lautrec.png','sound/Lautrec0.mp3','sound/Lautrec1.mp3','sound/Lautrec2.mp3',20,osszes=81)
Character('Lady of the Darkling', 'img/Darkling.png','sound/Darkling0.mp3','sound/Darkling1.mp3','sound/Darkling2.mp3',21,osszes=56)
Character('Laurentius of the Great Swamp', 'img/Laurentius.png','sound/Laurentius1.mp3','sound/Laurentius2.mp3','sound/Laurentius3.mp3',22,osszes=118)
Character("Lord's Blade Ciaran", 'img/Ciaran.png','sound/Ciaran0.mp3','sound/Ciaran1.mp3','sound/Ciaran2.mp3',23,osszes=29)
Character("Marvellous Chester", 'img/Chester.png','sound/Chester0.mp3','sound/Chester1.mp3','sound/Chester2.mp3',24,osszes=74)
Character("Oscar, Knight of Astora", 'img/Oscar.png','sound/Oscar0.mp3','sound/Oscar1.mp3','sound/Oscar2.mp3',25,osszes=36)
Character("Oswald of Carim", 'img/Oswald.png','sound/Oswald0.mp3','sound/Oswald1.mp3','sound/Oswald2.mp3',26,osszes=52)
Character("Patches", 'img/Patches.png','sound/Patches0.mp3','sound/Patches1.mp3','sound/Patches2.mp3',27,osszes=179)
Character("Petrus of Thorolund", 'img/Petrus.png','sound/Petrus0.mp3','sound/Petrus1.mp3','sound/Petrus2.mp3',28,osszes=109)
Character("Quelaag's sister", 'img/Quelaag.png','sound/Quelaag0.mp3','sound/Quelaag1.mp3','sound/Quelaag2.mp3',29,osszes=37)
Character("Quelana of Izalith", 'img/Quelana.png','sound/Quelana0.mp3','sound/Quelana1.mp3','sound/Quelana2.mp3',30,osszes=73)
Character("Rhea of Thorolund", 'img/Rhea.png','sound/Rhea0.mp3','sound/Rhea1.mp3','sound/Rhea2.mp3',31,osszes=63)
Character("Rickert of Vinheim", 'img/Rickert.png','sound/Rickert1.mp3','sound/Rickert2.mp3','sound/Rickert3.mp3',32,osszes=80)
Character("Shiva of the East", 'img/Shiva.png','sound/Shiva0.mp3','sound/Shiva1.mp3','sound/Shiva2.mp3',33,osszes=46)
Character("Sieglinde of Catarina", 'img/Sieglinde.png','sound/Sieglinde0.mp3','sound/Sieglinde1.mp3','sound/Sieglinde2.mp3',33,osszes=41)
Character("Siegmeyer of Catarina", 'img/Siegmeyer.png','sound/Siegmeyer2.mp3','sound/Siegmeyer3.mp3','sound/Siegmeyer4.mp3',35,osszes=215)
Character("Snuggly the Crow", 'img/Snuggly.png','sound/Snuggly0.mp3','sound/Snuggly1.mp3','sound/Snuggly2.mp3',36,osszes=13)
Character("Solaire of Astora", 'img/Solaire.png','sound/Solaire1.mp3','sound/Solaire2.mp3','sound/Solaire3.mp3',37,osszes=109)
Character("Undead Merchant (Female)", 'img/UDMerchF.png','sound/UDMerchF0.mp3','sound/UDMerchF1.mp3','sound/UDMerchF2.mp3',38,osszes=80)
Character("Undead Merchant (Male)", 'img/UDMerchM.png','sound/UDMerchM0.mp3','sound/UDMerchM1.mp3','sound/UDMerchM2.mp3',39,osszes=72)
Character("Vamos", 'img/Vamos.png','sound/Vamos0.mp3','sound/Vamos1.mp3','sound/Vamos2.mp3',40,osszes=47)
Character("Vince of Thorolund", 'img/Vince.png','sound/Vince0.mp3','sound/Vince1.mp3','sound/Vince3.mp3',41,osszes=30)

