from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import StateForm, state_const_form
import requests

dict = {"Abhanpur": "53", "Ahiwara": "67", "Akaltara": "33", "Arang": "52", "Basna": "40", "Bastar": "85",
        "Beltara": "31", "Bijapur": "89", "Bilha": "29", "Durg City": "64", "AGAR": "166", "ALOTE": "223",
        "AMLA": "130", "ASHTA": "157", "ATER": "9", "BAGLI": "174", "BAIHAR": "108", "BANDA": "42", "BARGI": "96",
        "BETUL": "131", "Aizawl North-i": "10", "Aizawl North-ii": "11", "Aizawl North-iii": "12",
        "Aizawl East-i": "13", "Aizawl East-ii": "14", "Aizawl South-i": "18", "Aizawl South-ii": "19",
        "Aizawl South-iii": "20", "Aizawl West-i": "15", "Aizawl West-ii": "16", "Aizawl West-iii": "17",
        "Ahore": "141", "Amber": "47", "Anta": "193", "Asind": "177", "Bali": "120", "Bagru": "56", "Bansur": "63",
        "Bari": "78", "Bassi": "57", "Bhim": "173", "Alair": "97", "Armur": "11", "Boath": "8", "Chennur": "2",
        "Chevella": "53", "Dubbak": "41", "Gadwal": "79", "Jagtial": "21", "Jukkal": "13", "Mulug": "109"}

dict1={"Alwar Rural":"65" ,"Alwar Urban": "66" ,"Anupgarh": "6" ,"Asind": "177",
       "Aspur": "159" ,"Bagru": "120","Bali": "120","Banswara": "164","Baran-atru": "195","Bari sadri": "171",
       "Baseri":"77","Bayana":"76","Baytu":"136","Beawar":"168",
       "Ahiwara": "67", "Akaltara": "33", "Arang": "52", "Beltara": "31","Bilaigarh":"43","Bilha":"29",
       "Bindranawagarh":"55","Chitrakot":"87","Durg Gramin":"63","Gunderdehi":"61","Jaijaipur":"37",
       "Janjgirchampa":"34","Jashpur":"12","Kanker":"81","Kasdo":"l44",
       "Achampet":"82","Adilabad":"7","Alair":"97","Alampur":"80","Amberpet":"59","Andole":"36",
       "Armur":"11","Asifabad":"5","Aswaraopeta":"118","Bahadurpura":"69","Balkonda":"19","Banswada":"14",
       "Bellampalli": "3", "Bhadrachalam": "119", "Bhongir": "94",
        "AGAR":"166", "ALIRAJPUR": "191", "ALOTE": "223", "AMLA": "130", "ASHOK NAGAR": "32",
        "ATER": "9", "BADNAGAR": "218", "BADNAWAR": "202", "BAGLI": "174", "BAHORIBAND": "94", "BAIHAR": "108",
        "BAMORI": "28", "BANDA": "42", "BANDHAVGARH": "89", "BARGHAT": "114", "BASODA": "145", "BHAINSDEHI": "133",
       "Aizawl South-iii": "20", "Champhai South": "24", "Hachhek": "1", "Hrangturzo": "28","Lawngtlai East": "38",
       "Lawngtlai West": "37", "Lengteng": "21","Lunglei South": "33", "Palak": "40", "Serlui": "6", "Tawi": "9",
       "Thorang": "34"}

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def partywise(request):
    states={'s26':'Chattisgarh','s29':'Telangana','s12':'MadhyaPradesh','s16':'Mizoram','s20':'Rajasthan'}
    if request.method=="POST":
        form = StateForm(request.POST)
        state = form['dropdown']
        if(state.data=='Chattisgarh'):
            return render(request,'app/chattisgarh.html')
        elif(state.data=='MadhyaPradesh'):
            return render(request,'app/madhyapradesh.html')
        elif(state.data=='Rajasthan'):
            return render(request,'app/rajasthan.html')
        elif(state.data=='Telangana'):
            return render(request,'app/telangana.html')
        elif(state.data=='Mizoram'):
            return render(request, 'app/mizoram.html')
        else:
            return render(request,'app/party.html')
    else:
        return render(request,'app/party.html')

def trend(request):
    if request.method=="POST":
        form = state_const_form(request.POST)
        Name = form['dropdown'].data
        if(Name=='Chattisgarh'):
            return render(request,'app/chattisgarhtrend.html')
        elif(Name=='MadhyaPradesh'):
            return render(request,'app/madhyapradeshtrend.html')
        elif(Name=='Rajasthan'):
            return render(request,'app/rajasthantrend.html')
        elif(Name=='Telangana'):
            return render(request,'app/telanganatrend.html')
        elif(Name=='Mizoram'):
            return render(request, 'app/mizoramtrend.html')
        else:
            return render(request,'app/party.html')
        return render(request,'app/trend.html')
    else:
        return render(request,'app/trend.html')

def const(request):
    if request.method=="POST":
        form = state_const_form(request.POST)
        state = form['dropdown'].data
        const = form['dropdown1'].data
        if(state=='Chattisgarh'):
            if(const=='Abhanpur'):
                return render(request,'app/abhanpur.html')
            if(const=='Ahiwara'):
                return render(request,'app/ahiwara.html')
            if(const=='Akaltara'):
                return render(request,'app/akaltara.html')
            if(const=='Arang'):
                return render(request,'app/arang.html')
            if(const=='Basna'):
                return render(request,'app/basna.html')
            if(const=='Bastar'):
                return render(request,'app/bastar.html')
            if(const=='Bijapur'):
                return render(request,'app/belha.html')
            if(const=='Beltara'):
                return render(request,'app/beltara.html')
            if(const=='Bilha'):
                return render(request,'app/belha.html')
            if(const=='Durg City'):
                return render(request,'app/durg.html')
        if(state=='MadhyaPradesh'):
            if(const=='AGAR'):
                return render(request,'app/agar.html')
            if(const=='ALOTE'):
                return render(request,'app/alote.html')
            if(const=='AMLA'):
                return render(request,'app/amla.html')
            if(const=='ASHTA'):
                return render(request,'app/ashta.html')
            if(const=='ATER'):
                return render(request,'app/ater.html')
            if(const=='BAGLI'):
                return render(request,'app/bagli.html')
            if(const=='BAIHAR'):
                return render(request,'app/baihar.html')
            if(const=='BANDA'):
                return render(request,'app/banda.html')
            if(const=='BARGI'):
                return render(request,'app/bargi.html')
            if(const=='BETUL'):
                return render(request,'app/betul.html')
        if(state=='Mizoram'):
            if(const=='Aizawl North-i'):
                return render(request,'app/an1.html')
            if(const=='Aizawl North-ii'):
                return render(request,'app/an2.html')
            if(const=='Aizawl North-iii'):
                return render(request,'app/an3.html')
            if(const=='Aizawl East-i'):
                return render(request,'app/ae1.html')
            if(const=='Aizawl East-ii'):
                return render(request,'app/ae2.html')
            if(const=='Aizawl South-i'):
                return render(request,'app/as1.html')
            if(const=='Aizawl South-ii'):
                return render(request,'app/as2.html')
            if(const=='Aizawl South-iii'):
                return render(request,'app/as3.html')
            if(const=='Aizawl West-i'):
                return render(request,'app/aw1.html')
            if(const=='Aizawl West-ii'):
                return render(request,'app/aw2.html')
            if(const=='Aizawl West-iii'):
                return render(request,'app/aw3.html')
        if(state=='Rajasthan'):
            if(const=='Ahore'):
                return render(request,'app/ahore.html')
            if(const=='Anter'):
                return render(request,'app/anter.html')
            if(const=='Amber'):
                return render(request,'app/amber.html')
            if(const=='Anta'):
                return render(request,'app/anta.html')
            if(const=='Asind'):
                return render(request,'app/asind.html')
            if(const=='Bali'):
                return render(request,'app/bali.html')
            if(const=='Bagru'):
                return render(request,'app/bagru.html')
            if(const=='Bansur'):
                return render(request,'app/bansur.html')
            if(const=='Bari'):
                return render(request,'app/bari.html')
            if(const=='Bassi'):
                return render(request,'app/bassi.html')
            if(const=='Bhim'):
                return render(request,'app/bhim.html')
        if(state=='Telangana'):
            if(const=='Gadwal'):
                return render(request,'app/gadwal.html')
            if(const=='Jagtial'):
                return render(request,'app/jagtial.html')
            if(const=='Mulug'):
                return render(request,'app/mulug.html')
            if(const=='Jukkal'):
                return render(request,'app/jukkal.html')
            if(const=='Aliar'):
                return render(request,'app/aliar.html')
            if(const=='Armur'):
                return render(request,'app/armur.html')
            if(const=='Boath'):
                return render(request,'app/boath.html')
            if(const=='Chennur'):
                return render(request,'app/chennur.html')
            if(const=='Chevella'):
                return render(request,'app/chevella.html')
        return render(request,'app/constituency.html')
    else:
        return render(request,'app/const.html')
