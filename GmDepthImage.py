#!/usr/bin/python3
import simplejson
import urllib
from PIL import Image
from PIL import PngImagePlugin
import ast

ELEVATION_BASE_URL = 'http://maps.google.com/maps/api/elevation/json'

RESPONSE_CACHE = "{'status': 'OK', 'results': [{'resolution': 610.8129272460938, 'elevation': 4303.2822265625, 'location': {'lat': 36.578581, 'lng': -118.291994}}, {'resolution': 610.8129272460938, 'elevation': 1677.936157226562, 'location': {'lat': 36.57870997996317, 'lng': -118.1587980423636}}, {'resolution': 610.8129272460938, 'elevation': 1116.869140625, 'location': {'lat': 36.57869077991322, 'lng': -118.0256018953414}}, {'resolution': 610.8129272460938, 'elevation': 2019.27587890625, 'location': {'lat': 36.57862864887367, 'lng': -117.8924060231431}}, {'resolution': 610.8129272460938, 'elevation': 1677.286499023438, 'location': {'lat': 36.57871922883434, 'lng': -117.7592099673502}}, {'resolution': 610.8129272460938, 'elevation': 1031.548583984375, 'location': {'lat': 36.57866162869643, 'lng': -117.6260138546624}}, {'resolution': 610.8129272460938, 'elevation': 1953.715087890625, 'location': {'lat': 36.57866634661902, 'lng': -117.4928180081312}}, {'resolution': 610.8129272460938, 'elevation': 1165.501586914062, 'location': {'lat': 36.57871852652099, 'lng': -117.359621888516}}, {'resolution': 610.8129272460938, 'elevation': 164.2804260253906, 'location': {'lat': 36.57862252633086, 'lng': -117.2264258444969}}, {'resolution': 610.8129272460938, 'elevation': 595.4700317382812, 'location': {'lat': 36.5786940932127, 'lng': -117.0932299638618}}, {'resolution': 610.8129272460938, 'elevation': -72.34255981445312, 'location': {'lat': 36.57870787302357, 'lng': -116.9600338147585}}, {'resolution': 610.8129272460938, 'elevation': 216.4579772949219, 'location': {'lat': 36.5783289876653, 'lng': -116.8365720101352}}, {'resolution': 610.8129272460938, 'elevation': -60.69433975219727, 'location': {'lat': 36.57136292764485, 'lng': -116.9694787499759}}, {'resolution': 610.8129272460938, 'elevation': 724.23486328125, 'location': {'lat': 36.56424936898235, 'lng': -117.1023612619589}}, {'resolution': 305.4064636230469, 'elevation': 283.84130859375, 'location': {'lat': 36.5569883771029, 'lng': -117.2352190495447}}, {'resolution': 305.4064636230469, 'elevation': 1333.569458007812, 'location': {'lat': 36.54958001875338, 'lng': -117.3680516170972}}, {'resolution': 305.4064636230469, 'elevation': 2170.738525390625, 'location': {'lat': 36.54202436199969, 'lng': -117.5008584699014}}, {'resolution': 305.4064636230469, 'elevation': 1906.69873046875, 'location': {'lat': 36.53432147622409, 'lng': -117.6336391141807}}, {'resolution': 305.4064636230469, 'elevation': 2395.684814453125, 'location': {'lat': 36.52647143212231, 'lng': -117.7663930571143}}, {'resolution': 305.4064636230469, 'elevation': 1124.027099609375, 'location': {'lat': 36.51847430170081, 'lng': -117.8991198068538}}, {'resolution': 305.4064636230469, 'elevation': 1103.478881835938, 'location': {'lat': 36.5103301582738, 'lng': -118.0318188725411}}, {'resolution': 610.8129272460938, 'elevation': 3370.533203125, 'location': {'lat': 36.50203907646035, 'lng': -118.1644897643248}}, {'resolution': 610.8129272460938, 'elevation': 3209.815185546875, 'location': {'lat': 36.49393849035912, 'lng': -118.2868396708355}}, {'resolution': 610.8129272460938, 'elevation': 3227.81005859375, 'location': {'lat': 36.49406157154703, 'lng': -118.1537894245954}}, {'resolution': 305.4064636230469, 'elevation': 1095.341064453125, 'location': {'lat': 36.49403692967661, 'lng': -118.0207390092426}}, {'resolution': 305.4064636230469, 'elevation': 1099.624877929688, 'location': {'lat': 36.49398408976491, 'lng': -117.8876888717849}}, {'resolution': 305.4064636230469, 'elevation': 2095.13671875, 'location': {'lat': 36.49406933283021, 'lng': -117.7546385338745}}, {'resolution': 305.4064636230469, 'elevation': 1652.720825195312, 'location': {'lat': 36.49400685276574, 'lng': -117.6215881568586}}, {'resolution': 305.4064636230469, 'elevation': 1205.325073242188, 'location': {'lat': 36.49401999723963, 'lng': -117.4885380368683}}, {'resolution': 305.4064636230469, 'elevation': 1416.332763671875, 'location': {'lat': 36.49406740213085, 'lng': -117.3554876405879}}, {'resolution': 305.4064636230469, 'elevation': 681.501220703125, 'location': {'lat': 36.49396708391006, 'lng': -117.2224373352093}}, {'resolution': 305.4064636230469, 'elevation': 1463.164306640625, 'location': {'lat': 36.4940462127616, 'lng': -117.0893871746153}}, {'resolution': 305.4064636230469, 'elevation': -79.59001159667969, 'location': {'lat': 36.49405577945009, 'lng': -116.9563367532652}}, {'resolution': 305.4064636230469, 'elevation': 150.1665191650391, 'location': {'lat': 36.49349487074515, 'lng': -116.840115972322}}, {'resolution': 305.4064636230469, 'elevation': -38.45621871948242, 'location': {'lat': 36.48653187553916, 'lng': -116.9728772566982}}, {'resolution': 305.4064636230469, 'elevation': 1582.809692382812, 'location': {'lat': 36.47942183696995, 'lng': -117.1056144258078}}, {'resolution': 305.4064636230469, 'elevation': 852.5798950195312, 'location': {'lat': 36.47216482017924, 'lng': -117.2383269867277}}, {'resolution': 305.4064636230469, 'elevation': 1523.310668945312, 'location': {'lat': 36.46476089162127, 'lng': -117.3710144474311}}, {'resolution': 305.4064636230469, 'elevation': 877.4044189453125, 'location': {'lat': 36.45721011906031, 'lng': -117.5036763168041}}, {'resolution': 305.4064636230469, 'elevation': 1708.958984375, 'location': {'lat': 36.44951257156779, 'lng': -117.6363121046631}}, {'resolution': 305.4064636230469, 'elevation': 1887.876220703125, 'location': {'lat': 36.44166831951967, 'lng': -117.768921321772}}, {'resolution': 305.4064636230469, 'elevation': 1087.244506835938, 'location': {'lat': 36.43367743459353, 'lng': -117.901503479859}}, {'resolution': 305.4064636230469, 'elevation': 1142.37939453125, 'location': {'lat': 36.42553998976568, 'lng': -118.0340580916333}}, {'resolution': 610.8129272460938, 'elevation': 2923.857421875, 'location': {'lat': 36.41725605930836, 'lng': -118.1665846708025}}, {'resolution': 610.8129272460938, 'elevation': 2918.26123046875, 'location': {'lat': 36.40929111136249, 'lng': -118.2848827712816}}, {'resolution': 610.8129272460938, 'elevation': 2940.445556640625, 'location': {'lat': 36.40941185865138, 'lng': -118.1519776388197}}, {'resolution': 305.4064636230469, 'elevation': 1112.6015625, 'location': {'lat': 36.40938533885101, 'lng': -118.0190723451564}}, {'resolution': 305.4064636230469, 'elevation': 1088.75146484375, 'location': {'lat': 36.40933559950194, 'lng': -117.8861673290942}}, {'resolution': 305.4064636230469, 'elevation': 1919.440307617188, 'location': {'lat': 36.40941906667621, 'lng': -117.7532621081922}}, {'resolution': 305.4064636230469, 'elevation': 1566.376831054688, 'location': {'lat': 36.40935526669507, 'lng': -117.6203568536442}}, {'resolution': 305.4064636230469, 'elevation': 514.292724609375, 'location': {'lat': 36.40937065033142, 'lng': -117.4874518524606}}, {'resolution': 305.4064636230469, 'elevation': 1212.0146484375, 'location': {'lat': 36.40941683734199, 'lng': -117.3545465754086}}, {'resolution': 305.4064636230469, 'elevation': 1812.393676757812, 'location': {'lat': 36.40931575721761, 'lng': -117.221641392266}}, {'resolution': 305.4064636230469, 'elevation': 1710.518432617188, 'location': {'lat': 36.40939626383034, 'lng': -117.0887363495548}}, {'resolution': 305.4064636230469, 'elevation': -26.68322563171387, 'location': {'lat': 36.40940517065005, 'lng': -116.955831048643}}, {'resolution': 305.4064636230469, 'elevation': -28.13953971862793, 'location': {'lat': 36.40882589705786, 'lng': -116.8404758414724}}, {'resolution': 305.4064636230469, 'elevation': 132.6836395263672, 'location': {'lat': 36.4018694653343, 'lng': -116.9730928474912}}, {'resolution': 305.4064636230469, 'elevation': 1686.580688476562, 'location': {'lat': 36.39476644299685, 'lng': -117.1056858619867}}, {'resolution': 305.4064636230469, 'elevation': 2105.260009765625, 'location': {'lat': 36.38751689487414, 'lng': -117.2382543956065}}, {'resolution': 305.4064636230469, 'elevation': 527.962646484375, 'location': {'lat': 36.38012088709851, 'lng': -117.3707979598863}}, {'resolution': 305.4064636230469, 'elevation': 666.3414916992188, 'location': {'lat': 36.37257848710318, 'lng': -117.5033160672664}}, {'resolution': 305.4064636230469, 'elevation': 1488.711059570312, 'location': {'lat': 36.36488976361969, 'lng': -117.6358082311094}}, {'resolution': 305.4064636230469, 'elevation': 1400.7841796875, 'location': {'lat': 36.35705478667514, 'lng': -117.7682739657164}}, {'resolution': 305.4064636230469, 'elevation': 1143.099731445312, 'location': {'lat': 36.34907362758932, 'lng': -117.9007127863441}}, {'resolution': 305.4064636230469, 'elevation': 1181.340698242188, 'location': {'lat': 36.34094635897192, 'lng': -118.0331242092214}}, {'resolution': 610.8129272460938, 'elevation': 2751.839111328125, 'location': {'lat': 36.33267305471968, 'lng': -118.1655077515661}}, {'resolution': 610.8129272460938, 'elevation': 3057.779052734375, 'location': {'lat': 36.32463905726876, 'lng': -118.2861064927266}}, {'resolution': 610.8129272460938, 'elevation': 2719.926025390625, 'location': {'lat': 36.3247609956847, 'lng': -118.1533458783185}}, {'resolution': 305.4064636230469, 'elevation': 1098.33154296875, 'location': {'lat': 36.32473612199837, 'lng': -118.0205850985481}}, {'resolution': 305.4064636230469, 'elevation': 1324.103271484375, 'location': {'lat': 36.32468333030801, 'lng': -117.8878245939896}}, {'resolution': 305.4064636230469, 'elevation': 1440.75048828125, 'location': {'lat': 36.32476854276223, 'lng': -117.7550638912993}}, {'resolution': 305.4064636230469, 'elevation': 1557.494506835938, 'location': {'lat': 36.3247069430452, 'lng': -117.6223031483816}}, {'resolution': 305.4064636230469, 'elevation': 1032.469970703125, 'location': {'lat': 36.32471841613102, 'lng': -117.4895426614319}}, {'resolution': 305.4064636230469, 'elevation': 527.2896118164062, 'location': {'lat': 36.32476690257477, 'lng': -117.3567819017627}}, {'resolution': 305.4064636230469, 'elevation': 1842.742431640625, 'location': {'lat': 36.32466857686227, 'lng': -117.224021227001}}, {'resolution': 305.4064636230469, 'elevation': 1773.74560546875, 'location': {'lat': 36.32474431471771, 'lng': -117.0912607028844}}, {'resolution': 305.4064636230469, 'elevation': 276.2406005859375, 'location': {'lat': 36.32475607512329, 'lng': -116.9584999175395}}, {'resolution': 305.4064636230469, 'elevation': -47.1343879699707, 'location': {'lat': 36.3243212826978, 'lng': -116.8376683290142}}, {'resolution': 305.4064636230469, 'elevation': 484.9957275390625, 'location': {'lat': 36.31737487374036, 'lng': -116.9701422213152}}, {'resolution': 305.4064636230469, 'elevation': 2156.405517578125, 'location': {'lat': 36.31028232441902, 'lng': -117.1025922567147}}, {'resolution': 305.4064636230469, 'elevation': 1666.653442382812, 'location': {'lat': 36.30304369922062, 'lng': -117.2350179493857}}, {'resolution': 305.4064636230469, 'elevation': 473.0885009765625, 'location': {'lat': 36.29565906392671, 'lng': -117.3674188143805}}, {'resolution': 305.4064636230469, 'elevation': 1494.529418945312, 'location': {'lat': 36.28812848561098, 'lng': -117.4997943676481}}, {'resolution': 305.4064636230469, 'elevation': 1609.83056640625, 'location': {'lat': 36.28045203263655, 'lng': -117.6321441260505}}, {'resolution': 305.4064636230469, 'elevation': 1677.654541015625, 'location': {'lat': 36.27262977465326, 'lng': -117.7644676073796}}, {'resolution': 305.4064636230469, 'elevation': 1440.137451171875, 'location': {'lat': 36.26466178259496, 'lng': -117.8967643303738}}, {'resolution': 305.4064636230469, 'elevation': 1287.98828125, 'location': {'lat': 36.2565481286766, 'lng': -118.0290338147341}}, {'resolution': 610.8129272460938, 'elevation': 2681.046875, 'location': {'lat': 36.24828888639149, 'lng': -118.1612755811416}}, {'resolution': 610.8129272460938, 'elevation': 2385.591552734375, 'location': {'lat': 36.23998226898982, 'lng': -118.2904941330517}}, {'resolution': 610.8129272460938, 'elevation': 2551.55224609375, 'location': {'lat': 36.24010888392858, 'lng': -118.1578774437196}}, {'resolution': 305.4064636230469, 'elevation': 1285.154907226562, 'location': {'lat': 36.24008914077599, 'lng': -118.0252605730775}}, {'resolution': 305.4064636230469, 'elevation': 1523.723876953125, 'location': {'lat': 36.2400271817175, 'lng': -117.8926439720552}}, {'resolution': 305.4064636230469, 'elevation': 2007.4150390625, 'location': {'lat': 36.24011762100977, 'lng': -117.7600271917052}}, {'resolution': 305.4064636230469, 'elevation': 1553.094360351562, 'location': {'lat': 36.24006170213116, 'lng': -117.6274103527907}}, {'resolution': 305.4064636230469, 'elevation': 1764.944946289062, 'location': {'lat': 36.24006315284382, 'lng': -117.4947937771414}}, {'resolution': 305.4064636230469, 'elevation': 541.791015625, 'location': {'lat': 36.2401174164393, 'lng': -117.3621769361128}}, {'resolution': 305.4064636230469, 'elevation': 1028.81787109375, 'location': {'lat': 36.24002532186575, 'lng': -117.2295601592652}}, {'resolution': 305.4064636230469, 'elevation': 2259.68505859375, 'location': {'lat': 36.24009018234874, 'lng': -117.0969435558095}}, {'resolution': 305.4064636230469, 'elevation': 587.7286987304688, 'location': {'lat': 36.24010827021726, 'lng': -116.9643266844416}}, {'resolution': 305.4064636230469, 'elevation': -84.61699676513672, 'location': {'lat': 36.23998, 'lng': -116.83171}}]}"

DEBUG = False

def getElevation(lat1=36.578581, long1=-118.291994, lat2=36.23998, long2=-116.83171,sensor="false", **elvtn_args):
    
    resX = 20
    resY = 20

    locations = ""

    for y in range(0, resY):
        for x in range(0, resX):
            lat = (lat2-lat1)*(x/float(resX-1)) + lat1
            lon = (long2-long1)*(y/float(resY-1)) + long1
            locations += str(lat)+","+str(lon)+"|"

    locations = locations[:-1]

    if DEBUG is False:
        elvtn_args.update({
            'locations': locations,
            'sensor': sensor
        })

        url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
        response = simplejson.load(urllib.urlopen(url))
    else:
        response = ast.literal_eval(RESPONSE_CACHE)

    # Create a dictionary for each results[] object
    elevationArray = []

    minVal = 99999999999.
    maxVal = 0.

    #read result
    for resultset in response['results']:
        value = resultset['elevation']
        if value < minVal:
            minVal = value
        if value > maxVal:
            maxVal = value
        elevationArray.append(value)

    #normalize result
    elevationArrayNormalized = []
    for elev in elevationArray:
        val = (elev-minVal) / (maxVal-minVal)
        elevationArrayNormalized.append(val)

    print(len(response['results']))


    #convert to pixels
    pixels = []
    for val in elevationArrayNormalized:
        pixels.append(val*255)

    img = Image.new('L', (resX, resY))
    img.putdata(pixels)
    img.save('image.bmp')


    #print(pixels)


if __name__ == '__main__':
        
    print("")
    print("Elevation Depth Map Maker")
    print("")

    # Collect the Latitude/Longitude input string
    # from the user
    startStr = raw_input('Enter the start latitude,longitude value (default Mt. Whitney) --> ').replace(' ','')
    if not startStr:
      startStr = "36.578581,-118.291994"

    endStr = raw_input('Enter the end latitude,longitude value (default Death Valley) --> ').replace(' ','')
    if not endStr:
      endStr = "36.23998,-116.83171"

    pathStr = startStr + "|" + endStr

    getElevation()