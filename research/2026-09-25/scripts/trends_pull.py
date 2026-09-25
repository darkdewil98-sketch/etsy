import time, json
import pandas as pd
from pytrends.request import TrendReq
t = TrendReq(hl="en-US", tz=300, timeout=(10,30))
A="custom sweatshirt"
G={
"formats":["personalized ornament","custom mug","personalized blanket","custom tumbler"],
"formats2":["custom tote bag","custom hoodie","custom t shirt","personalized apron"],
"recipients":["teacher gift","nurse gift","retirement gift","grandma gift"],
"family":["mama sweatshirt","grandma sweatshirt","dad shirt","aunt shirt"],
"pets":["pet ornament","dog mom sweatshirt","cat mom shirt","pet portrait"],
"milestones":["pregnancy announcement","baby first christmas ornament","new home ornament","engagement gift"],
"couples":["bride sweatshirt","bachelorette shirts","couples ornament","anniversary gift"],
"hobbies":["book lover gift","gardening gift","fishing gift","coffee lover gift"],
"work":["coworker gift","boss gift","nurse sweatshirt","teacher sweatshirt"],
"q4":["family christmas shirts","thanksgiving shirt","christmas pajamas","halloween shirt"],
"misc":["memorial ornament","memorial gift","stocking stuffers","book club gift"],
}
frames={}
for name,kws in G.items():
    for attempt in range(4):
        try:
            t.build_payload([A]+kws, timeframe="today 5-y", geo="US")
            df=t.interest_over_time().drop(columns="isPartial")
            frames[name]=df; print("ok",name,flush=True); break
        except Exception as e:
            print("retry",name,e,flush=True); time.sleep(30*(attempt+1))
    time.sleep(10)
pd.concat(frames,axis=1).to_csv("trends_5y.csv")
