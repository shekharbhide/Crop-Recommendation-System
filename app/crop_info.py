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
    """,
     
    )
    ,  

    

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