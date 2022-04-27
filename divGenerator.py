headTemplate = '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <title>ACES VWG ODT - Compare Images </title>
    <style>
        * {
            margin: auto;
            padding: 0;
            text-align: center;
        }
    </style>
    <link rel="stylesheet" type="text/css"
        href="https://rawgit.com/NUKnightLab/juxtapose/1.1.3/juxtapose/css/juxtapose.css" />
</head>

<body>

    <style>
        a.jx-knightlab div.knightlab-logo {
            visibility: hidden;
            display: none;
        }
        a.jx-knightlab span.juxtapose-name {
            visibility: hidden;
            display: none;
        }
        div.jx-slider {
            color: #f70d8a;
        }
        div.jx-image div.jx-label {
            background-color: #f70d8a;
            opacity:1;
            color:#000000;
        }

        h1  {
        padding: 10px;}

        .grid-container {
        display: grid;
        grid-template-columns: COLUMN_BLOCK;
        grid-gap: 10px;
        }
    #juxtapose-wrapper {
      border: 10px solid #f70d8a;
    }
    </style>
    <!-- Title section -->
    <div class="title">
        <h1>HEADINGBLOCK</h1>
        Only tested and known to work on a Pro Display XDR in Chrome under MacOS 12.3
        <br>
        <br>
    
    <div  class="grid-container" id="compares" style="width:90%;background-color:transparent;">
'''


divTemplateSDRvsHDR = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate A revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="A - SDR" />
            <img src="images/ACES_ODT_Candidate A revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="A - HDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate B revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="B - SDR" />
            <img src="images/ACES_ODT_Candidate B revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="C - SDR" />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''

divTemplateZvsHDR = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate A revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="A - HDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate B revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''

divTemplateZvsSDR = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate A revRRR - SDRsim.XXXX.avif"  loading="lazy" data-label="A - SDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate B revRRR - SDRsim.XXXX.avif"  loading="lazy" data-label="B - SDR"  />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate Z revRRR - Rec.2100.XXXX.avif"    loading="lazy" data-label="Matrix + EOTF" />
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"  loading="lazy" data-label="C - SDR"  />
        </div>'''

divTemplateAvsC = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate A revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="A - SDR" />
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="C - SDR" />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate A revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="A - HDR"  />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''

divTemplateBvsC = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate B revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="B - SDR" />
            <img src="images/ACES_ODT_Candidate C revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="C - SDR" />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate B revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
            <img src="images/ACES_ODT_Candidate C revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="C - HDR"  />
        </div>'''

divTemplateAvsB = '''        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate A revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="A - SDR" />
            <img src="images/ACES_ODT_Candidate B revRRR - SDRsim.XXXX.avif"    loading="lazy" data-label="B - SDR" />
        </div>
        <div class="juxtapose" data-startingposition="50%" data-showlabels="true"style="margin: 0 auto">>
            <img src="images/ACES_ODT_Candidate A revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
            <img src="images/ACES_ODT_Candidate B revRRR - Rec.2100.XXXX.avif"  loading="lazy" data-label="B - HDR"  />
        </div>'''


footTemplate = '''    </div>
    <script
        src="js/juxtapose.min.js">
    </script>
    <link rel="stylesheet"
        href="css/juxtapose.css">
</body>

</html>'''



rev = '008'

## get list of image names from image directory
import os
imageNames = os.listdir('images')
## isolate frame numbers from name
frameNumbers = [x.split('.')[-2] for x in imageNames]
## sort frame numbers
frameNumbers.sort()
## remove duplicates
frameNumbers = list(dict.fromkeys(frameNumbers))
frameNumbers = [x for x in frameNumbers if x != '']

for frame in frameNumbers:
    print(frame)

############################################

### Write out SDR vs HDR
newDivs = []
description = 'ACES 2.0 OT Candidates revRRR - SDR vs HDR'.replace('RRR', rev)
for frame in frameNumbers:
    # print(str(i).zfill(4))
    newDivs.append(divTemplateSDRvsHDR.replace('XXXX', frame).replace('RRR', rev))

# for div in newDivs:
#     print(div)

#write to html file on disk
with open('sdrVsHdr.html', 'w') as f:
    f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','33% 33% 33%'))
    f.write('\n'.join(newDivs))
    f.write(footTemplate)

############################################

### Write out Matrix + EOTF vs HDR
newDivs = []
description = 'ACES 2.0 OT Candidates revRRR - Matrix + EOTF vs HDR'.replace('RRR', rev)
for frame in frameNumbers:
    # print(str(i).zfill(4))
    newDivs.append(divTemplateZvsHDR.replace('XXXX', frame).replace('RRR', rev))

# for div in newDivs:
#     print(div)

#write to html file on disk
with open('MatrixEOTFvsHDR.html', 'w') as f:
    f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','33% 33% 33%'))
    f.write('\n'.join(newDivs))
    f.write(footTemplate)

############################################

### Write out Matrix + EOTF vs SDR
newDivs = []
description = 'ACES 2.0 OT Candidates revRRR - Matrix + EOTF vs SDR'.replace('RRR', rev)
for frame in frameNumbers:
    # print(str(i).zfill(4))
    newDivs.append(divTemplateZvsSDR.replace('XXXX', frame).replace('RRR', rev))

# for div in newDivs:
#     print(div)

#write to html file on disk
with open('MatrixEOTFvsSDR.html', 'w') as f:
    f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','33% 33% 33%'))
    f.write('\n'.join(newDivs))
    f.write(footTemplate)


############################################

### Write out A vs C
newDivs = []
description = 'ACES 2.0 OT Candidates revRRR - A vs C'.replace('RRR', rev)
for frame in frameNumbers:
    # print(str(i).zfill(4))
    newDivs.append(divTemplateAvsC.replace('XXXX', frame).replace('RRR', rev))

for div in newDivs:
    print(div)

#write to html file on disk
with open('AvsC.html', 'w') as f:
    f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','50% 50%'))
    f.write('\n'.join(newDivs))
    f.write(footTemplate)

############################################

### Write out A vs B
newDivs = []
description = 'ACES 2.0 OT Candidates revRRR - A vs B'.replace('RRR', rev)
for frame in frameNumbers:
    # print(str(i).zfill(4))
    newDivs.append(divTemplateAvsB.replace('XXXX', frame).replace('RRR', rev))

for div in newDivs:
    print(div)

#write to html file on disk
with open('AvsB.html', 'w') as f:
    f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','50% 50%'))
    f.write('\n'.join(newDivs))
    f.write(footTemplate)

############################################

### Write out B vs C
newDivs = []
description = 'ACES 2.0 OT Candidates revRRR - B vs C'.replace('RRR', rev)
for frame in frameNumbers:
    # print(str(i).zfill(4))
    newDivs.append(divTemplateBvsC.replace('XXXX', frame).replace('RRR', rev))

for div in newDivs:
    print(div)

#write to html file on disk
with open('BvsC.html', 'w') as f:
    f.write(headTemplate.replace('HEADINGBLOCK', description).replace('COLUMN_BLOCK','50% 50%'))
    f.write('\n'.join(newDivs))
    f.write(footTemplate)