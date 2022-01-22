from itertools import groupby
# https://www.breastcancer.org/symptoms/understand_bc/risk/factors
import json
def write_json(data,filename="cancerdeathsbystate.json"):
    with open (filename, "r") as a:
        json.dump(data, a, indent=4)
    with open("apoth.json") as json_file:
        data= json.load(json_file)
    write_json(data)
risk_factors = [{'Factor':'Weight'}, {'Factor':'Diet'}, {'Factor':'Lack of excercise'},{'Factor':'Alcohol consumption'}, {'Factor':'Smoking'}, {'Factor':'Exposure to Estrogen'}, {'Factor':'Recent Oral contraceptive use'}, {'Factor':'Stress and Anxiety'}]
uncontrolled_risk_factors = [{'Factor':'Gender'}, {'Factor':'Age'}, {'Factor':'Family'}, {'Factor':'Personal history of breast cancer'}, {'Factor':'Race'}, {'Factor':'Radiation therapy to chest'}, {'Factor':'Breast cellular changes'}, {'Factor':'Exposure to estrogen'}, {'Factor':'Pregnancy'}, {'Factor':'DES Exposure'}]
risks_controlled = groupby(risk_factors, key=lambda x:x['Factor'])

breast_cancer_deaths_per_hundred_thousand_by_race = [{'Race':'White', 'Stat':19.4}, {'Race':'Black', 'Stat':27.1}, {'Race':'Asian/Pacific Islander', 'Stat':11.6}, {'Race':'America Indian/Alaska Native', 'Stat':15.6}, {'Race':'Hispanic', 'Stat':13.7}, {'Race':'Non-Hispanic', 'Stat':20.6}]
race_stats = groupby(breast_cancer_deaths_per_hundred_thousand_by_race, key=lambda x:x['Stat'])
for key, value in race_stats:
    print(key, list(value))
top_ten_obesity_rates_by_state = [{'State':'Missippi', 'Rate':40.80}, {'State':'West Virginia', 'Rate':39.70}, {'State':'Arkansas', 'Rate':37.40},
{'State':'Oklahoma', 'Rate':36.80}, {'State':'Kentucky', 'Rate':36.50}, {'State':'Tennessee', 'Rate':36.50}, {'State':'Alabama', 'Rate':36.10},
{'State':'Michigan', 'Rate':36}, {'State':'Louisiana', 'Rate':35.90}, {'State':'South Carolina', 'Rate':35.40}]
obesity_Rates = groupby(top_ten_obesity_rates_by_state, key=lambda x:x['Rate'])
for key, value in obesity_Rates:
    print(key, list(value))
top_ten_death_rate_cancer = [{'State':'Kentucky', 'Death rate':219.1}, {'State':'Tennessee', 'Death rate':210.3}, {'State':'Mississippi', 'Death rate':208.9},
{'State':'Louisiana', 'Death rate':208.6}, {'State':'Arkansas', 'Death rate':207.7}, {'State':'West Virginia', 'Death rate':207.4}, {'State':'Maine', 'Death rate':204.8}, {'State':'Alabama', 'Death rate':204.4}, {'State':'Indiana', 'Death rate':199.8}, {'State':'Delaware', 'Death rate':199.1}]
cancer_death_rates = groupby(top_ten_death_rate_cancer, key=lambda x:x['Death rate'])
deaths_by_State = [{'State':'California', 'Deaths':54732}, {'State':'Florida', 'Deaths':40592}, {'State':'New York', 'Deaths':35556}, {'State':'Texas', 'Deaths':34291}, {'State':'Pennsylvania', 'Deaths':29616}, {'State':'Ohio', 'Deaths':24702}, {'State':'Illinois', 'Deaths':24250}, {'State':'Michigan', 'Deaths':20094}, {'State':'New Jersey', 'Deaths':17171}, {'State':'North Carolina', 'Deaths':16724}]
overall_state_deaths = groupby(deaths_by_State, key=lambda x:x['Deaths'])
for key, value in overall_state_deaths:
    print(key, list(value))
opiod_deaths = [{'State':'California', 'Deaths':6198}, {'State':'Florida', 'Deaths':5268}, {'State':'Pennsylvania', 'Deaths':4377}, {'State':'Ohio', 'Deaths':4251}, {'State':'New York', 'Deaths':3617}, {'State':'New Jersey', 'Deaths':2805},
{'State':'Illinois', 'Deaths':2790}, {'State':'Michigan', 'Deaths':2385}]
opioid_grp = groupby(opiod_deaths, key=lambda x:x['Deaths'])
for key, value in opioid_grp:
    print(key, list(value))
#opoiods are a stress factor inidicator 