from django.utils.safestring import mark_safe

crop_dict = {
    'Tomato' : mark_safe("""
    Soil: Well drain, sandy loam, PH-6-7.5
Climate: Warm & Humid, Temp.
21-270 C
Varieties: Pusa Ruby, Sioux, Dhanshree, Rajshree, Pusa Gaurav, Arka Vikas, Arka Saurabh, Pusa Sheetal.
Propn method: Seed
Seed Rate, Spacing & Planting
season: 400-500 g/ha,
60 x 45 cm, Kharif & Rabi.
FIELD7:
Fertilizer dose: FYM-25 t/ha, 100:50:50 Kg
NPK/ha
FIELD9:
Maturity Indices: Mature Green stage, Pink Stage, Ripe Stage, Fully Ripe Stage.
Harvesting: Harvesting done manually by plucking at different stage of maturity.
FIELD12:
Yield: 25-30
t/ha, F1- 50-60
t/ha
FIELD14:
FIELD15:
Pests: Fruit borer, White fly, Thrips, leaf minor.
FIELD17:
Diseases: Early blight, late blight, leaf curl virus (WF), Spotted wilt virus
(Thrips)
    """
        ),

'Potato' : mark_safe("""Soil: Well drain, sandy loam, red lateritic, PH-6-6.5<br>
Climate: Warm & Humid, Temp.<br>
18-220 C<br>
Varieties: Pusa Purple Long, Pusa Kranti, Pusa Anmol, Manjri Gota, Krishna, Pragati, Arka Navneet, Phule Harit.<br>
Propn method: Seed<br>
Seed Rate, Spacing & Planting<br>
season: 600-800 g/ha<br>
60 x 60 cm,<br>
60 x 45 cm,<br>
45 x 45 cm & Kharif, Rabi,<br>
Summer.<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 100:50:50 Kg<br>
NPK/ha<br>
FIELD9:<br>
Maturity Indices: Desirable size, colour & tender stage<br>
Harvesting: Harvesting done by cutting with a small pruning shear or sharp knife<br>
FIELD12:<br>
Yield: 20-30<br>
t/ha, F1- 40-50<br>
t/ha<br>
FIELD14:<br>
FIELD15:<br>
Pests: Brinjal fruit and shoot borer, stem borer,<br>
aphids<br>
FIELD17:<br>
Diseases: Phomopsis blight, damping off, wilt, little leaf (Jassids)""",
        ),  

           "Brinjal" : mark_safe(""" 
Soil: Well drain, sandy loam, red lateritic, PH-6-6.5<br>
Climate: Warm & Humid, Temp.<br>
18-220 C<br>
Varieties: Pusa Purple Long, Pusa Kranti, Pusa Anmol, Manjri Gota, Krishna, Pragati, Arka Navneet, Phule Harit.<br>
Propn method: Seed<br>
Seed Rate, Spacing & Planting<br>
season: 600-800 g/ha<br>
60 x 60 cm,<br>
60 x 45 cm,<br>
45 x 45 cm & Kharif, Rabi,<br>
Summer.<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 100:50:50 Kg<br>
NPK/ha<br>
FIELD9:<br>
Maturity Indices: Desirable size, colour & tender stage<br>
Harvesting: Harvesting done by cutting with a small pruning shear or sharp knife<br>
FIELD12:<br>
Yield: 20-30<br>
t/ha, F1- 40-50<br>
t/ha<br>
FIELD14:<br>
FIELD15:<br>
Pests: Brinjal fruit and shoot borer, stem borer,<br>
aphids<br>
FIELD17:<br>
Diseases: Phomopsis blight, damping off, wilt, little leaf (Jassids)
      
  """ ), 

   "Chilli (Mexico) Fruits": ("""
      
Soil: Fertile, sandy loam,<br>
PH-6-8<br>
Climate: Warm & Humid, Temp.<br>
Varieties: Pusa Jwala, Agnirekha, Pusa Sadabahar, Pant C- 1, Arka Mohini, Arka Gaurav, Arka Lohit.<br>
Propn method: Seed<br>
Seed Rate, Spacing & Planting<br>
season: 1-1.5 Kg/ha,<br>
60 x 45 cm,<br>
45 x 45 cm & Kharif, Rabi, Summer.<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 100:50:50 Kg<br>
NPK/ha<br>
FIELD9:<br>
Maturity Indices: Harvested at two stages Green in colour & dry chilli when red in<br>
colour.<br>
Harvesting: Fruit are picked either green or fully red ripen.<br>
FIELD12:<br>
Yield: 5-7 t/ha<br>
FIELD14:<br>
FIELD15:<br>
Pests: Thrips<br>
FIELD17:<br>
Diseases: Anthracnose, leaf curl(WF & Thrips), mosaic<br>
(Aphids)
      
   """),


 'Okra' : mark_safe(""" 
    Soil: Sandy loam to clay, well drain, PH-6- 6.8<br>
Climate: Warm & Humid, Temp.<br>
20-300 C,<br>
continues rain are harmful.<br>
Varieties: Pusa Sawani, Parbhani Kranti, Arka Anamica, Punjab Padmini, phule Kirti, Phule Uttakarsha.<br>
Propn method: Seed<br>
Seed Rate, Spacing & Planting<br>
season: 12-15 Kg/ha, 45<br>
x 30 cm, Kharif & Summer.<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 100:50:50 Kg<br>
NPK/ha<br>
FIELD9:<br>
Maturity Indices: Green tender, Size 6-8cm, 6-7 days after opening of flower<br>
Harvesting: Harvesting done by picking of tender fruit.<br>
FIELD12:<br>
Yield: 12-15<br>
t/ha<br>
FIELD14:<br>
FIELD15:<br>
Pests: Shoot and borer, jassids, White fly (WF)<br>
FIELD17:<br>
Diseases: Yellow vein mosaic virus (WF),<br>
Enation leaf curl virus<br>
(WF).
  """ ), 

   'Onion' : mark_safe(""" 
Soil: Sandy loam with good organic matter, PH- 6-7.5.<br>
Climate: Cool season grows well under mild climate, temp.<br>
o<br>
20-25 C.<br>
Varieties: N-53, Baswant 780, Phule Safed, Pusa Red, Phule Utkarsha, Arka Kalyan, Phule Suvarna.<br>
Propn method: Seed<br>
Seed Rate, Spacing & Planting<br>
season: 10-12 Kg/ha for<br>
rabi, 12-15 Kg/ha for Kharif.<br>
15 x 10 cm, 12.5<br>
x 7.5 cm, Kharif, Rabi, Summer.<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 150:50:50 Kg<br>
NPK/ha<br>
FIELD9:<br>
Maturity Indices: 3-4 month after transplanting, Neck Fall 60-<br>
70%,<br>
Harvesting: Harvesting is done by pulling out plants when tops are drooping but still green.<br>
FIELD12:<br>
Yield: 20-25<br>
t/ha,<br>
FIELD14:<br>
FIELD15:<br>
Pests: Thrips, onion fly, leaf eating caterpillar, head borer, cut<br>
worm.<br>
FIELD17:<br>
Diseases: Purple blotch, onion smut, downey mildew<br>
  """ ), 

   'Cabbage' : mark_safe(""" 
Soil: Well drain, sandy to heavy clay loam, PH 6-8.<br>
Climate: Cool season crop, temp.<br>
o<br>
13-16 C,<br>
Varieties: Golden Acre, Pride of India, Pusa Drum Head, Copenhagen Market, Pusa Mukta, Pusa Ageti, Pusa Sambandh.<br>
Propn method: Seed<br>
Seed Rate, Spacing & Planting<br>
season: 400-500 g/ha,<br>
45 x 15 cm,<br>
60 x 45 cm, Kharif, Rabi<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 150:50:50 Kg<br>
NPK/ha<br>
FIELD9:<br>
Maturity Indices: Colour changes to light green at maturity, compact head.<br>
Harvesting: The heads are cut with sickle attached with some wrapper leaves.<br>
FIELD12:<br>
Yield: 20-30<br>
t/ha<br>
FIELD14:<br>
FIELD15:<br>
Pests: Diamond back moth, cabbage butterfly, mustard<br>
saw fly.<br>
FIELD17:<br>
Diseases: Damping off, club rot, black rot<br>
  """ ), 

     'Cauliflower' : mark_safe(""" 
Soil: Sandy loam, Well drain, PH 6.5-7.5<br>
Climate: Cool season crop, temp.<br>
o<br>
17-20 C<br>
Varieties: Pusa Ketki, Pusa Himjyoti, Pusa Snowball K-1, Pusa Meghna, Hisar- 1, Pusa Deepali, Pant Shubhra. Arka kanti<br>
Propn method: Seed<br>
Seed Rate, Spacing & Planting<br>
season: 400-500 g/ha<br>
60 x 45 cm,<br>
45 x 45 cm, Kharif, Rabi<br>
FIELD7:<br>
Fertilizer dose: FYM-15 t/ha, 100:50:50 Kg<br>
NPK/ha<br>
FIELD9:<br>
Maturity Indices: Curd attained desirable size, head are compact.<br>
Harvesting: Curd cut with sharp knife with 2-3 large leaves to protect the curd.<br>
FIELD12:<br>
Yield: 15-20<br>
t/ha<br>
FIELD14:<br>
FIELD15:<br>
Pests: Diamond back moth, cabbage butterfly, mustard<br>
saw fly.<br>
FIELD17:<br>
Diseases: Damping off, club rot, black rot<br>
  """ ), 

  ' Cucumber' : mark_safe(""" 
  Soil: Sandy loam to clay soil. PH 5.5 -6.8<br>
  Climate: Warm season crop, Temp. 18- 240C<br>
  Varieties: Phule Shubhangi, Pusa Sanyog, Himangi, Poona Khira, Sheetal, Pusa Uday, Swarna Ageti.<br>
  Propn method: Seed<br>
  Seed Rate, Spacing & Planting<br>
  season: 2.5-3.5 Kg/ha,<br>
  1 x 0.5 m Kharif & Summer.<br>
  FIELD7: FYM-15 t/ha, 100:50:50 Kg<br>
  NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/ immature stage, 60-70 days after sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Regular harvesting of fruit is necessary, to avoid inhabitation of further fruit set<br>
  on plant<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 25-35<br>
  t/ha<br>
  Pests:<br>
  FIELD17: Fruit Fly,<br>
  Red Pumpkin beetle,<br>
  Diseases: Cucumber mosaic virus,<br>
 
  """ ), 

  'Watermelon' : mark_safe(""" 
  Soil: Loam & Sandy loam best, rich in organic matter,<br>
  PH 6-6.5<br>
  Climate: Warm season crop, Temp. 24- 270C, high temp & low humidity suitable for<br>
  watermelon.<br>
  Varieties: Sugar Baby, Arka Manik, Arka Jyoti, Pusa Bedana (seedless variety), Durgapura Meetha, Durgapura Keshar,<br>
  Durgapura Lal.<br>
  Propn method: Seed<br>
  Seed Rate, Spacing & Planting<br>
  season: 3.5-5 kg/ha<br>
  2 x 0.5 m,<br>
  Summer<br>
  FIELD7: 25 t FYM/ha,<br>
  100:50:50 Kg<br>
  NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: 95-120 days after seed sowing, change of ground spot color green to yellow & dull-thud sound on<br>
  thumping the fruit.<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Harvested at full ripening stage,<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 25-35<br>
  t/ha<br>
  Pests:<br>
  FIELD17: Epilachna Beetle,<br>
  Aphids,<br>
  Diseases: Green Mottle Mosaic.<br>
  
  """ ), 

  'Muskmelon' : mark_safe(""" 
  Soil: Loam & Sandy loam best, rich in organic matter,<br>
  PH 6-7.5<br>
  Climate: High temp. & low humidity for fruit ripening, temp.<br>
  20-250C.<br>
  Varieties: Arka Jeet, Arka Rajhans, Pusa Madhuras, Pusa Sharbati, Pusa Rasraj, Panjab Raseela, Hara Madhu, Durgapura<br>
  Madhu, Hisar Saras.<br>
  Propn method: Seed<br>
  Seed Rate, Spacing & Planting<br>
  season: 5-6 kg/ha,<br>
  1.5 x 0.5m,<br>
  90 x 60 cm Summer<br>
  FIELD7: 15 t FYM/ha,<br>
  100:50:50 Kg<br>
  NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Mature fruit separate (slip) easily from stem is called full slip  stage, half slip stage half stem separate<br>
  from stem easily.<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Half slip for long-distance market, Full slip stage for local market & 90-125 day after seed<br>
  sowing,<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 10-15<br>
  t/ha<br>
  Pests:<br>
  FIELD17: Mites.<br>
  Diseases: Bud Necrosis,<br>
 
  """ ), 

  'Bottle Gourd' : mark_safe(""" 
  Soil: Well-drained sandy loam with rich organic matter,<br>
  PH 6-7<br>
  Climate: Warm and humid climate and slightly cool, temp. 24-270C.<br>
  Varieties: Samrat, Pusa Sandesh, Pusa Meghdoot, Arka Bahar, Pusa Navneet, Pusa Manjari, Panjab Komal.<br>
  Propn method: Seed<br>
  Seed Rate, Spacing & Planting<br>
  season: 3-4 kg/ha,<br>
  2.5 x 1 m, 3 x 1 m,<br>
  Kharif & Rabi<br>
  FIELD7: 15 t FYM/ha,<br>
  100:50:50 Kg<br>
  NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/immature stage, 60-70 days after seed sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The fruit harvested at attain marketable stage, harvesting should be carefully so fruit do not get<br>
  Bruised.<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 25-30<br>
  t/ha<br>
  Pests:<br>
  FIELD17:<br>
  Diseases: Downy<br>
  
  """ ), 

  ' Ridge Gourd' : mark_safe(""" 
  Soil: Sandy loam with rich in organic matter<br>
  PH 6-7<br>
  Climate: Warm season crop, warm and humid climate, Temp. 24-270C<br>
  Varieties: Pusa Nasdar, Co-1, Co-2, Satputia, Panjab Sada Bahar, PKM-1, Arka Sujath, Konkan Harita<br>
  Propn method: Seed<br>
  Seed Rate, Spacing & Planting<br>
  season: 3.5-5 kg/ha<br>
  2 x 1 m, Kharif & Summer<br>
  FIELD7: 15 t FYM/ha<br>
  100:50:50 Kg<br>
  NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/ immature stage, 60-90 days after seed sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The fruit harvested at attain marketable stage after 5-7 days after anthesis<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 12-15<br>
  t/ha<br>
  Pests:<br>
  FIELD17:<br>
  Diseases:
  """ ), 

  'Sponge Gourd ' : mark_safe(""" 
  Soil: Sandy loam with rich in organic matter<br>
  PH 6-7<br>
  Climate: Warm season crop, warm and humid climate, Temp. 24-270C<br>
  Varieties: Pusa Chikni, Pusa Supriya, Pusa Sneha, Arka Sumeet, Pusa Nutan<br>
  Propn method: Seed<br>
  Seed Rate, Spacing & Planting<br>
  season: 2.5-3.5 kg/ha<br>
  2 x 1 m, Kharif & Summer<br>
  FIELD7: 15 t FYM/ha<br>
  100:50:50 Kg<br>
  NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/ immature stage, 60-90 days after seed sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The fruit harvested at attain marketable stage after 5-7 days after anthesis<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 8-12<br>
  t/ha<br>
  Pests:<br>
  FIELD17:<br>
  Diseases:
  """ ), 

  ' Bitter Gourd' : mark_safe(""" 
  Soil: Sandy loam with rich in organic matter<br>
  PH 6-7<br>
  Climate: Warm season crop, Temp. 25- 300C<br>
  Varieties: Hirkani, Phule Green Gold, Pusa Do Mausami, Pusa Vishesh, Arka Harit, Konkan Tara<br>
  Propn method: Seed<br>
  Seed Rate, Spacing & Planting<br>
  season: 4-6 kg/ha<br>
  2 x 1 m, Kharif & Summer<br>
  FIELD7: 15 t FYM/ha<br>
  100:50:50 Kg<br>
  NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/ immature stage, 50-60 days after seed sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Harvested at fruit attain marketable stage for 2-3 weeks after anthesis<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 10-15<br>
  t/ha<br>
  Pests:<br>
  FIELD17:<br>
  Diseases:
  """ ), 

  'Mango' : mark_safe(""" 
  Soil: Alluvial soil, Slightly acidic having PH-5.5-7<br>
  with good drainage is ideal.<br>
  Climate: Tropical climate having temp. 24-270C is ideal, high temp. during fruit development give good<br>
  quality fruit.<br>
  Varieties: Monoembryonic: Alphanso, Kesar, Langra, Vanraj, totapuri, Polyemryonic: Olour, Bappakai, Goa,<br>
  Hybrid: Mallika, Amrapali, Ratna, Sindhu<br>
  Propn method: Stone grafting, Soft wood grafting<br>
  Seed Rate, Spacing & Planting<br>
  season: 10 x 10 m<br>
  8 x 8 m<br>
  2.5 x 2.5 m (HDP)<br>
  June-July, Aug- September<br>
  FIELD7: 100 kg FYM/plant/ year 1000:500:1000<br>
  g NPK/plant/ year<br>
  Fertilizer dose:<br>
  FIELD9: Tapka stage, specific gravity-1.01-1.02, TSS-12-15%, Colour<br>
  dark green to light green, shoulder out grow the stalk end<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Harvesting should be done fruit attain full size, harvesting should be done with help of nutal zela or mango harvester.<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 2000-<br>
  3000<br>
  fruit/ plant/ year<br>
  Pests:<br>
  FIELD17: Fruit Fly, Stem Borer, Stone Weevil, Aphid.<br>
  Diseases: Powdery Mildew, Anthracnose.<br>
  """ ), 


  'Banana' : mark_safe(""" 
  Soil: Deep, alluvial, well drained, loamy with good organic matter<br>
  PH 6-8<br>
  Climate: Warm and humid, rainy climate, temp. 20-300C, rain fall 120 cm.<br>
  Varieties: Grand-9, Basarai, Srimanti, Harisal, Lal Velchi, Safed Velchi, Mahalaxmi, Poovan, Nendran.<br>
  Propn method: Rhizome (500-750g<br>
  wt.), suckers, Tissue culture.<br>
  Seed Rate, Spacing & Planting<br>
  season: 2 x 2 m<br>
  1.8 x 1.8 m<br>
  1.5 x 1.5 m June � July Sept. - oct.<br>
  FIELD7: 50 kg FYM/plant/ year 200:40:200 g<br>
  NPK/plant/ year<br>
  Fertilizer dose:<br>
  FIELD9: 11-14 month after planting, fruit mature after 120-140 day after flowering, metallic sound at finger taping, drying of upper leaves.<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The trunk is lopped with sickle, the bunch will not fall to ground to avoid injury and about 30 cm of stalk must be left to make<br>
  handling easy.<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 40<br>
  t/ha<br>
  Pests:<br>
  FIELD17: Weevil, Aphid.<br>
  Diseases: Sigatoka, Bunchy Top, Panama Wilt.
  """ ), 


  ' Grape' : mark_safe(""" 
  Soil: well drained, light, medium, alluvial soil, with good organic matter<br>
  PH 6.5-8<br>
  Climate: Semi arid and sub-tropical, summer hot and dry & mild winter, bright sunny days, temp. 10-400C.<br>
  Varieties: Thompson Seed Less, Sonaka, Tas-E Ganesh, Sharad Seed Lees (Black colour), Manik Chaman, Manjari Naveen, Perlette, Arkavati.<br>
  Propn method: Hard Wood Cutting (Root stock- Bangalore Dogridge,<br>
  One-10-R.<br>
  Seed Rate, Spacing & Planting<br>
  season: 3 x 1.5 m<br>
  2.5 x 1.5 m Jan-Feb.<br>
  FIELD7: 50 kg FYM/plant/ year 900:500:700 g<br>
  NPK/plant/ year<br>
  Fertilizer dose:<br>
  FIELD9: Fruit mature 120-140 day after fruit pruning, TSS-16-20 % (Brix)<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Fully ripe fruit are harvested, the bunch removed from vine by sharp secateurs.<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 25-40<br>
  t/ha<br>
  Pests:<br>
  FIELD17: Udya Beetle, Mealy Bug, Stem Girdler, Thrips<br>
  Diseases: Powdery mildew, Downy Mildew, Anthracnose.
  """ ), 
  
  ' Pomegran ate' : mark_safe(""" 
  Soil: Loamy and alluvial soil, medium or light soil is ideal,<br>
  PH 6-7.5<br>
  Climate: Cool winter and hot & dry summer where rainfall is low, temp. 10-400C<br>
  Varieties: Phule Bhagwa, Phule Arakta, Ganesh, Mridula<br>
  Propn method: Air Layering<br>
  Seed Rate, Spacing & Planting<br>
  season: 5 x 5 m June - July<br>
  FIELD7: 50 kg FYM/plant/ year 625:250:250 g<br>
  NPK/plant/<br>
  year<br>
  Fertilizer dose:<br>
  FIELD9: Fruit ready 150-170 day after flowering, TSS 16-17%, dark red color and surface become soft<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The fruit are harvested at proper stage of maturity<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 25-30<br>
  t/ha<br>
  Pests:<br>
  FIELD17: Fruit Borer, Anar Caterpillar<br>
  Diseases: Bacterial blight<br>
  """ ), 

  ' Sapota' : mark_safe(""" 
  Soil: Deep alluvial good organic matter<br>
  PH 6-7.5<br>
  Climate: Tropical climate rain fall125-250 cm, temp. range 20-340C<br>
  Varieties: Kalipatti, Pillipatti, Cricket Ball, Dhola Diwani, Culcutta Round<br>
  Propn method: Aproch Grafting, Inarch Grafting<br>
  Seed Rate, Spacing & Planting<br>
  season: 10x10 m<br>
  8x8 m June - July<br>
  FIELD7: 100 kg FYM/plant/ year 1000:500:500 g<br>
  NPK/plant/<br>
  year<br>
  Fertilizer dose:<br>
  FIELD9: Fruit mature 240-270 days after flowering, fruit develop dull orange or potato color, milky latex<br>
  content reduce<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Fully mature fruit are harvested with the help of sapota harvester<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 3000<br>
  fruit/ plant/ year<br>
  Pests:<br>
  FIELD17: Fruit Fly, Leaf Eating Caterpillar, Scale<br>
  Insect<br>
  Diseases: Leaf Spot and Fruit Rot<br>
  """ ), 


  ' Guava' : mark_safe(""" 
  Soil: Sandy loam with good organic matter<br>
  PH 6-7.5<br>
  Climate: Basically tropical climate grow wide range of climate<br>
  Varieties: L-49 (Sardar), Allahabad Safeda, Lalit, Banaras<br>
  Propn method: Air Layering, ground layering<br>
  Seed Rate, Spacing & Planting<br>
  season: 7x7 m 5x5 m<br>
  June - July<br>
  FIELD7: 50 kg FYM/plant/ year 625:250:250 g<br>
  NPK/plant/<br>
  year<br>
  Fertilizer dose:<br>
  FIELD9: Fruit mature 140-160 days after flowering, color change from pale green fruit become soft<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Hand pulling, picking is done 2-3 times in a weeks, fruit collect in basket<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15: 1500<br>
  Fruit/ plant/ year<br>
  Pests:<br>
  FIELD17: Fruit fly, White fly<br>
  Diseases: Anthracnose, Guava Canker
  """ ), 


  'Mandarin ' : mark_safe(""" 
  Soil: Sandy loam with good organic matter<br>
  PH 6-7.5<br>
  Climate: Tropical climate, temp.<br>
  25-350C<br>
  Varieties: Nagpur Mandarin, coorg Mandarin, Khashi, Kamla<br>
  Propn method: T-<br>
  Budding<br>
  Seed Rate, Spacing & Planting<br>
  season: 7x7 m 5x5 m June-July<br>
  FIELD7:<br>
  Fertilizer dose: 50 kg FYM/plant/ year<br>
  1000: 500:500 g<br>
  NPK/plant/ year<br>
  FIELD9:<br>
  Maturity Indices: Mature 210-240 day after flowering,<br>
  Harvesting: Fruit picker collect the fruit manually<br>
  FIELD12:<br>
  Yield:<br>
  FIELD14: 800-<br>
  1200<br>
  fruit/ plant/ year<br>
  FIELD15:<br>
  Pests: Fruit fly leaf minor, leaf eating caterpillar<br>
  FIELD17:<br>
  Diseases: Gummosis, Citrus Canker, Dieback<br>
  """ ), 


  ' Sweet orange' : mark_safe(""" 
  Soil: Sandy loam with good organic matter<br>
  PH 6-7.5<br>
  Climate: Sub-tropical, dry climates, low rainfall, temp. 20-300C<br>
  Varieties: Mosambi, Katol Gold, Pine Apple, Washington Novel, Satgudi, Jaffa<br>
  Propn method: T-<br>
  Budding<br>
  Seed Rate, Spacing & Planting<br>
  season: 6x6 m 5x5 m June-July<br>
  FIELD7:<br>
  Fertilizer dose: 50 kg FYM/plant/ year<br>
  1000: 500:500 g<br>
  NPK/plant/<br>
  year<br>
  FIELD9:<br>
  Maturity Indices: Mature 210-240 day after flowering,<br>
  Harvesting: Fruit picker collect the fruit manually<br>
  FIELD12:<br>
  Yield:<br>
  FIELD14: 600-<br>
  800<br>
  fruit/ plant/<br>
  year<br>
  FIELD15:<br>
  Pests: Fruit sucking moth, leaf minor<br>
  FIELD17:<br>
  Diseases: Gummosis, Citrus Canker, Dieback<br>
  """ ), 


  ' Acid Lime' : mark_safe(""" 
  Soil: Sandy loam with good organic matter<br>
  PH 6-7.5<br>
  Climate: Sub-tropical, dry climates, low rainfall, temp. 20-300C<br>
  Varieties: Sai Sarbati, Vikram Pramalini, Chakradhar (seedless) Baramasi, PDKV Bahar<br>
  Propn method: T-<br>
  Budding<br>
  Seed Rate, Spacing & Planting<br>
  season: 5x5 m June-July<br>
  FIELD7:<br>
  Fertilizer dose: 50 kg FYM/plant/ year<br>
  600: 300:300 g<br>
  NPK/plant/<br>
  year<br>
  FIELD9:<br>
  Maturity Indices: Mature 120-150 day after flowering,<br>
  Harvesting: Fruit picker collect the fruit manually<br>
  FIELD12:<br>
  Yield:<br>
  FIELD14: 3000<br>
  fruit/ plant/ year<br>
  FIELD15:<br>
  Pests: Fruit fly leaf minor, leaf eating caterpillar<br>
  FIELD17:<br>
  Diseases: Gummosis, Citrus Canker, Dieback
  """ ), 


  'Ber ' : mark_safe(""" 
  Soil: Sandy loam with good organic matter<br>
  PH 6-7.5<br>
  Climate: Sub-tropical, dry climates, low rainfall, temp. 20-300C<br>
  Varieties: Sai Sarbati, Vikram Pramalini, Chakradhar (seedless) Baramasi, PDKV Bahar<br>
  Propn method: T-<br>
  Budding<br>
  Seed Rate, Spacing & Planting<br>
  season: 5x5 m June-July<br>
  FIELD7:<br>
  Fertilizer dose: 50 kg FYM/plant/ year<br>
  600: 300:300 g<br>
  NPK/plant/<br>
  year<br>
  FIELD9:<br>
  Maturity Indices: Mature 120-150 day after flowering,<br>
  Harvesting: Fruit picker collect the fruit manually<br>
  FIELD12:<br>
  Yield:<br>
  FIELD14: 3000<br>
  fruit/ plant/ year<br>
  FIELD15:<br>
  Pests: Fruit fly leaf minor, leaf eating caterpillar<br>
  FIELD17:<br>
  Diseases: Gummosis, Citrus Canker, Dieback<br>
  """ ), 


  'Rose' : mark_safe(""" 
  Soil: Well drained, medium loam soil having PH 6-7.5 is ideal<br>
  Climate: Cool climate, Loves sunshine & free ventilation, Night Temp.<br>
  160C, produce more flower.<br>
  Varieties: Hybrid Tea: Super Star, Raktagandha, Arjun, Rajkumari, Bhim.<br>
  Floribundas: Mohini, Sindhoor, Suchitra.<br>
  Propn method: Shield budding & Cutting.<br>
  Seed Rate, Spacing & Planting season: 60 x 75 cm,<br>
  60 x 45 cm. Oct to Dec & May to June.<br>
  FIELD7:<br>
  Fertilizer dose: 8-10 kg / plant 250:500:375 kg/ha<br>
  FIELD9:<br>
  Maturity Indices: Cut flower: Tight bud stage<br>
  Loose Flower:<br>
  Fully open.<br>
  Harvesting: Harvesting should be done early morning or late evening<br>
  FIELD12:<br>
  Yield:<br>
  FIELD14: 30-40 flower/ plant/y r.<br>
  FIELD15:<br>
  Pests: Red Scale, Mites, Thrips, Mealy Bug.<br>
  FIELD17:<br>
  Diseases: Dieback, Powdery mildew, Black Spot, Rust.<br>
  """ ), 

  'Chrysanth emum' : mark_safe(""" 
  Soil: Well drained, sandy loam with good organic matter<br>
  PH 6.5-7<br>
  Climate: Short Day Plant, Temp.<br>
  20-270C<br>
  Varieties: Sonar Bangla, Sweet Heart, Kirti, Indira, Chandrama, Day Dream, Mahatma Gandhi, Chandrakant.<br>
  Propn method: Seeds, Root suckers or Terminal cuttings.<br>
  Seed Rate, Spacing & Planting season: 45 x 30 cm,<br>
  30 x 30 cm. Jan-Feb., Jun-July.<br>
  FIELD7:<br>
  Fertilizer dose: 20-30 t FYM/ha<br>
  200:200:200<br>
  kg/ha<br>
  FIELD9:<br>
  Maturity Indices: Standard: 40-<br>
  50% flower open,<br>
  Dwarf Var.: 80-<br>
  85% flower<br>
  open.<br>
  Harvesting: 3-4 months after TP.,<br>
  fully open flower are harvested.<br>
  FIELD12:<br>
  Yield:<br>
  FIELD14: 10-12<br>
  t/ha<br>
  FIELD15:<br>
  Pests: Aphids<br>
  FIELD17:<br>
  Diseases: Wilt, Stem & Foot rot<br>
  """ ), 

  'Aster' : mark_safe(""" 
  Soil: Well drained, loamy with good organic matter<br>
  PH 6-8<br>
  Climate: Mild Climate, Temp. 18-200C,<br>
  Avoid frost.<br>
  Varieties: Kamini, Pournima, Shashank, Phule ganesh White, Phule Ganesh Pink, Phule Ganesh<br>
  Violet<br>
  Propn method: Seeds<br>
  Seed Rate, Spacing & Planting season: 30 x 30 cm,<br>
  45 x 30 cm<br>
  FIELD7:<br>
  Fertilizer dose: 20-30 t FYM/ha<br>
  200:200:200<br>
  kg/ha<br>
  FIELD9:<br>
  Maturity Indices: 40-50% flower open,<br>
  Harvesting: Fully open flower are harvested<br>
  FIELD12:<br>
  Yield:<br>
  FIELD14: 18-20<br>
  t/ha<br>
  FIELD15:<br>
  Pests: Aphids, Thrips, Bud borer.<br>
  FIELD17:<br>
  Diseases:
  """ ), 

  'Marigold' : mark_safe(""" 
  Soil: Well Drain,<br>
  Climate: Mild Climate,<br>
  Varieties: Af. Marigold: Snowbird,<br>
  Propn method: Seeds<br>
  Seed Rate, Spacing & Planting season: 3 kg/ha<br>
  FIELD7:<br>
  Fertilizer dose: 15 t FYM/ha<br>
  FIELD9:<br>
  Maturity Indices: The flower are<br>
  Harvesting: Harvesting should<br>
  FIELD12:<br>
  Yield: AM: 8-12<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Red Mites,<br>
  FIELD17:<br>
  Diseases: Powdery
  """ ), 

  'Gladiolus' : mark_safe(""" 
  Soil: Light to clay<br>
  Climate: Mild climate,<br>
  Varieties: Phule Ganesh, Phule<br>
  Propn method: Corms,<br>
  Seed Rate, Spacing & Planting season: 1,50,000<br>
  FIELD7:<br>
  Fertilizer dose: 15-20 t FYM/ha<br>
  FIELD9:<br>
  Maturity Indices: basal flower<br>
  Harvesting: Spikes are<br>
  FIELD12:<br>
  Yield: 2 lake<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Aphids<br>
  FIELD17:<br>
  Diseases: Wilt or Collar<br>
  """ ), 

  'Blanket flower' : mark_safe(""" 
  Soil:<br>
  Climate: Avoid frost.<br>
  Varieties: Cobalt, Monark,<br>
  Propn method: Seeds<br>
  Seed Rate, Spacing & Planting season: May - July.<br>
  FIELD7:<br>
  Fertilizer dose: kg/ha<br>
  FIELD9:<br>
  Maturity Indices: flower show the<br>
  color<br>
  Harvesting:<br>
  FIELD12:<br>
  Yield:<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Jassides<br>
  FIELD17:<br>
  Diseases: mildew.<br>
  """ ), 

  'Jasmine' : mark_safe(""" 
  Soil: Sandy loam<br>
  Climate: Mild tropical<br>
  Varieties: Khoya, Motia, Single<br>
  Propn method: Stem<br>
  Seed Rate, Spacing & Planting season: 1.2 x 1.2 m,<br>
  FIELD7:<br>
  Fertilizer dose: 10 kg<br>
  FIELD9:<br>
  Maturity Indices: Flowering start<br>
  Harvesting: fully develop/<br>
  FIELD12:<br>
  Yield: 8-Jul<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Bud Warm,<br>
  FIELD17:<br>
  Diseases: Wilt, Leaf<br>
  """ ), 


  'Mogra' : mark_safe(""" 
  Soil: with good<br>
  Climate: climate, warm<br>
  Varieties: Mohora, Double<br>
  Propn method: cutting,<br>
  Seed Rate, Spacing & Planting season: Jun - July.<br>
  FIELD7:<br>
  Fertilizer dose: FYM/Plant/yr.<br>
  FIELD9:<br>
  Maturity Indices: from IInd yr after<br>
  Harvesting: opened flower<br>
  FIELD12:<br>
  Yield: t/ha<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Red Mites,<br>
  FIELD17:<br>
  Diseases: Spot, Leaf<br>
  """ ), 

  'Jai' : mark_safe(""" 
  Soil: Sandy loam<br>
  Climate: Mild tropical<br>
  Varieties: Surabhi, Co-1 Pitchi,<br>
  Propn method: Semi hard<br>
  Seed Rate, Spacing & Planting season: 1.5 x 1.5 m,<br>
  FIELD7:<br>
  Fertilizer dose: 10 kg<br>
  FIELD9:<br>
  Maturity Indices: Flowering start<br>
  Harvesting: fully develop/<br>
  FIELD12:<br>
  Yield: 10-Aug<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Bud Warm,<br>
  FIELD17:<br>
  Diseases: Wilt, Leaf<br>
  """ ), 

  'Jui' : mark_safe(""" 
  Soil: Sandy loam<br>
  Climate: Mild tropical<br>
  Varieties: Co-1 Mullai, Co-2 Mullai,<br>
  Propn method: Semi hard<br>
  Seed Rate, Spacing & Planting season: 1.8 x 1.8 m,<br>
  FIELD7:<br>
  Fertilizer dose: 10 kg<br>
  FIELD9:<br>
  Maturity Indices: Flowering start<br>
  Harvesting: fully develop/<br>
  FIELD12:<br>
  Yield: 8<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Bud Warm,<br>
  FIELD17:<br>
  Diseases: Wilt, Leaf<br>
  """ ),  

}