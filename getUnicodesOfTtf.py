
import os
from fontTools.ttLib import TTFont
#https://fonttools.readthedocs.io/en/latest/ttLib/tables/_c_m_a_p.html
#Platform ID	Platform name	Platform-specific encoding IDs
#0	Unicode	Various
#1	Macintosh	Script manager code
#2	ISO [deprecated]	ISO encoding [deprecated]
#3	Windows	Windows encoding
#4	Custom	Custom


onlywindowsencoding = True
current_working_directory = os.getcwd()
print(current_working_directory)
if onlywindowsencoding:print("Only Windows Encoding is activated")

fonts = []
for file in os.listdir(current_working_directory):
    if file.endswith(".ttf"):
        fonts.append(os.path.join(file))
print (fonts)


for font in fonts:
    filename=font+".csv"
    path = current_working_directory + "/" + font

    chars = []
    codes = []
    with TTFont(path, 0, ignoreDecompileErrors=True) as ttf:
        for x in ttf["cmap"].tables:
            #print(x)
            for (code, _) in x.cmap.items():
                #print(x.platEncID)
                if onlywindowsencoding:
                    if x.platEncID == 3:
                        chars.append(chr(code))
                        codes.append(code)
                # chars.append(ttf.getGlyphName(code))
    print(chars)
    print(codes)

    utf8 = []
    with (TTFont(path, 0, ignoreDecompileErrors=True) as ttf):
        for x in ttf["cmap"].tables:
            for (code, _) in x.cmap.items():
                if onlywindowsencoding:
                    if x.platEncID == 3:
                        utf8.append(hex(code))
    print(utf8)


    def whritedata(string):
        f = open(filename, "a")
        f.write(string + "\n")
        f.close()
    whritedata("unicode,unicode padded,unicodevalue")
    print (str(len(utf8)) + " Glyphes detected.")
    for code in utf8:
        hexvalue = code[2:len(code)]
        while len(hexvalue) < 4:
            utf16 = "0" + hexvalue
            hexvalue = "0" + hexvalue
        whritedata(code + ",u+" + utf16 + "," + hexvalue)
